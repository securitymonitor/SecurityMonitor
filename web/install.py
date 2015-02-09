#!/usr/bin/env python
import json, os
from lib.termcolor import colored
import sqlite3 as lite
from passlib.hash import sha512_crypt


print
print
print
print " .d8888b.                  888b     d888                 "
print " d88P  Y88b                8888b   d8888                 "
print " Y88b.                     88888b.d88888                 "
print "   Y888b.   .d88b.  .d8888b888Y88888P888 .d88b. 88888b.  "
print "    'Y88b.d8P  Y8bd88P'   888 Y888P 888d88""88b888 '88b  "
print "      '88888888888888     888  Y8P  888888  888888  888  "
print "  8b  d88PY8b.    Y88b.   888   '   888Y88..88P888  888  "
print "  Y8888P'  'Y8888  'Y8888P888       888 'Y88P' 888  888  "
print "Install script for first run."
print
print
print


# Check if config file exists
print "-->> Checking for configuration file..."
if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "/lib/config.json"):
    print "-->>", colored('Found.:', 'green'), os.path.dirname(os.path.abspath(__file__)) + "/lib/config.json"
else:
    print "-->>", colored('Not found.', 'red')

    # Collect all the config values
    dir_webserver_root = os.path.dirname(os.path.abspath(__file__)) + "/"
    dir_webserver_log = dir_webserver_root + "log/"
    dir_assets = dir_webserver_root + "assets/"
    dir_secmon_root = os.path.dirname(os.getcwd()) + "/src/"
    dir_secmon_core = dir_secmon_root + "core/"
    dir_secmon_rules = dir_secmon_root + "custom/rules/"
    file_auth_database = dir_webserver_root + "lib/auth.db"
    file_ssl_cert = dir_webserver_root + "lib/server.pem"
    server_ip = '"0.0.0.0"'
    print "-->> Please specify the port you want to use for the application."
    server_port = raw_input("Port number:")

    # Write the values to a new config file
    data = {"paths"  :{"dir_webserver_root" : dir_webserver_root, "dir_webserver_log" : dir_webserver_log, "dir_assets" : dir_assets, "dir_secmon_root" : dir_secmon_root, "dir_secmon_core" : dir_secmon_core, "dir_secmon_rules" : dir_secmon_rules, "file_auth_database" : file_auth_database, "file_ssl_cert" : file_ssl_cert, "server_ip" : server_ip, "server_port" : server_port}}
    with open(dir_webserver_root + 'lib/config.json', 'w') as outfile:
        json.dump(data, outfile)

    print "-->>", colored('Config file created.', 'green')

# Create SSL certificate script
print "-->> Checking SSL file..."
if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "/lib/server.pem"):
    print "-->>", colored('SSL key found:', 'green'), os.path.dirname(os.path.abspath(__file__)) + "/lib/server.pem"
else:
    print "-->>", colored('SSL key not found.', 'red')
    key_file = os.path.dirname(os.path.abspath(__file__)) + "/lib/server.pem"

    os.system('openssl req -new -x509 -keyout ' + key_file + ' -out ' + key_file + ' -days 365 -nodes')
    print "-->>", colored('SSL key generated.', 'green')

print
print
print
print "-->>", colored('Install successful.', 'green')