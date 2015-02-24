#!/usr/bin/env python2.7

import json, os

"""
Part 1: Start-up checks
"""

def CreateConfigFile():
    dir_webserver_root = os.path.dirname(os.path.abspath(__file__)) + "/"
    dir_webserver_log = dir_webserver_root + "log/"
    dir_assets = dir_webserver_root + "assets/"
    dir_secmon_root = os.path.dirname(os.getcwd()) + "/src/"
    dir_secmon_core = dir_secmon_root + "core/"
    dir_secmon_rules = dir_secmon_root + "custom/rules/"
    file_auth_database = dir_webserver_root + "lib/auth.db"
    file_ssl_cert = dir_webserver_root + "lib/server.pem"
    server_port = raw_input("Port number:")

    # Write the values to a new config file.
    data = {"paths"  :{"dir_webserver_root" : dir_webserver_root, "dir_webserver_log" : dir_webserver_log, "dir_assets" : dir_assets, "dir_secmon_root" : dir_secmon_root, "dir_secmon_core" : dir_secmon_core, "dir_secmon_rules" : dir_secmon_rules, "file_auth_database" : file_auth_database, "file_ssl_cert" : file_ssl_cert, "server_port" : server_port}}
    with open(dir_webserver_root + 'lib/config.json', 'w') as outfile:
        json.dump(data, outfile)

def CreateSSLCertificate():
    key_file = os.path.dirname(os.path.abspath(__file__)) + "/lib/server.pem"
    os.system('openssl req -new -x509 -keyout ' + key_file + ' -out ' + key_file + ' -days 365 -nodes')

# Now loop trough the checks
if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "/lib/config.json") != True:
    CreateConfigFile()
if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "/lib/server.pem") != True:
    CreateSSLCertificate()
if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "/log") != True:
    os.system('mkdir log')
if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + "/pid") != True:
    os.system('mkdir pid')

# Import config file.
config_file_dir = os.path.dirname(os.path.abspath(__file__)) + "/lib/config.json"
config = json.loads(open(config_file_dir).read())

# Import other important requirements.
import lib.bottle as bottle
from lib.bottle import route, template, debug, static_file, TEMPLATE_PATH, error, auth_basic, get, post, request, response, run, view, redirect, SimpleTemplate, HTTPError, abort, url
import sys, re, sqlite3, time, datetime, random
from passlib.hash import sha512_crypt

# This function checks if the client is authenticated to view the requested page.
def restricted(fn):
    def check_credentials(**kwargs):

        # Connect to the database.
        conn = sqlite3.connect(config["paths"]["file_auth_database"])
        c = conn.cursor()
        c.execute("SELECT SessionID FROM secure_login")
        rows = c.fetchall()
        c.close()

        for row in rows:
            for col in row:
                username = request.get_cookie("username", secret=col)
                if username != None:
                    return fn(**kwargs)
                    break
                else:
                    pass
        abort(401)
    return check_credentials

"""
# Part 2: Routing table
    - Documentation: http://bottlepy.org/docs/0.12/
"""

@route('/')
@view('log-in')
def show_page_index():

    # Check for user database file.
    if os.path.isfile(config["paths"]["file_auth_database"]):
        # Userdatabase is found, show log-in page.
        pass
    else:
        # User database not found.
        # Start registration script.
        response.status = 303
        response.set_header('Location', '/install')

@route('/install')
def show__page_install():

    # This page should only be viewed if there is no user database.
    if os.path.isfile(config["paths"]["file_auth_database"]):
        # Userdatabase is found!
        # Kick user away from page.
        response.status = 303
        response.set_header('Location', '/logout')
    else:
        return template('install')

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

@route('/create_rule')
@restricted
@view('create_rule')
def show_page_rules():
    return dict(url=url, config=config)

@route('/users')
@restricted
@view('users')
def show_page_users():
    return dict(url=url, config=config)

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
@view('log-in')
def show__page_about():

    # Connect to the database.
    conn = sqlite3.connect(config["paths"]["file_auth_database"])
    c = conn.cursor()
    c.execute("SELECT SessionID FROM secure_login")
    rows = c.fetchall()

    for row in rows:
        for col in row:
            username = request.get_cookie("username", secret=col)
            if username != None:
                # Delete cookie
                response.delete_cookie("username", secret=col)
                c.execute("UPDATE secure_login SET SessionID = (?) WHERE Username = (?)", (None, str(username),))
                c.close()
                return dict(notification='User ' + str(username) + ' logout successful.')
                break
            else:
                pass
    c.close()

    # Now redirect the user back to the correct page.
    response.status = 303
    response.set_header('Location', '/')

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
@error(419)
@error(500)
@error(501)
@error(502)
@error(503)
@error(504)
@error(505)
@error(506)
@error(507)
@error(508)
@error(509)
@error(510)
@error(511)
@view('error')
def error404(e):
    return dict(url=url, e=e, debug=True)

