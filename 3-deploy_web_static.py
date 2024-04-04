#!/usr/bin/python3
"""
Create and distribute an archive to a web server
"""
from fabric.api import env, run, put, local
from os.path import exists
import os
import time

env.user = 'ubuntu'
env.hosts = ['18.234.105.208', '18.204.10.184']

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

def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    """
    if not exists(archive_path):
        return False

    put_result = put(archive_path, '/tmp/')
    if put_result.failed:
        return False

    archive_filename = archive_path.split('/')[-1]
    folder_name = '/data/web_static/releases/{}'.format(
        archive_filename.split('.')[0])
    run('mkdir -p {}'.format(folder_name))
    untar_result = run('tar -xzf /tmp/{} -C {}'.format(
        archive_filename, folder_name))
    if untar_result.failed:
        return False

    delete_archive_result = run('rm /tmp/{}'.format(archive_filename))
    if delete_archive_result.failed:
        return False

    move_files_result = run(
        'mv {}/web_static/* {}'.format(folder_name, folder_name))
    if move_files_result.failed:
        return False

    delete_web_static_folder_result = run(
        'rm -rf {}/web_static'.format(folder_name))
    if delete_web_static_folder_result.failed:
        return False

    delete_link_result = run('rm -rf /data/web_static/current')
    if delete_link_result.failed:
        return False

    create_link_result = run('ln -s {} /data/web_static/current'.format(
        folder_name))
    if create_link_result.failed:
        return False

    print("New version deployed!")
    return True

def deploy():
    """Create and distribute an archive to a web server."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
