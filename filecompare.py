#!/usr/bin/env python
import sys



file1 = []
file2 = []


with open(sys.argv[1]) as File1:
    content_1 = File1.readlines()

content_1 = [x.strip() for x in content_1]
print content_1



with open(sys.argv[2]) as File2:
    content_2 = File2.readlines()

content_2 = [x.strip() for x in content_2]
print content_2

if content_1 == content_2:
    print("\n Compare: Files are the same.\n")
else:
    print("\n Files are not the same.\n")
