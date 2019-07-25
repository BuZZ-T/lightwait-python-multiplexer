#!/usr/bin/env python3.7
import asyncio
import sys
from configparser import ConfigParser
import subprocess

async def runTransmitter(transmitter, params):
    subprocess.call([transmitter, *params])

async def main():
    params = sys.argv[1:]

    config_parser = ConfigParser()
    config_parser.read('./multiplexer.conf')

    transmitter_keys = config_parser.options('transmitter')
    transmitter = [runTransmitter(config_parser.get('transmitter', key), params) for key in transmitter_keys]

    asyncio.gather(
        *transmitter
    )
if __name__ == '__main__':
    asyncio.run(main())