# This router will make the whole /assets/ folder publicly accessable.
# Only static content (like HTML/CSS) should be placed in this directory for security reasons.
@route('/assets/<filepath:path>', name='assets')
def server_static(filepath):
    return static_file(filepath, root=config["paths"]["dir_assets"])

"""
# Part 3: Post actions
    - The code below will specify the behavior of the webserver on a HTML form submit.
"""

@post('/')
def do_login():

    # This post function will check if the user log-in credentials are correct.

    # Get the user details from the login form.
    username = request.forms.get('username')
    password = request.forms.get('password')

    try:
        # Connect to the database.
        conn = sqlite3.connect(config["paths"]["file_auth_database"])
        c = conn.cursor()
        c.execute("SELECT Password FROM secure_login WHERE Username = ?", (str(username),))
        rows = c.fetchall()
        c.close()
    except OperationalError:
        # If the user is not found in the database and we don't know the password, exit authentication.
        abort(403, "Authentication failed.")

    if len(rows) == 0:
        abort(403, "Authentication failed.") 
        
    # Check if the password from the user matches the passwored stored in the database.
    for row in rows:
        for col in row:
            check = sha512_crypt.verify(password, col)
            if check == True:
                # Password and username checks passed. Now proceeding for setting authenticated session cookie.

                # Generate unique session ID.
                session_start_time = str(datetime.datetime.now())
                secret = sha512_crypt.encrypt(session_start_time)

                # Save cookie secret and session start time to the db.
                conn = sqlite3.connect(config["paths"]["file_auth_database"])
                c = conn.cursor()
                c.execute("UPDATE secure_login SET SessionID = (?) WHERE Username = (?)", (secret, username))
                c.execute("UPDATE secure_login SET SessionStartTime = (?) WHERE Username = (?)", (session_start_time, username))
                conn.commit()
                c.close()

                response.set_cookie("username", username, secret=secret)
                return template('dashboard', url=url, config=config, notification= 'User ' + username + ' login successful.')
            else:
                abort(403, "Authentication failed.")

@post('/install')
def do_login():

    # This post function will create the first administrator if there is no user database.

    # As a safety measure check if the auth.db file exists

    if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "/lib/auth.db"):
        # Userdatabase is found!
        # Kick user away from page.
        response.status = 303
        response.set_header('Location', '/logout')
    else:
        # Get the user details from the registration form.
        username = request.forms.get('username')
        password = request.forms.get('password')

        # Hash the password.
        hash = sha512_crypt.encrypt(password)

        # Create the sqlite database with the right path.
        con = sqlite3.connect(config["paths"]["file_auth_database"])

        # Save the administrator in the database.
        with con:
            cur = con.cursor()    
            cur.execute("CREATE TABLE secure_login(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Username TEXT NOT NULL UNIQUE, Password BLOB NOT NULL, SessionID BLOB UNIQUE, SessionStartTime BLOB)")
            cur.execute("INSERT INTO secure_login(ID,Username,Password) VALUES (?,?,?)", (1,username,hash))

        # Now redirect the user back to the correct page.
        response.status = 303
        response.set_header('Location', '/')

@post('/dashboard')
@restricted
def post_dashboard():

    # This post function will restart the daemon.

    # This loop will start / stop the daemon based on current running status.
    daemon_running = os.path.isfile('/tmp/secmon.pid')

    if daemon_running:
        os.chdir(config["paths"]["dir_secmon_core"])
        os.system('python2.7 securitymonitor.py stop')
        time.sleep(1)
        msg = "Daemon stopped."
    else:
        os.chdir(config["paths"]["dir_secmon_core"])
        os.system('python2.7 securitymonitor.py start')
        time.sleep(1)
        msg = "Daemon started."

    # Reload dashboard html view.
    return template('dashboard', url=url, config=config, notification=msg)

