# lightwait-python-multiplexer

This is a simple multiplexing transmitter in the [lightwait-stack](https://github.com/BuZZ-T/lightwait). It's written in python with less than 30 lines of code.

It just calls every configured transmitter repeating the given CLI params. It does this asynchronously using `asyncio.gather(...)` (requiring python3.7).
It uses the CLI-based [lightwait-tt](https://github.com/BuZZ-T/lightwait#trigger---transmitter) communiction protocol.

Its main usecase will be probably demonstration and testing purposes, but feel free to use in production, once you have a proper need for this!

## Configuration

Place a configuration file named "multiplexer.conf" in the same folder as the python script. One default config file is added to the git repository.

The basic structure is one section named "transmitter" containing option entries with arbitrary keys and the file path to a [lightwait-transmitter](https://github.com/BuZZ-T/lightwait#transmitter) as value.

### Example
    [transmitter]
    first=/bin/echo
    second=../lightwait-python-tcp-udp.git/lightwait-tcp-udp.py

## Tested with

| OS | Version | python | Result | Reason
|-|-|-|-|-
| Ubuntu | 18.04 | 2.7.15+ | ✘ | `asyncio.run` requires python >=3.7
| Ubuntu | 18.04 | 3.6.8 | ✘ | `asyncio.run` requires python >=3.7
| Ubuntu | 18.04 | 3.7.3 | ✔