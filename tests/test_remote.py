import os
import pyfakefs
import pytest

import pylcmodel


def test_find_config(fs):
    fs.create_file("/usr/src/app/.pylcmodel")
    os.chdir("/usr/src/app")

    assert "/usr/src/app/.pylcmodel" == pylcmodel.cli.find_config()


def test_read_config(fs):
    content = r"""hostname=lcmodel
user=lcm
password=lcm
"""

    fs.create_file("/usr/src/app/.pylcmodel", contents=content)

    config = pylcmodel.cli.read_config("/usr/src/app/.pylcmodel")

    assert {
        "hostname": "lcmodel",
        "port": "22",
        "user": "lcm",
        "password": "lcm",
        "persist_remote_files": False
    } == config


def test_remote_connection_password():
    print("working")
    pylcmodel.run_lcm_remote({
        "hostname":"lcmodel",
        "port": "22",
        "user":"lcm",
        "password": "lcm"
    }, {
        "OWNER": "",
        "KEY": 123456789,
        "TITLE": "Example Run",
        "FILRAW": "/usr/src/app/test_env/pylcmodel/test_data/svs_97.RAW",
        "FILBAS": "/home/lcm/.lcmodel/basis-sets/dummy.basis",
        "FILPS": "/usr/src/app/out.ps",
        "NUNFIL": 1024,
        "HZPPPM": 123.226056,
        "DELTAT": 0.000833,
        #"LPRINT": 6,
        #"FILPRI": "/usr/src/app/print.txt"
        #"FILTAB": 'svs_97.TABLE',
        #"LTABLE": 7,
        #"FILCSV": 'test_env/pylcmodel/test_data/svs_97.CSV',
        #"LCSV": 11,
        #"FILCOO": 'test_env/pylcmodel/test_data/svs_97.COORD',
        #"LCOORD": 9
    })

def test_remote_connection_key():
    print("working")
    pylcmodel.run_lcm_remote({
        "hostname":"lcmodel",
        "port": "22",
        "user":"lcm",
        "key_filename": "/root/.ssh/id_rsa",
    }, {
        "OWNER": "",
        "KEY": 123456789,
        "TITLE": "Example Run",
        "FILRAW": "/usr/src/app/test_env/pylcmodel/test_data/svs_97.RAW",
        "FILBAS": "/home/lcm/.lcmodel/basis-sets/dummy.basis",
        "FILPS": "/usr/src/app/out.ps",
        "NUNFIL": 1024,
        "HZPPPM": 123.226056,
        "DELTAT": 0.000833,
    })
