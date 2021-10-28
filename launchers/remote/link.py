#!/usr/bin/env python
# coding: utf-8

"""
Tools for the communication with the supercomputer.
"""

import pysftp
import os
import re

try:
    from logins import hst, usr, pwd
except:
    hst = 'your-hostanme'
    usr = 'your-username'
    pwd = 'your-password'

def send(
    cnx: pysftp.Connection,
    nam: str,
    pth: str = '',
    ign: str = None
) -> None:
    """
    Send files to the supercomputer.

    Input:
        cnx (pysftp.Connection): pysftp connection
        nam (str): file or directory to send recursively
      **pth (str): path to the file or directory to send (default: '')
      **ign (str): regular expression of the nodes not sent (default: None)
    """
    pthnam = os.path.join(pth, nam)
    if ign==None or re.search(ign, pthnam)==None:
        print(f"(>) {pthnam}")
        if os.path.isfile(pthnam):
            cnx.put(pthnam, nam)
        else:
            if not cnx.exists(nam):
                cnx.mkdir(nam)
            for child in os.listdir(pthnam):
                send(cnx, f"{nam}/{child}", pth, ign)

def execute(
    cnx: pysftp.Connection,
    cmd: str,
) -> list:
    """
    Execute the command on the supercomputer.

    Input:
        cnx (pysftp.Connection): pysftp connection
        cmd (str): bash command to execute
    """
    lines = [out.decode('utf-8').strip()+"\n" for out in cnx.execute(cmd)]
    if len(lines) == 1:
        return lines[0]
    return lines
