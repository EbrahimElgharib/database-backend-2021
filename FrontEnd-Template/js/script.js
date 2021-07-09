

function getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(pos) {
        //You have your locaton here
        console.log(pos)
        console.log("Latitude: " + pos.coords.latitude +"Longitude: " +pos.coords.longitude);
        document.getElementById('longitude').innerHTML =  "    موقعي بالنسبة لخط الطول::  "+pos.coords.longitude;
        document.getElementById('Latitude').innerHTML =  "  موقعي بالنسبة لخط العرض::     "+pos.coords.latitude;
        });
      } else {
        console.log("Geolocation is not supported by this browser.");
      }


      
    }






function myFunction() {
 

  var x, i;
  x = document.querySelectorAll(".change");
  for (i = 0; i < x.length; i++) {
    x[i].style.backgroundColor = "#fff";
    x[i].style.border = "2px solid #000";
    x[i].disabled = false;
  }

 


 
    
}


