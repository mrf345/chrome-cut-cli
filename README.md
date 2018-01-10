<p align='center'>
<img src='https://chrome-cut.github.io//logo.png' width='40%'>
</p>

# chrome-cut-cli
### Basic command line tool to scan, detect, stream and control chrome cast devices. Great for pranking someone with a chrome cast device in your local network. Plus there is a [GUI version here][3fb05a7a].

  [3fb05a7a]: https://github.com/mrf345/chrome-cut "GUI version"

<p align='center'>
<img src='https://chrome-cut.github.io/chrome-cut-cli.gif'>
</p>

## Setup:
### - With pip:
1. `pip install chrome-cut`
2. `chrome-cut --help`

### - with git:
1. `git clone https://github.com/mrf345/chrome-cut-cli.git`
2. `cd chrome-cut-cli`
3. `pip install requirements.txt`
4. `python chrome-cut.py`

#### - Or you can download binaries for Windows and Mac OS from [SoruceForge](https://sourceforge.net)
## Commands:
`chrome-cut.py --help` ` chrome-cut.py command --help`
```
Commands:
  abort_stream          abort the currently streamed app on chrome...
  factory_restore       factory reset a chrome cast device with its...
  loop_abort_stream     repeatedly abort current stream, with a wait...
  loop_factory_restore  repeatedly send factory reset command, with a...
  loop_stream           repeatedly stream inserted youtube video,...
  scan                  scan the local network for chrome cast...
  stream                stream youtube video through chrome cast...
```
## Credit:
- [Blog][7aef02c6] that inspired this tool.
- [Click][479b1383] amazing Python command-line utility library.

  [7aef02c6]: https://fiquett.com/2013/07/chromecast-traffic-sniffing/ "Blog link"
  [479b1383]: http://click.pocoo.org/5/ "Click website"
