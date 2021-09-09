#!/usr/bin/env python
# coding: utf-8

"""
Send the files, submit the task and retrieve the results.
"""

import pysftp
import time

from logins import hostname, username, password
from remote import custom_put, custom_execute

print("[INPUT REMOTE ANALYSES]")

remdir = 'workspace-input' # remote directory
job = 'input_analyses' # .py and .job stem name

with pysftp.Connection(hostname, username=username, password=password) as sftp:
    if not sftp.exists(remdir):
        sftp.mkdir(remdir)
    with sftp.cd(remdir):
        if input("\nSend files ? (y/n) ") == "y":
            custom_put(sftp, job+'.job')
            custom_put(sftp, job+'.py')
            custom_put(sftp, 'settings.py')
        if input("\nSubmit job ? (y/n) ") == "y":
            out = custom_execute(sftp, 'cd '+remdir+'; sbatch '+job+'.job')
            id = out.split(" ")[-1].strip("\n")
            out = custom_execute(sftp, 'scontrol show jobid -dd '+id)
            print("".join(out))
            if input("\nWait results ? (y/n) ") == "y":
                outfil = "slurm-"+id+".out"
                outdir = username+"-"+id
                terminated = False
                while not terminated:
                    terminated = True
                    lines = custom_execute(sftp, 'squeue')
                    for l in lines:
                        if id in l:
                            terminated = False
                            date = "("+time.strftime("%Y-%m-%d %H:%M:%S")+") "
                            print(date+" ".join(l.split()))
                    time.sleep(10)
                time.sleep(10)
                if sftp.exists(outdir):
                    print("(<) "+outdir)
                    sftp.get_r(outdir, "")
                else:
                    print(outdir+" not found")
                if sftp.exists(outfil):
                    print("(<) "+outfil)
                    sftp.get(outfil, outfil)
                else:
                    print(outfil+" not found")

input("\nPress 'enter' to exit...")
