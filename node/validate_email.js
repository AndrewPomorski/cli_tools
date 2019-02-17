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
 * You're going to need express for that script: 
 *
 *  npm install --save express
 *
 * Or add it to your package.json:
 *
 * "express" : "*"
 *  
 * 
 * This server (more or less) validates email addresses. Make a GET http request to localohost on port 8080,
 * or other port if PORT env variable is set.
 *
 * example request: 
 * 	localhost:8080/email/john@doe.com
 *
 * example response (Invalid): 
 *	{
 *	  "email": "john@doe.com",
 *	  "message": "[-] This email address appears to be invalid.",
 *	  "valid": false
 *	}
 * example response (Valid): 
 *
 *	{
 *	  "email": "johndoe@gmail.com",
 *	  "message": "[+] This email address is (probably) valid.",
 *	  "valid": true
 *	}
 *
 *
 *
 *	If you wish to add or remove any domain names simply eddit domains.json file. 
 *	List of emails, courtesy of mailcheck : https://github.com/mailcheck/mailcheck/
 */

"use strict";

var express = require("express");
var app = express();
var PORT = process.env.PORT || 8080;
var fs = require("fs");

app.set("json spaces", 4);


var input = fs.readFileSync("domains.json");
var config = JSON.parse(input);
var domains = config.domains;


var verifyEmail = function(email){
	var email = email.split("@");
	var domain_name = email[1];
	var contains = (domains.indexOf(domain_name) > -1);
	return contains;
}





app.get("/", function(req, res){
	res.send("Use /email/your_email_address to verify the address");
});


app.get("/email/:mail_addr", function(req, res){
	var valid_email = verifyEmail(req.params.mail_addr);
	if (valid_email) {
		res.json({ email: req.params.mail_addr, message:"[+] This email address is (probably) valid.", valid: true });
	} else {
		res.json({ email: req.params.mail_addr, message:"[-] This email address appears to be invalid.", valid: false });
	}
});


app.listen(PORT, function(err){
	if (err) {
		throw err;
	}
	console.log("Server listening on port " + PORT);
});
