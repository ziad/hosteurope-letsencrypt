# Add new domain to a certificate.
# File is a modifed copy of verlaengern.py created by Ziad Hakim 

import json
import os

from shared import domain_list, config_file
 
with open(config_file('einstellungen.json')) as cfg_file:
    config = json.load(cfg_file)
staging = config['staging']
cert = config['cert-name']

# certbot Kommando zusammenbauen
cmd = 'certbot certonly -n --manual --manual-auth-hook "python3 validate.py" --agree-tos --manual-public-ip-logging-ok'
# we can get the cert name using 'certbot certificates'
cmd += ' --cert-name ' + cert
if staging:
    cmd += ' --staging'
cmd += domain_list

# Sicherheitsabfrage
print(cmd)
answer = input('Modify the domains this certificate contains (j/n): ')
if answer != 'j':
    print('Abbruch, es wurde kein Zertifikat geändert.')
    exit(0)

# neues Zertifikat erstellen
os.system(cmd)
