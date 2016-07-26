// HTTP Server Setup
var express = require('express');
var app = express();
var port = process.env.PORT || 4567;
var exec = require('child_process').exec;
var cmd = 'cd /var/www/html && git reset --hard HEAD && git pull origin master';

// Start the http server
app.listen(port);
console.log('Server started! At http://localhost:' + port);

app.post('/payload', function(req, res) {
	console.log("Received git commit");
	exec(cmd, function(error, stdout, stderr) { });
    res.writeHead(200, {'Content-Type': 'application/json'});
    res.end();
});