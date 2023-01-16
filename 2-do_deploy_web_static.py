#!/usr/bin/python3
"""Script that does the deployment"""
import os
from fabric.api import run, put, env


env.hosts = ['34.139.167.198', '34.138.129.5']


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    mkdir_cmd = "mkdir -p /data/web_static/releases/"
    rm_cmd = "rm -rf /data/web_static/releases/"
    deployed_success = "New Version Deployed!"
    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            filename = archive_path.split('/', 1)
            no_ext = filename[1].split('.', 1)
            file_name = no_ext[0]
            run(mkdir_cmd + file_name + "/")
            run("tar -zxf /tmp/" + filename[1] +
                " -C /data/web_static/releases/" +
                file_name + "/")
            run("rm /tmp/" + filename[1])
            run("mv /data/web_static/releases/" + file_name +
                "/web_static/* /data/web_static/releases/" + file_name + "/")
            run(rm_cmd + file_name + "/web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s /data/web_static/releases/" + file_name +
                "/ /data/web_static/current")
            print("{}".format(deployed_success))
            return True
        except:
            return False
    else:
        return False
