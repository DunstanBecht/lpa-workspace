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

rem_dir = 'workspace-input' # remote directory
job = 'input_analyses' # .py and .job stem name

with pysftp.Connection(hostname, username=username, password=password) as sftp:
    if not sftp.exists(rem_dir):
        sftp.mkdir(rem_dir)
    with sftp.cd(rem_dir):
        if input("\nSend files ? (y/n) ") == "y":
            custom_put(sftp, job+'.job')
            custom_put(sftp, job+'.py')
            custom_put(sftp, 'settings.py')
        if input("\nSubmit job ? (y/n) ") == "y":
            out = custom_execute(sftp, 'cd '+rem_dir+'; sbatch '+job+'.job')
            id = out.split(" ")[-1].strip("\n")
            out = custom_execute(sftp, 'scontrol show jobid -dd '+id)
            print("".join(out))
            if input("\nWait results ? (y/n) ") == "y":
                output_fil = "slurm-"+id+".out"
                output_dir = username+"-"+id
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
                if sftp.exists(output_dir):
                    print("(<) "+output_dir)
                    sftp.get_r(output_dir, "")
                else:
                    print(output_dir+" not found")
                if sftp.exists(output_fil):
                    print("(<) "+output_fil)
                    sftp.get(output_fil, output_fil)
                else:
                    print(output_fil+" not found")

input("\nPress 'enter' to exit...")
