#!/usr/bin/env python
import json, os

config = json.loads(open('lib/config.json').read())


import lib.bottle as bottle
from lib.bottle import route, template, debug, static_file, TEMPLATE_PATH, error, auth_basic, get, post, request, response, run, view, redirect, SimpleTemplate, HTTPError, abort, url
import sys, re, sqlite3, time
from passlib.hash import sha512_crypt


"""
# Global functions
  - Functions listed here are used on multiple pages and therefore only specified once.
"""

# This function checks if the client has an authentic cookie to view the requested page.
def restricted(fn):
    def check_credentials(**kwargs):   
        cookie_check = request.get_cookie("account", secret='54C5F98V4006B3j31sjf9733Q4jXu253g')
        if cookie_check:
            return fn(**kwargs)
        else:
            abort(401)
    return check_credentials

"""
# Routing table
  - All pages are listed in this table.
  - If someone calls a page that is not specified in this table, the server throws an 401 not authorized error. 
"""

@route('/')
@view('log-in')
def show_page_index():
    pass

@route('/dashboard')
@restricted
@view('dashboard')
def show__page_dashboard():
    return dict(url=url, config=config)

@route('/logs')
@restricted
@view('logs')
def show_page_rules():
    return dict(url=url, config=config)

@route('/logs/<log>')
@restricted
@view('view_log')
def show_page_logs_log(log):
    #log_path = config["paths"]["dir_secmon_core"] + log
    #with open(log_path) as f:
    #    log_content = f.readlines()
    return dict(url=url, log=log, config=config)

@route('/rules')
@restricted
@view('rules')
def show_page_rules():
    return dict(url=url, config=config)

@route('/rules/<rule>')
@restricted
@view('view_rule')
def show_page_rules_rule(rule):

    # Read the config file
    file = open(config["paths"]["dir_secmon_rules"] + rule, 'r')
    configlist = {}
    regex = '.+ = .*?'
    for line in file:
        match = re.findall(regex, line)
        if match:
            match = ''.join(match)
            x,y = line.split(match)
            y = y.strip('\n')
            y = y.strip(" ' ").strip('')
            match = match.replace(" ", '')           
            configlist.update({match:y})
            
    return dict(url=url, config=config, rule=rule, configlist=configlist)

@route('/users')
@restricted
@view('users')
def show_page_users():

    # Connect to the database
    conn = sqlite3.connect(config["paths"]["file_auth_database"])
    c = conn.cursor()

    # Select all users from the database
    c.execute("SELECT ID, Username from secure_login")
    
    # List all users in the variable result
    result = c.fetchall()
    c.close()
    return dict(url=url, rows=result)

@route('/users/<user>')
@restricted
@view('users_manage')
def show_page_users(user):
    return dict(url=url)

@route('/settings')
@restricted
@view('settings')
def show_page_settings():
    return dict(url=url)

@route('/create_user')
@restricted
@view('create_user')
def show_page_create_user():
    return dict(url=url)

@route('/logout')
@restricted
@view('log-in')
def show__page_about():

    # Delete cookie
    response.delete_cookie("account", secret='54C5F98V4006B3j31sjf9733Q4jXu253g')
    return dict(notification='User logout successful.')

@error(400)
@error(401)
@error(402)
@error(403)
@error(404)
@error(405)
@error(406)
@error(407)
@error(408)
@error(409)
@error(410)
@error(411)
@error(412)
@error(413)
@error(414)
@error(415)
@error(416)
@error(417)
@error(418)
@error(500)
@view('error')
def error404(e):
    return dict(url=url, e=e, debug=True)

@route('/assets/<filepath:path>', name='assets')
def server_static(filepath):
    return static_file(filepath, root=config["paths"]["dir_assets"])

"""
# Post actions
  - This application html post forms on quite some pages.
    The following code tells the server what to do on a post request.
"""

