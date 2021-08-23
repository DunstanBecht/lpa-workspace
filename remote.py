#!/usr/bin/env python
# coding: utf-8

"""
Tools for remote control.
"""

import pysftp
import os
import re

def custom_put(
    sftp: pysftp.Connection,
    node: str,
    ignore: str = None
) -> None:
    """
    Send files via sftp.

    Input:
        sftp: pysftp connection
        node: file or directory to send recursively
        ignore: regular expression of the nodes that should not be sent
    """
    if ignore==None or re.search(ignore, node)==None:
        print("(>) "+ node)
        if os.path.isfile(node):
            sftp.put(node, node)
        else:
            if not sftp.exists(node):
                sftp.mkdir(node)
            for child in os.listdir(node):
                custom_put(sftp, node + "/" + child, ignore)

def custom_execute(
    sftp: pysftp.Connection,
    c: str,
) -> str:
    """
    Execute the command c remotely.

    Input:
        sftp: pysftp connection
        c: bash command to execute
    """
    lines = [out.decode('utf-8').strip()+"\n" for out in sftp.execute(c)]
    if len(lines) == 1:
        return lines[0]
    return lines
