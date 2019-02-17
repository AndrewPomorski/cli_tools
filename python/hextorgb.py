'''
    MIT License

    Copyright (c) 2017 Andrew Pomorski

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
'''


'''
    This program converts 6-character hex values to RGB or RGBA codes. It only adds 1 at the end of RGBA,
    So it's not very useful, but whatever. You can add optional parameter --rgba to output RGBA value.
'''


#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--rgba', action="store_true")
args, leftovers = parser.parse_known_args()

try:
    input_val= sys.argv[1]
except IndexError:
    print "Usage: program_alias #123123"
    sys.exit()

hex_val = input_val

if not len(hex_val) == 6:
    print "Invalid use. Please use 6-character HEX code."
    sys.exit()

r = int(hex_val[0:2], 16)
g = int(hex_val[2:4], 16)
b = int(hex_val[4:6], 16)

if args.rgba is not False:
    print 'rgba(' + str(r) + ',' + str(g) + ',' + str(b) + ',1)'
else:
    print 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'
