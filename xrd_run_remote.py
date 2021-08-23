#!/usr/bin/env python
# coding: utf-8

"""
Send files to the cluster and compile.
"""

import pysftp
import os
import time
import re

from logins import hostname, username, password
from remote import custom_put, custom_execute

print("[REMOTE XRD]")

rem_dir = 'workspace-xrd' # remote directory
script = 'xrd_run.py'

with pysftp.Connection(hostname, username=username, password=password) as sftp:
    if not sftp.exists(rem_dir):
        sftp.mkdir(rem_dir)
    with sftp.cd(rem_dir):
        if input("\nSend files ? (y/n) ")=="y":
            custom_put(sftp, 'xrd')
            custom_put(sftp, script)
            custom_put(sftp, 'settings.py')
            custom_put(sftp, 'logins.py')
    print("\nRun the following command with ssh:")
    print('cd '+rem_dir+'; nohup python3 '+script+' &')

input("\nPress 'enter' to exit...")
