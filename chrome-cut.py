from sys import exc_info
from chrome_cut.cli import cli

try:
    cli()
except Exception:
    print('Something went wrong: ' + exc_info()[0])
    print('please help me improve it by reporting on :')
    print('https://github.com/mrf345/chrome-cut-cli')