@post('/logs')
@restricted
def post_page_logs():

    # This post function will check the selected options on the logs page.

    # Check which boxes are selected in the datatable
    form_data = request.forms.getall('chkBox')

    # Check if the list is empty (nothing is selected). If so, redirect the user to the user came from.
    if len(form_data) == 0:
        response.status = 303
        response.set_header('Location', '/logs')

    # Pass results back to the view
    return template('view_log', url=url, form_data=form_data, config=config)


@post('/rules')
@restricted
def post_page_rules():

    # This post function will create a new rule, modify a rule or remove a rule based on the user selection.

    # First request the selected checkboxes on the /rules page and the button that the user clicked.
    form_data = request.forms.getall('chkBox')
    submit_action = request.forms.getall('submit_btn')

    # This line is for debug purposes
    # return { "You pressed this button: " : submit_action, "Selected checkboxes are:" : form_data}
        
    # Check if the user has clicked the 'create' button. If so, show create_rule template where the user can create new rules.
    if 'create' in submit_action:
        response.status = 303
        response.set_header('Location', '/create_rule')

    # Check if the user has clicked the 'modify' button. If so, show view_rule template where the user can modify rules.
    elif 'modify' in submit_action:
        # If the checkboxes are empty (no user input), do nothing.
        if len(form_data) == 0:
            response.status = 303
            response.set_header('Location', '/rules')
        else:
            return template('view_rule', url=url, config=config, form_data=form_data)

    # If none of the above, the user wants to delete the selected rules.
    elif 'remove' in submit_action:
        # If the checkboxes are empty (no user input), do nothing.
        if len(form_data) == 0:
            response.status = 303
            response.set_header('Location', '/rules')
        else:
            for item in form_data:
                os.remove(config["paths"]["dir_secmon_rules"] + item)
            return template('rules', url=url, config=config, notification='Remove succesfull.')
   
    # If none of the above, do nothing.
    else:
        response.status = 303
        response.set_header('Location', '/rules')


@post('/create_rule')
@restricted
def post_page_create_rule():

    # This post function will save the form data into a new rule .txt file, restart the secmon daemon and redirect the user.

    # Serverside checks for the required fields to protect the security monitor daemon from incorrect input from the user.
    if len(request.forms.get('rule_name')) == 0:
        return template('create_rule', url=url, config=config, notification='The rule name field is empty, this field is required.')
    if len(request.forms.get('rule_description')) == 0:
        return template('create_rule', url=url, config=config, notification='The rule description field is empty, this field is required.')
    if len(request.forms.get('count')) == 0:
        return template('create_rule', url=url, config=config, notification='The count field is empty, this field is required.')
    if len(request.forms.get('action')) == 0:
        return template('create_rule', url=url, config=config, notification='The action field is empty, this field is required.')
    if len(request.forms.get('log')) == 0:
        return template('create_rule', url=url, config=config, notification='The log field is empty, this field is required.')
    if len(request.forms.get('match')) == 0:
        return template('create_rule', url=url, config=config, notification='The match field is empty, this field is required.')
    
    # If the user is performing an rule modification, there should be an existing rule that may or may not have changed by name.
    # If the rule name has changed, the rule will be recreated with the new name. This code will delete the old one.
    if request.forms.get('current_rulename') == None:
        pass
    elif request.forms.get('current_rulename') != request.forms.get('rule_name'): 
        os.remove(config["paths"]["dir_secmon_rules"] + request.forms.get('current_rulename') + '.txt')
    else:
        pass


    # Create new .txt rule file based on user input in the rule directory.
    new_rule_name = request.forms.get('rule_name')
    new_rule_name = config["paths"]["dir_secmon_rules"] + new_rule_name + '.txt'
    f = open(new_rule_name, "w")

    # These are the values that are submitted by the form.
    # rule_name
    # rule_description
    # source-ip-address
    # source-ip-port
    # target-ip-address
    # target-ip-port
    # protocol
    # count
    # interval
    # action
    # log
    # message
    # match

    # Write the values line by line in secmon readable format.
    f.write("NAME = '" + request.forms.get('rule_name') + "'\n")
    f.write("DESCRIPTION = '" + request.forms.get('rule_description') + "'\n")
    if len(request.forms.get('source-ip-address')) != 0:
        f.write("SOURCEIP = " + request.forms.get('source-ip-address') + "\n")
    if len(request.forms.get('source-ip-port')) != 0:
        f.write("SOURCEPT = " + request.forms.get('source-ip-port') + "\n")
    if len(request.forms.get('target-ip-address')) != 0:
        f.write("TARGETIP = " + request.forms.get('target-ip-address') + "\n")
    if len(request.forms.get('target-ip-port')) != 0:
        f.write("TARGETPT = " + request.forms.get('target-ip-port') + "\n")
    if len(request.forms.get('target-ip-port')) != 0:
        f.write("PROTOCOL = " + request.forms.get('protocol') + "\n")
    f.write("COUNT >" + request.forms.get('count') + "\n")
    if len(request.forms.get('interval')) != 0:
        f.write("INTERVAL = " + request.forms.get('interval') + "\n")
    f.write("ACTION = '" + request.forms.get('action') + "'\n")
    f.write("LOG = " + request.forms.get('log') + "\n")
    if len(request.forms.get('message')) != 0:
        f.write("MESSAGE = " + request.forms.get('message') + "\n")
    f.write("MATCH = " + request.forms.get('match') + "\n")
    f.close()

    # Restart the security monitor daemon so it will use the new rule.
    daemon_running = os.path.isfile('/tmp/secmon.pid')
    if daemon_running:
        os.system('python2.7 ' + config["paths"]["dir_secmon_core"] + 'securitymonitor.py stop')
        os.system('python2.7 ' + config["paths"]["dir_secmon_core"] + 'securitymonitor.py start')

    # Redirect the user back to the rules page.
    response.status = 303
    response.set_header('Location', '/rules')