@post('/')
def do_login():

    # This post function will check if the user log-in credentials are correct.

    # First let's get the user details from the login form.
    username = request.forms.get('username')
    password = request.forms.get('password')

    try:
        # Connect to the database.
        conn = sqlite3.connect(config["paths"]["file_auth_database"])
        c = conn.cursor()

        # Request the password for the given username in the form.
        c.execute("SELECT Password FROM secure_login WHERE Username = ?", (str(username),))
        rows = c.fetchall()
        c.close()
    except OperationalError:
        # If the user is not found in the database and we don't know the password, exit authentication.
        abort(403, "Authentication failed, please try again.")

    if len(rows) == 0:
        abort(403, "Authentication failed, please try again.") 
        
    # Now let's check if the password from the user matches the passwored stored in the database.
    for row in rows:
        for col in row:
            check = sha512_crypt.verify(password, col)
            if check == True:
                response.set_cookie("account", username, secret='54C5F98V4006B3j31sjf9733Q4jXu253g')
                return template('dashboard', url=url, config=config, notification='{{username}} login successful.', username=username)
            else:
                abort(403, "Authentication failed, please try again.")

@post('/dashboard')
@restricted
def post_dashboard():
    # This script will restart the daemon.
    daemon_running = os.path.isfile('/tmp/secmon.pid')

    # This loop will start / stop the daemon based on current running status.
    if daemon_running:
        os.system('python ' + config["paths"]["dir_secmon_core"] + 'securitymonitor.py stop')
        time.sleep(1)
        msg = "Daemon stop command executed succesfully."
    else:
        os.system('python ' + config["paths"]["dir_secmon_core"] + 'securitymonitor.py start')
        time.sleep(1)
        msg = "Daemon start command executed succesfully."

    return template('dashboard', url=url, config=config, notification=msg)

@post('/logs')
@restricted
def post_page_logs():

    # Let's request the selections the user has made in the HTML form.
    form_data = request.forms.getall('chkBox')

    return template('view_log', url=url, form_data=form_data, config=config)


@post('/users')
@restricted
def post_page_users():

    # Let's request the selections the user has made in the HTML form.
    form_data = request.forms.getall('chkBox')

    # Now let's check if the list is empty. If so, return to the same page.
    if len(form_data) == 0:
        response.status = 303
        response.set_header('Location', '/users')

    else:

        for item in form_data:
            conn = sqlite3.connect(config["paths"]["file_auth_database"])
            c = conn.cursor()
            c.execute("DELETE FROM secure_login WHERE ID = ?", (item,))
            conn.commit()
            c.close()

        response.status = 303
        response.set_header('Location', '/users')

@post('/create_user')
@restricted
def post_create_user():

    # Get the user details from the registration form.
    new_username = request.forms.get('new_uname')
    new_password = request.forms.get('new_passwd')

    # Let's hash the password
    hash = sha512_crypt.encrypt(new_password)

    # Connect to the database
    conn = sqlite3.connect(config["paths"]["file_auth_database"])
    c = conn.cursor()

    # Save user in the database
    c.execute("INSERT INTO `secure_login`(`ID`,`Username`,`Password`) VALUES (?,?,?)", (None, new_username, hash))
    conn.commit()
    c.close()

    # Let's redirect back to the users list.
    response.status = 303
    response.set_header('Location', '/users')


@post('/rules/<rule>')
@restricted
def post_rules_rule(rule):
    rule_path = config["paths"]["dir_secmon_rules"] + rule
    rule_content = request.forms.get('content')

    with open(rule_path) as f:
        f.write(rule_content)

    list_rule_dir = os.listdir(config["paths"]["dir_secmon_rules"])

    return template('rules', url=url, list_rule_dir=list_rule_dir, notification='Rule edit successful.')

@post('/rules')
@restricted
def post_page_rules():

    # Check which boxes are selected in the datatable
    form_data = request.forms.getall('chkBox')

    # Pass results back to the view
    return template('view_rule', url=url, config=config, form_data=form_data)

'''
Fix for template path
'''

TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "view")))

'''
Call the daemon file to start the Python webserver daemon.
'''

from lib.bottledaemon import daemon_run
if __name__ == "__main__":
	daemon_run()