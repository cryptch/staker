#!/usr/bin/env python3

from datetime import datetime
import json
import time
from coind import Coind
import config

coind = Coind(config.COIND_NAME, config.COIND_TYPE, config.COIND_PATH, config.COIND_DEBUG)


def get_staking_command():
    """
    Find stake command
    Normaly command will be one of theses:
    - getstakingstatus
    - getstakinginfo
    """
    help_res = coind.run('help | grep getstak').split('\n')
    command = ''
    for cmd in help_res:
        if cmd in ['getstakingstatus', 'getstakinginfo']:
            command = cmd

    return command


def is_staking(cmd):
    """
    Check if stake is active

    :param cmd: coind stake check command
    :type cmd: string
    """
    if not cmd: return False

    res = coind.run(cmd)
    status = json.loads(res)
    name = 'staking status' if cmd == 'getstakingstatus' else 'staking'
    return status[name]


def staker():
    """
    Check stake situation and active it if need
    If wallet is down, start too
    """
    if coind.is_running():
        command = get_staking_command()
        if is_staking(command):
            print('['+str(datetime.now())+']: Stake already active')
        else:
            cmd = 'walletpassphrase "'+config.UNLOCK_PASS+'" 99999999'
            if config.UNLOCK_ONLY_STAKE: cmd += ' true'
            res = coind.run(cmd)
            if not res: res = 'Stake activated'
            print('['+str(datetime.now())+']: '+res)
    else:
        print('['+str(datetime.now())+']: Starting daemon')
        coind.run('-daemon')
        time.sleep(60)
        staker()


if __name__ == '__main__':
    staker()