@post('/users')
@restricted
def post_page_users():

    # This post script will delete the selected users from the database on the users page.

    # Request the selections the user has made in the HTML form.
    form_data = request.forms.getall('chkBox')
    submit_action = request.forms.getall('submit_btn')

    # Check if the user has clicked the 'create' button. If so, show create_user template where the user can create new users.
    if 'create' in submit_action:
        response.status = 303
        response.set_header('Location', '/create_user')

    # If none of the above, the user wants to delete the selected rules.
    elif 'remove' in submit_action:
        # If the checkboxes are empty (no user input), do nothing.
        if len(form_data) == 0:
            response.status = 303
            response.set_header('Location', '/users')

        for item in form_data:
            conn = sqlite3.connect(config["paths"]["file_auth_database"])
            c = conn.cursor()
            c.execute("DELETE FROM secure_login WHERE ID = ?", (item,))
            conn.commit()
            c.close()

        # Redirect back to the same page.
        return template('users', url=url, config=config, notification='User deleted successfully.')

    else:
        response.status = 303
        response.set_header('Location', '/users')


@post('/create_user')
@restricted
def post_create_user():

    # This post script will create a new user in the database or modify an existing one.

    # Request the selections the user has made in the HTML form.
    submit_action = request.forms.getall('submit_btn')

    if 'create' in submit_action:
        # Get the user details from the registration form.
        new_username = request.forms.get('new_uname')
        new_password = request.forms.get('new_passwd')
        new_password_check = request.forms.get('new_passwd_check')

        # Some serverside checks on the user input for the required fields to protect the server from invalid input.
        if len(new_username) == 0:
            return template('create_user', url=url, config=config, notification='The username field is required.')
        if len(new_password) == 0:
            return template('create_user', url=url, config=config, notification='The password field is required.')
        if new_password != new_password_check:
            return template('create_user', url=url, config=config, notification='Password mismatch.')

        # Hash the password.
        hash = sha512_crypt.encrypt(new_password)

        # Generate unique session ID.
        session_start_time = str(datetime.datetime.now())
        secret = sha512_crypt.encrypt(session_start_time)

        # Connect to the database.
        conn = sqlite3.connect(config["paths"]["file_auth_database"])
        c = conn.cursor()

        # Save new user in the database.
        c.execute("INSERT INTO `secure_login`(`ID`,`Username`,`Password`) VALUES (?,?,?)", (None, new_username, hash))
        conn.commit()
        c.close()

        # Redirect.
        response.status = 303
        response.set_header('Location', '/users')

    else:
        # Redirect.
        response.status = 303
        response.set_header('Location', '/users')

# This is a fix for the view directory.
TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "view")))

# Pass this code to the lib.bottledaemon so the server can start.
from lib.bottledaemon import daemon_run
if __name__ == "__main__":
	daemon_run()
