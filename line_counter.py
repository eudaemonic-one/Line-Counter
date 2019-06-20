# -*- coding: utf-8 -*-

import argparse
import os
import re
import time

__version__ = '0.0.1'


class LineCounter:
    def __init__(self, args):
        self.result = {}
        self.file_count = 0
        self.line_count = 0
        self.blank_line_count = 0
        self.running_time = 0
        self.detailed = args.detailed
        self.ignore_blank_lines = args.ignore_blank_lines
        self.start_dirs = args.start_dirs
        self.prefix = args.prefix
        self.suffix = args.suffix

    def count_file_lines(self, filepath):
        line_count, blank_line_count = 0, 0
        for _, line in enumerate(open(filepath, 'r', encoding='UTF-8')):
            if self.ignore_blank_lines:
                if not line or line == '\n':
                    blank_line_count += 1
            line_count += 1
        return line_count, blank_line_count

    def archive_directory_recursively(self, curr_dir):
        dir_list = os.listdir(curr_dir)
        for curr_file in dir_list:
            path = os.path.join(curr_dir, curr_file)
            if os.path.isfile(path):
                pattern = r'(.*?)'
                if self.prefix:
                    pattern += self.prefix
                if self.suffix:
                    pattern += self.suffix
                match = re.search(pattern, path)
                if match:
                    line_count, blank_line_count = self.count_file_lines(path)
                    self.file_count += 1
                    self.line_count += line_count
                    self.blank_line_count += blank_line_count
                    print('file: {} lines: {}'.format(path, line_count))
            elif os.path.isdir(path):
                self.archive_directory_recursively(path)

    def show_result(self):
        print('{0} files, {1} lines, used {2}s'.format(self.file_count,
                                                       self.line_count,
                                                       self.running_time))
        if self.ignore_blank_lines:
            line_count_without_blank_lines = self.line_count - self.blank_line_count
            print('{} lines if ignoring blank lines'.format(line_count_without_blank_lines))
        if self.detailed:
            pass

    def start_count(self):
        start = time.time()
        for start_dir in self.start_dirs:
            self.archive_directory_recursively(start_dir)
        self.running_time = time.time() - start
        self.show_result()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Notes-Counter')
    parser.add_argument(
        '-d', '--detailed', action='store_true',
        help='show more detailed result')
    parser.add_argument(
        '-i', '--ignore-blank-lines', action='store_true',
        help='ignore blank lines in text files')
    parser.add_argument(
        '-v', '--version', action='version',
        version='Line-Counter {}'.format(__version__))
    parser.add_argument(
        '--start-dirs', action='store', nargs='*', default=os.getcwd(),
        help='analyze files under specified directories')
    parser.add_argument(
        '--prefix', type=str, action='store', default=None,
        help='match files with specified prefix in filename')
    parser.add_argument(
        '--suffix', type=str, action='store', default='.md',
        help='match files with specified suffix in filename')
    print(os.path.abspath('.'))
    args = parser.parse_args()
    counter = LineCounter(args)
    counter.start_count()
