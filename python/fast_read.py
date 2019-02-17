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
   So apparently our ability to read fast is limited by the need of moving our eyeballs. This program's task is to eliminate the need for that
   and spit out the text right in front of you, so you can read faster. Simply specify a text file containing the text you want to read, and 
   there you go! read away :)
'''

#!/usr/bin/env python3

import sys
import shutil
import time



try:
    file_path = sys.argv[1]
except IndexError:
    print('Please specify text file path.')
    sys.exit()

text = open(file_path).read().split()
text = [item.replace("\xe2\x80\x99", "'") for item in text]



columns = shutil.get_terminal_size().columns

print("\n" * 10)

for word in text:
    print(word.center(columns), end="\r")
    time.sleep(0.15)


print("\n" * 50)
