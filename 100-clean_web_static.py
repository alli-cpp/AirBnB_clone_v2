#!/usr/bin/python3
# This fabfile deletes outdated versions of airbnb website
from os import listdir
from fabric.api import *

env.hosts = ["44.192.38.74", "35.174.176.158"]


def do_clean(number=0):
    """Cleans outdated versions of airbnb site"""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
