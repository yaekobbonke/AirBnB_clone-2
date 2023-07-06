#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the
# contents of the web_static folder of my AirBnB Clone repo
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """return the archive path if the archive has been correctly
    generated. Otherwise, it should return None"""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
