#!/usr/bin/python3
"""Generate a .tgz archive from the contents of the web_static folder"""
import os
from fabric.api import local
import time


def do_pack():
    """Generate .tgz archive from web_static folder"""
    if not os.path.exists("versions"):
        os.makedirs("versions")

    timestamp = time.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)

    result = local(
        "tar -cvzf versions/{} web_static/".format(archive_name), capture=True)

    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None
