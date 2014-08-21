var http = require('http');
var server = http.createServer().listen(3000);
var io = require('socket.io').listen(server);
var querystring = require('querystring');

io.on('connection', function(socket){
	socket.on('preguntando' , function(data){
		var values = querystring.stringify(data);
		options = {
			hostname : 'localhost',
			port : 8000,
			path : '/crear',
			method : 'POST',
			headers : {
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': values.length
			}
		}

		var req = http.request(options, function(res){
			res.setEncoding('utf8');
			res.on('data', function(data){
				io.emit('devolviendo pregunta', data);
			});
		});

		req.write(values);
		req.end();
	});
});