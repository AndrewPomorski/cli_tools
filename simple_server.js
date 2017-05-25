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

/*
 * 
 * Express.js is required for that script to work: 
 *
 *  npm install --save express
 *
 * Or add it to your package.json:
 *
 * "express" : "*"
 *
 * This script is a simple one-liner for static html files. It server .css files properly and it should serve images and .js file as well.
 * You need to have index.html file in your current directory, or specify path to directory with one. You can also point the .html file, 
 * that you want to serve.
 * 
 * Example usage: 
 *
 *  node simple_server // this assumes you have your index.html in current directory. If not see below
 *
 *  node simple_server html/main.html // you can point to other html files.
 *
 * If you want the server to run on port different that default one (8080), add PORT=PORT_# when running the app.
 *
 */


"use strict";

var express = require("express");
var fs = require("fs");
var PORT = process.env.PORT || 8080; 
var app = express();

var args = process.argv.slice(2);
var htmlFile = args[0];

var dirContents = [];
fs.readdirSync('./').forEach(file => {
	dirContents.push(file);
});
var hasIndexFile = (dirContents.indexOf("index.html") > -1);

if (!htmlFile == undefined){
	var pathToDir = htmlFile.split("/");
	var pathToDir = pathToDir[0];
}

app.use('/', express.static(__dirname + '/' + pathToDir));

if (htmlFile == undefined){
	if (hasIndexFile){
		htmlFile = 'index.html';
	}else {
		console.log("Couldn't find index.html. Aborting.");
		process.exit();
	}
}

app.get("/", function(req, res){
	res.sendFile(htmlFile, { root: __dirname });	
});


app.listen(PORT, function(err){
	if(err) throw err;
	console.log("Listening on PORT: ", PORT); 
});
