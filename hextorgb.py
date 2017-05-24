#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--rgba', action="store_true")
args, leftovers = parser.parse_known_args()

try:
    input_val= sys.argv[1]
except IndexError:
    print "Usage: phator #123123"
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
