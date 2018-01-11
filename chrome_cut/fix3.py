# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import asyncio
import click
import socket
from .core import get_ips, ports, counter, is_ccast


@asyncio.coroutine
# old style since using py3.4 to insure compatibility between CC-gui CC-cli
def det_ccast(ip, log=False):
    """
    to detect chrome cast with its known ports and return its ip
    and status in list, asyncrnioudfdslfr-sly.
    """
    results = is_ccast(ip)
    if log:
        global counter
        counter += 1
        click.clear()
        click.echo(
            click.style(
                'Completed : ' + str(int(counter * 100 / 255)) + '%',
                bold=True, fg='red'))
        click.echo()
        click.echo(
            click.style(
                ' == ' + ip,
                blink=False, bg='red', fg='black'))
        click.echo(
            click.style(
                ('[' + '=' * int(counter / 10)) + ']',
                blink=False, bg='red', fg='black'))
        click.clear()
    yield from asyncio.sleep(0)
    return [results, ip]
