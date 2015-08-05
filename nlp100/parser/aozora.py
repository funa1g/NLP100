# /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import re

class AozoraParser:

    def __init__(self):
        self.text = []
        self.__comment_pat = re.compile('(※)?［＃.*?］')
        self.__ruby_pat = re.compile('《.*?》')
        self.__marker = '｜'

    def _read(self, path):
        f = open(path, "r")
        for line in f:
            self.text.append(self._clean(line)) 
        f.close()

    def _clean(self, line):
        line = self._delete_comment(line)
        line = self._delete_ruby(line)
        line = self._delete_marker(line)
        return line

    def _delete_comment(self, line):
        return self.__comment_pat.sub("", line)

    def _delete_ruby(self, line):
        return self.__ruby_pat.sub("", line)

    def _delete_marker(self, line):
        return line.replace(self.__marker, "")

    def _write(self, path):
        f = open(path, "w")
        for line in self.text:
            f.write(line)
        f.close()


def parse(src, dest):
    parser = AozoraParser()
    parser._read(src)
    parser._write(dest)


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 3:
        print "Usage: python aozora.py [src] [dest]"
        sys.exit()
    src = argv[1]
    dest = argv[2]
    parse(src, dest)
