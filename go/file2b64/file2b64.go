/*
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
*/
package main

import (
    "bufio"
    "encoding/base64"
    "fmt"
    "io/ioutil"
    "os"
		"flag"
)

func main() {
	filePath := parseArgs()
	f, _ := os.Open(filePath)

	reader := bufio.NewReader(f)
	content, _ := ioutil.ReadAll(reader)

	encoded := base64.StdEncoding.EncodeToString(content)
	
	fmt.Println(encoded)
}

func parseArgs() string {
	fileNamePtr := flag.String("filepath", "", "A path to file you wish to convert")
	flag.Parse()
	return *fileNamePtr
}

