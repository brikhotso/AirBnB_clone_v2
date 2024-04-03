#!/usr/bin/python3
"""
Distributes an archive to web servers using Fabric.
"""
from fabric.api import env, run, put
from os.path import exists


env.user = 'ubuntu'
env.hosts = ['18.234.105.208', '18.204.10.184']


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

    delete_link_result = run('rm -rf /data/web_static/current')
    if delete_link_result.failed:
        return False

    create_link_result = run('ln -s {} /data/web_static/current'.format(
        folder_name))
    if create_link_result.failed:
        return False

    return True
