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

if input(f"\nSend {jobnam}.py ? (y/n) ")=="y":
    with pysftp.Connection(hst, username=usr, password=pwd) as sftp:
        if not sftp.exists(remdir):
            sftp.mkdir(remdir)
        with sftp.cd(remdir):
            for filnam in (f'{jobnam}.py',):
                send(sftp, filnam, dirloc)
print((f"\nRun the following command through ssh:\n"
       f"ssh compute-0-1-gpu\n"
       f"module load cuda/10.1\n"
       f"cd {remdir}\n"
       f"nohup python3 {jobnam}.py > benchmark.txt &"))

input("\nPress 'enter' to exit...")
