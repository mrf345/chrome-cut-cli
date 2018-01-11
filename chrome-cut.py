from sys import exc_info
from chrome_cut import cli

try:
    cli()
except Exception:
    print(exc_info()[1])
    print('Something went wrong')
    print('please help me improve it by reporting on :')
    print('https://github.com/mrf345/chrome-cut-cli')
