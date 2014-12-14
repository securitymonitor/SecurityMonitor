#!/usr/bin/env python
import lib.bottle as bottle
from lib.Configuration import Configuration
from lib.bottle import route, template, debug, static_file, TEMPLATE_PATH, error, auth_basic, get, post, request, response, run, view, redirect, SimpleTemplate, HTTPError, abort, url
import os, sys, re



def authenticate(fn):
    def check_details(**kwargs):
        username = request.forms.get('username')
        password = request.forms.get('password')
        if (username == "666" and password == "666"):
            response.set_cookie("account", username, secret='54C5F98V4006B3j31sjf9733Q4jXu253g')
            return template('secure_page', page='Dashboard', url=url, notification='User login successful.')
        else:
            abort(401, "Sorry, access denied.") 
    return check_details



def restricted(fn):
    def check_credentials(**kwargs):   
        cookie_check = request.get_cookie("account", secret='54C5F98V4006B3j31sjf9733Q4jXu253g')
        if cookie_check:
            return fn(**kwargs)
        else:
            abort(401, "Sorry, access denied.")
    return check_credentials



def test(fn):
    def read_config_file(**kwargs):
        configfile = '/var/secmon/Config.txt'
                    
        file = open(configfile, 'r')
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
        return fn(**kwargs)
    return read_config_file

list_rules = os.listdir("/var/src/custom/rules/")

root = 'assets'

"""""""""""""""""
#################
# Routing table #
#################
"""""""""""""""""

@route('/')
@view('log-in')
def show_page_index():
    pass

@post('/')
@authenticate
def do_login():
    pass

@route('/dashboard')
@restricted
@view('secure_page')
def show__page_dashboard():
    return dict(page = 'Dashboard', url=url)

@route('/rules')
@restricted
@view('secure_page')
def show_page_rules():
    return dict(page = 'Rules', list_rules = list_rules, url=url)

@route('/rules/<rule>')
@restricted
@view('secure_page')
def show_page_rules_more(rule):
    return dict(page = rule, rule = rule, url=url)

@route('/settings')
@restricted
@view('secure_page')
def show_page_settings():
    return dict(page = 'Settings', url=url)

@route('/debug')
@view('secure_page')
def show__page_debug():
    return dict(page = 'Debug', url=url)

@route('/logout')
@restricted
@view('log-in')
def show__page_about():
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

#@error(500)
#@view('500')
#def error500(error):
#    return dict(url=url)

#@route('/assets/<filepath:path>')
@route('/assets/<filepath:path>', name='assets')
def server_static(filepath):
    return static_file(filepath, root='/var/secmon/assets')


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