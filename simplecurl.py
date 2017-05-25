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
    Simple alternative to curl, when you don't want to have to use all those cryptic required parameters. It's a bit easier here
    (I think so).

    parameters:
       --method / --m   Is optional, because very often it's completely okay if it defaults to GET.
       -address / -a    Required, well, doh!
       --verbose / --v  If set, the body of response will be printed. Defaults to false.
       --data / --d     If you wish to submit JSON, you can do that too. I'm using ast eval to evaluate string into dictionary.
       
       Proper way to pass JSON as parameter:
        "{'key' : 'value', 'key':'value'}"
'''

#!/usr/bin/env python

import sys
import ast
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--method", "--m", help="HTTP request method (POST or GET)", default="GET")
parser.add_argument("-address", "-a", help="Specify url you wish to send request to.", required=True)
parser.add_argument("--verbose", "--v", help="Do you want to output the body of the response?", action="store_true", default=False)
parser.add_argument("--data", "--d", help="JSON data you wish to POST. Wrap the JSON in quotation marks.", default=False)


args = vars(parser.parse_args())


method = args["method"].upper()
address = args["address"].lower()
verbose = args["verbose"]

try:
    json_data = ast.literal_eval(args["data"])
except ValueError:
    print "Invalid JSON data"
    if not args["data"] == False:
        sys.exit()

if method == "GET":
    response = requests.get(address)

elif method == "POST":
    if not json_data: 
        response = requests.post(address)
    else:
        response = requests.post(address, json=json_data)
    
if not response == None:
    print "Address: ", address
    print "Status Code: ", response.status_code
    print "Headers: \n", response.headers
    if verbose:
        print "Body: ", response.body

