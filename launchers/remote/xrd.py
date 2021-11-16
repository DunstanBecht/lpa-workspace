#!/usr/bin/env python
# coding: utf-8

"""
Send files to the cluster and compile.
"""

from link import *

idf = input('\nIdentifier: ')
dirloc = f'../local' # directory containing files to be sent
jobnam = f'xrd' # name of the job
remdir = f'lpa-{jobnam}-{idf}' # receiving remote directory

with pysftp.Connection(hst, username=usr, password=pwd) as sftp:
    if not sftp.exists(remdir):
        sftp.mkdir(remdir)
    with sftp.cd(remdir):
        if input("\nSend files ? (y/n) ")=="y":
            for filnam in (f'{jobnam}.py', 'settings.py'):
                send(sftp, filnam, dirloc)
    print((f"\nRun the following command through ssh:\n"
           f"ssh compute-0-1-gpu\n"
           f"cd {remdir}\n"
           f"nohup python3 {jobnam}.py &"))

input("\nPress 'enter' to exit...")
