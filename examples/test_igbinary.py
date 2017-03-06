#!/usr/bin/python
# -*- coding: utf8 -*-

import commands

from igbinary import IgBinaryReader

def main():
    num = 100000
    status, msg = commands.getstatusoutput('php -r "print(igbinary_serialize(%s));"' % num)
    print msg
    print '\n\n'
    if status == 0:
        print IgBinaryReader(msg).readvalue()

if __name__ == '__main__':
    main()
