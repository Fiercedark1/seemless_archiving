#!/bin/bash

if ! rpm -qa | grep -qw cronie; then
    yum -y install cronie && echo -e "#0 * * * * /path/to/python_scripts/untar_revive.py\n0 3 * * * /path/to/python_scripts/untar_revive.py #every 3 hours\n#0 * * * * /path/to/python_scripts/time_limit.py #every hour\n0 3 * * * /path/to/python_scripts/time_limit.py #every 3 hours" >> /var/spool/cron/$USER
else
    echo -e "#0 * * * * /path/to/python_scripts/untar_revive.py\n0 3 * * * /path/to/python_scripts/untar_revive.py #every 3 hours\n#0 * * * * /path/to/python_scripts/time_limit.py #every hour\n0 3 * * * /path/to/python_scripts/time_limit.py #every 3 hours" >> /var/spool/cron/$USER
fi
