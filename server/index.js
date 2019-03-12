var server = require('ws').Server;
var s = new server({port: 5001});
var s1 = new server({port: 5002});
var marker = require('../static/app.js');


s.on('connection',function(ws){
	 ws.on('message',function(message){
	 	console.log("RFID : " + message);

		// s.clients.forEach(function e(client){
		// 	if(client==ws)
		// 		client.send(message);
		// });
		//ws.send(JSON.stringify(obj));
	 });
});

s1.on('connection',function(ws){
	 ws.on('message',function(message){
	 console.log("RFID and Location : " +  message);
	 var dat = message.split(",");
	 marker.marker_position(null,null);
	 marker.marker_position(dat[0],dat[1]);

});
});
