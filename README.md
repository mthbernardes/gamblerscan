# gamblerscan

#### Python scanner for open ports (1..1024)

## Install

Just it:

```
$ git clone https://github.com/mthbernardes/gamblerscan
```

## Usage

```
usage: gamblerscan.py [-h] [-m MIN] [-M MAX] host

positional arguments:
  host               host to check doors

optional arguments:
  -h, --help         show this help message and exit
  -m MIN, --min MIN  Port to start check
  -M MAX, --max MAX  Port to finish check
```

Example:

```
python gamblerscan.py www.github.com
```