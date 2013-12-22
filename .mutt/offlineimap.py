#!/usr/bin/python
import os
import subprocess

def mailpasswd(indiunix_pass):
    indiunix_pass = os.path.basename(indiunix_pass)
    path = "/home/abhay/.mutt/%s.gpg" % indiunix_pass
    args = ["gpg", "--use-agent", "--quiet", "--batch", "-d", path]
    try:
        return subprocess.check_output(args).strip()
    except subprocess.CalledProcessError:
        return ""
