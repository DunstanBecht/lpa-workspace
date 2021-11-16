#!/usr/bin/env python
# coding: utf-8

"""
Perform remote spatial analyses of the distributions.
"""

from link import *

idf = input('\nIdentifier: ')
dirloc = f'../local' # directory containing files to be sent
jobnam = f'stats' # name of the job
remdir = f'lpa-{jobnam}-{idf}' # receiving remote directory

with pysftp.Connection(hst, username=usr, password=pwd) as sftp:
    if not sftp.exists(remdir):
        sftp.mkdir(remdir)
    with sftp.cd(remdir):
        if input("\nSend files ? (y/n) ") == "y":
            for filnam in (f'{jobnam}.py', f'{jobnam}.job', f'settings.py'):
                send(sftp, filnam, dirloc)
        if input("\nSubmit job ? (y/n) ") == "y":
            outstr = execute(sftp, f'cd {remdir}; sbatch {jobnam}.job')
            jobidf = outstr.split(" ")[-1].strip("\n")
            outstr = execute(sftp, f'scontrol show jobid -dd {jobidf}')
            print("".join(outstr))

input("\nPress 'enter' to exit...")
