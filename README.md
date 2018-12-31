# Python Icon Generator

## Description

This is a super simple command line script written in Python that generates downsampled icons based on master resolution. As of now, the script only supports iOS icons.

## Usage

First, the script uses Pillow in order to do image processsing, so make sure that's installed on your machine

``` bash
pip install Pillow
```


Once that's installed you're good to go.

``` bash
optional arguments:
  -h, --help                     show this help message and exit
  -f FILE, --file FILE           file name of icon
  -n NEWFILE, --newfile NEWFILE  overrides the file name during saving
```

Pass the filename using the -f flag, if you want to use a different filename than the master filename, pass that using the -n flag

### Example

``` bash
python gen_icons.py -f some-file.png -n some-file-fancyname.png
```

Boom. That's it. Very simple.