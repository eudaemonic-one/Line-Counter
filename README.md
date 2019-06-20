# Line-Counter

A command line tool to count lines (defaultly for markdown notes) under specified directory.

## Quick Start

Before running Line-Counter, you have to have **Python** installed on your running environment.

Step 1: Download Line-Counter.

Step 2: Open a terminal (cmd.exe on Windows).

Step 3: Use python environment to invole line-counter as follows.

    python line_counter.py -h

## Options

Optional arguments are showed as follows:

    -h, --help            show this help message and exit
    -d, --detailed        show more detailed result
    -i, --ignore-blank-lines
                          ignore blank lines in text files
    -v, --version         show program's version number and exit
    --start-dirs [START_DIRS [START_DIRS ...]]
                          analyze files under specified directories
    --prefix PREFIX       match files with specified prefix in filename
    --suffix SUFFIX       match files with specified suffix in filename (Default value is '.md')

## License

Line-Counter is licensed under the MIT License.
