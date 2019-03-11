// server.on('error', (err) => {
//         console.error(`server error`);
//         server.close();
//     });
//     server.on('message', (msg, rinfo) => {
//     	console.log(message);
//     });
//     server.on('listening', () => {
//         const address = server.address();
//     });
//     server.bind(port);


	var socket = io.connect('http://localhost:4000');

	setInterval(function(){
		socket.emit('message',{
			message:"shoahdouh",
		});

		console.log("dagf");
	}, 10);
