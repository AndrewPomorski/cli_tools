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
    I used to make some HTML documents backups, and sometimes I got confused with it's names, so I wanted to have a quick way to tell
    if those files are the same. This program does EXACTLY that. This is by no means advanced, git diff like program, it only checks, 
    whether the files are absoultely identical.
'''

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
