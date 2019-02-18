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

