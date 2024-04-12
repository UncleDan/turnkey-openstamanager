#!/usr/bin/python3
"""Set OpenSTAManager admin password

Option:
    --pass=     unless provided, will ask interactively
    --domain=   unless provided, will ask interactively
                DEFAULT=www.example.com
"""

import sys
import getopt
import hashlib
import crypt
import re
from libinithooks import inithooks_cache

from libinithooks.dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

DEFAULT_DOMAIN='www.example.com'

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'domain='])
    except getopt.GetoptError as e:
        usage(e)

    domain = ''
    password = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--domain':
            domain = val

    if not password:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        password = d.get_password(
            "OpenSTAManager password",
            "Enter new password for the OpenSTAManager 'admin' account.")

    if not domain:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        domain = d.get_input(
            "OpenSTAManager Domain",
            "Enter the domain to serve OpenSTAManager.",
            DEFAULT_DOMAIN)

    if domain == "DEFAULT":
        domain = DEFAULT_DOMAIN

    inithooks_cache.write('APP_DOMAIN', domain)

    conf = "/var/www/openstamanager/data/config-internal.php"

    lines = []
    with open(conf, 'r') as fob:
        for line in fob:
            match = re.search("'passwordSalt' => '([^']*)',", line)
            if match != None:
                normSalt = ('$6$%s$' % match.group(1))
                hashed = crypt.crypt(hashlib.md5(password.encode('utf8')).hexdigest(), normSalt).replace(normSalt, '')

                m = MySQL()
                m.execute('UPDATE openstamanager.user SET password=%s WHERE user_name=\"admin\"', (hashed))
            if 'siteUrl' in line:
                line = re.sub("=> '([^']*)'", f"=> 'https://{domain}'", line)

            lines.append(line)

    with open(conf, 'w') as fob:
        fob.writelines(lines)

if __name__ == "__main__":
    main()
