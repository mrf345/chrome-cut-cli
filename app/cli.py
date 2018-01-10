# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from .core import get_ips, loop_ips, is_ccast, cancel_app, send_app
from .core import cast, reset_cc, shut, block
import click


def v_local_ip(a, b, value):
    """ to validate the local ip """
    try:
        if value[0] not in get_ips():
            raise click.BadParameter(
                'requires your currently connected IP address')
    except:
            raise click.BadParameter(
                'requires your currently connected IP address')
    return value[0]


def v_cast_ip(a, b, value):
    """ to validate if ip is chrome cast """
    try:
        if not is_ccast(value[0]):
            raise click.BadParameter(
                'require active chrome cast device IP, try scan command')
    except:
        raise click.BadParameter(
            'require active chrome cast device IP, try scan option to find it')
    return value[0]


def v_youtube_v(a, b, value):
    """ to validate if string is youtube video link, and return ready to u """
    try:
        if '/watch?' not in value[0]:
            raise click.BadParameter(
                'requires a valid youtube video link'
            )
    except:
        raise click.BadParameter(
            'requires a valid youtube video link'
        )
    return value[0].split('/watch?').pop()


def v_duration(a, v, value):
    """ to validate duration to be an int and not lesser than 0 """
    try:
        if type(value[0]) == int:
            if value[0] > 0:
                return value[0]
    except:
        pass
    raise click.BadParameter(
        'requires a valid integer, greater than 0'
    )


@click.group()
def cli():
    """
    Chrome-Cut 0.2 CLI \n
    Basic command line tool to scan detect and control chrome
    cast devices Find more: https://github.com/mrf345/chrome-cut-cli
    """
    pass


@click.command()
@click.option('--ip_address', '-ip', multiple=True,
              help='Your current IP address, to scan with',
              type=str, callback=v_local_ip)
def scan(ip_address):
    """scan the local network for chrome cast devices, with inserted IP"""
    active_CC = loop_ips(ip_address, True)
    if active_CC is None:
        click.echo(
            click.style(
                'No active chrome cast devices were found',
                bold=True, fg='red'))
    else:
        click.echo(
            click.style(
                'Active chrome cast devices :',
                bold=True, fg='blue'))
        click.echo()
        for index, ip in enumerate(active_CC):
            click.echo(
                click.style(
                    ' < ' + str(index + 1) + ' > ' + ip,
                    bg='red', fg='black', blink=True))
    click.echo()


@click.command()
@click.option('--ip_address', '-ip', multiple=True,
              help='Chrome cast IP address',
              type=str, callback=v_cast_ip)
def abort_stream(ip_address):
    """abort the currently streamed app on chrome cast device"""
    if cancel_app(ip_address):
        click.echo(
            click.style(
                ip_address + ' current stream got aborted.',
                bold=True, fg='blue'))
    else:
        click.echo(
            click.style(
                ip_address + ' failed to abort stream.',
                bold=True, fg='red'))


@click.command()
@click.option('--ip_address', '-ip', multiple=True,
              help='Chrome cast ip address',
              type=str, callback=v_cast_ip)
@click.option('--duration', '-d', multiple=True,
              help='Duration to wait between each streem command',
              type=int, callback=v_duration)
def loop_abort_stream(ip_address, duration):
    """
    repeatedly abort current stream, with a wait duration
    inbetween each abort
    """
    block(ip_address, duration, True)


@click.command()
@click.option('--ip_address', '-ip', multiple=True,
              help='Chrome cast IP address',
              type=str, callback=v_cast_ip)
@click.option('--youtube_video', '-v', multiple=True,
              help='Youtube video link to stream',
              type=str, callback=v_youtube_v)
def stream(ip_address, youtube_video):
    """stream youtube video through chrome cast device"""
    if send_app(ip_address, youtube_video):
        click.echo(
            click.style(
                ip_address + ' Video sent to chrome cast stream.',
                bold=True, fg='blue'))
    else:
        click.echo(
            click.style(
                ip_address + ' Video failed to stream.',
                bold=True, fg='red'))


@click.command()
@click.option('--ip_address', '-ip', multiple=True,
              help='Chrome cast ip address',
              type=str, callback=v_cast_ip)
@click.option('--youtube_video', '-v', multiple=True,
              help='Youtube video link to stream',
              type=str, callback=v_youtube_v)
@click.option('--duration', '-d', multiple=True,
              help='Duration to wait between each streem command',
              type=int, callback=v_duration)
def loop_stream(ip_address, youtube_video, duration):
    """
    repeatedly stream inserted youtube video, with a wait duration
    inbetween each repeat
    """
    cast(ip_address, youtube_video, duration, True)


@click.command()
@click.option('--ip_address', '-ip', multiple=True,
              help='Chrome cast IP address',
              type=str, callback=v_cast_ip)
def factory_restore(ip_address):
    """factory reset a chrome cast device with its IP adress"""
    if reset_cc(ip_address):
        click.echo(
            click.style(
                ip_address + ' Successful factory reset.',
                bold=True, fg='blue'))
    else:
        click.echo(
            click.style(
                ip_address + ' Failed to factory reset.',
                bold=True, fg='red'))


@click.command()
@click.option('--ip_address', '-ip', multiple=True,
              help='Chrome cast IP address',
              type=str, callback=v_cast_ip)
@click.option('--duration', '-d', multiple=True,
              help='Duration to wait between each factory restore command',
              type=int, callback=v_duration)
def loop_factory_restore(ip_address, duration):
    """
    repeatedly send factory reset command, with a wait duration
    inbetween each repeat
    """
    shut(ip_address, duration, True)


cli.add_command(scan)
cli.add_command(abort_stream)
cli.add_command(stream)
cli.add_command(loop_stream)
cli.add_command(factory_restore)
cli.add_command(loop_factory_restore)
cli.add_command(loop_abort_stream)

if __name__ == '__main__':
    cli()
