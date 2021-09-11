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

remdir = 'workspace-xrd' # remote directory
script = 'xrd_run.py'

with pysftp.Connection(hostname, username=username, password=password) as sftp:
    if not sftp.exists(remdir):
        sftp.mkdir(remdir)
    with sftp.cd(remdir):
        if input("\nSend files ? (y/n) ")=="y":
            custom_put(sftp, script)
            custom_put(sftp, 'settings.py')
            custom_put(sftp, 'logins.py')
    print("\nRun the following command with ssh:")
    print('cd '+remdir+'; nohup python3 '+script+' &')

input("\nPress 'enter' to exit...")
