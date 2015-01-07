#!/usr/bin/env python
import json
config = json.loads(open('lib/config.json').read())

import lib.bottle as bottle
from lib.bottle import route, template, debug, static_file, TEMPLATE_PATH, error, auth_basic, get, post, request, response, run, view, redirect, SimpleTemplate, HTTPError, abort, url
import os, sys, re, sqlite3, os.path
from passlib.hash import sha512_crypt

"""
# Start Decorators

- Decorators are functions that are used on multiple pages.
  Example: the 'restriced' decorator checks if the user is authenticated by cookie, this logic will be used on almost every page of the application.

"""

def restricted(fn):
    def check_credentials(**kwargs):   

        # This function checks if the browser can supply the auth cookie. If it can, the page will load. If it can't, the page will abort.
        cookie_check = request.get_cookie("account", secret='54C5F98V4006B3j31sjf9733Q4jXu253g')
        if cookie_check:
            return fn(**kwargs)
        else:
            abort(401, "Sorry, access denied.")
    return check_credentials


"""
# Start Routing table
"""

@route('/')
@view('log-in')
def show_page_index():
    pass

@post('/')
def do_login():

    # Get the user details from the login form.
    username = request.forms.get('username')
    password = request.forms.get('password')

    # Connect to the database
    conn = sqlite3.connect(config["paths"]["file_auth_database"])
    c = conn.cursor()

    # Now let's request the password for the given username in the form
    c.execute("SELECT Password FROM secure_login WHERE Username = ?", (str(username),))
    rows = c.fetchall()
    c.close()

    # Now let's check if the password from the user matches the passwored stored in the database.
    for row in rows:
        for col in row:
            check = sha512_crypt.verify(password, col)
            if check == True:
                response.set_cookie("account", username, secret='54C5F98V4006B3j31sjf9733Q4jXu253g')
                return template('dashboard', url=url, notification='{{username}} login successful.', username=username)
            else:
                abort(403, "Incorrect login.2")

@route('/dashboard')
@restricted
@view('dashboard')
def show__page_dashboard():
    return dict(url=url)

@route('/rules')
@restricted
@view('rules')
def show_page_rules():
    return dict(url=url, config=config)

@route('/rules/<rule>')
@restricted
@view('rule_manage')
def show_page_rules_rule(rule):
    rule_path = config["paths"]["dir_secmon_rules"] + rule
    with open(rule_path) as f:
        rule_content = f.readlines()
    return dict(url=url, rule=rule, rule_content=rule_content)

@post('/rules/<rule>')
@restricted
def post_rules_rule(rule):
    rule_path = config["paths"]["dir_secmon_rules"] + rule
    rule_content = request.forms.get('content')

    with open(rule_path) as f:
        f.write(rule_content)

    list_rule_dir = os.listdir(config["paths"]["dir_secmon_rules"])

    return template('rules', url=url, list_rule_dir=list_rule_dir, notification='Rule edit successful.')

@route('/users')
@restricted
@view('users')
def show_page_users():

    # Connect to the database
    conn = sqlite3.connect(config["paths"]["file_auth_database"])
    c = conn.cursor()

    # Select all users from the database
    c.execute("SELECT ID, Username, Password from secure_login")
    
    # List all users in the variable result
    result = c.fetchall()
    c.close()
    return dict(url=url, rows=result)

@post('/users')
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


@route('/logout')
@restricted
@view('log-in')
def show__page_about():

    # Delete cookie
    response.delete_cookie("account", secret='54C5F98V4006B3j31sjf9733Q4jXu253g')
    return dict(notification='User logout successful.')

@error(401)
@view('401')
def error401(error):
    return dict(url=url)

@error(404)
@view('404')
def error404(error):
    return dict(url=url)

@route('/assets/<filepath:path>', name='assets')
def server_static(filepath):
    return static_file(filepath, root=config["paths"]["dir_assets"])


'''
Fix for template path
'''

TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "view")))

'''
Call the daemon file to start the Python webserver daemon.
'''

bottle.debug(True)
from lib.bottledaemon import daemon_run
if __name__ == "__main__":
	daemon_run()