

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

function Send_Information(){
        var fullName= document.getElementById(person_name).value;
        alert("name: "+fullName);
        alert("hi")

}
var login = document.getElementById("Login");
var signin = document.getElementById("signin");



/** function myFunction() {
     if (name1.value.endsWith("@admin"))
{
        login.action="index4.html"
      }
    

    else{
           login.action="index.html"
    }


 
    
}**/



function myFunction_signUp() {
  var ID = document.getElementById("personal_Id").value;

 
  if ( (document.getElementById("password").value== document.getElementById("passwordR").value) && ID.endsWith("@admin")  )
{
  
  signin.action="index4.html"




   }
 

 else if (!(ID.endsWith("@admin"))&&!(document.getElementById("password").value== document.getElementById("passwordR").value)){
  signin.action="index3.html";
 alert("please put @admin in the end of your ID");
 alert("make sure that your password indentical");
        
 }
 else if (!(document.getElementById("password").value== document.getElementById("passwordR").value)){
  signin.action="index3.html";
  alert("make sure that your password indentical");
        
 }
 else {
  signin.action="index3.html";
  
  alert("please put @admin in the end of your ID");

 }



 
}

