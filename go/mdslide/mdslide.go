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

// This script is designed to work with the Gatsby Starter Deck (https://github.com/fabe/gatsby-starter-deck) 
// it's meant to provide an easy way to quickly switch the slides to be displayed in the web client.
// Is it an overkill? probably.
// was it fun to make? yes.

package main

import (
	"flag"
	"io/ioutil"
	"io"
	"log"
	"fmt"
	"os"
)

func main() {
	deckName := parseArgs()
	if (len(deckName) == 0) {
		log.Fatal("Deck name not provided")
	}
	if (fetchDeck(deckName)) {
		fmt.Println("deck found")
	} else {
		log.Fatal("Deck not found")
	}
}


func parseArgs() string {
	slideNamePtr := flag.String("deck", "", "A name of deck you want to use")
	flag.Parse()
	return *slideNamePtr
}

func copyDeck(src, dst string) (int64, error) {
	sourceFileStat, err := os.Stat(src)
	if err != nil {
		return 0, err
	}

	if !sourceFileStat.Mode().IsRegular() {
		return 0, fmt.Errorf("%s is not a regular file", src)
  }

	source, err := os.Open(src)
	
	if err != nil {
		return 0, err
	}

	defer source.Close()

	destination, err := os.Create(dst)

	if (err != nil) {
		return 0, err
	}

	defer destination.Close()

	nBytes, err := io.Copy(destination, source)
  return nBytes, err
}


func fetchDeck(deckName string) bool {
	files, err := ioutil.ReadDir("./decks")
	fileFound := false

	if err != nil {
		log.Fatal(err)
	}
	for _, f := range files {
		if (f.Name() == deckName) {
			fileFound = searchForSlides(f.Name())
		}

	}
	return fileFound
}

func searchForSlides(dirName string) bool {
	files, err := ioutil.ReadDir("./decks/" + dirName)
	slidesFound := false
	if err != nil {
		log.Fatal(err)
	}
	for _, f := range files {
		if (f.Name() == "slides.md") {
			slidesFound = true	
		}
	}
	return slidesFound
}
