var socket = io.connect('http://localhost:4000');
      var submit = document.getElementById("submit");
      var submit2 = document.getElementById("fname");
      
      submit.addEventListener("click", function(){
        console.log("hello");
         socket.on('chat', function(data1){
          console.log(data1);
            });
      });

         // Creating map options
         var mapOptions = {
            center: [12.82122, 80.03829],
            zoom: 10
         }
         
         // Creating a map object
         var map = new L.map('map', mapOptions);
         
         // Creating a Layer object
         var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
         var marker = new L.Marker([12.82122, 80.03829]);
         //var marker = new L.Marker(track);
         
         marker.addTo(map);

         marker.bindPopup('tatti').openPopup();
         marker.addTo(map); 
         
         // Adding layer to the map
         map.addLayer(layer);