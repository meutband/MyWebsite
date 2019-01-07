var popup1 = document.getElementById('popup1');
var popup2 = document.getElementById('popup2');
var popup3 = document.getElementById('popup3');

var btn1 = document.getElementById("popup-btn1");
var btn2 = document.getElementById("popup-btn2");
var btn3 = document.getElementById("popup-btn3");

var span1 = document.getElementsByClassName("close1")[0];
var span2 = document.getElementsByClassName("close2")[0];
var span3 = document.getElementsByClassName("close3")[0];

btn1.onclick = function() {
    popup1.style.display = "block";
    console.log("Button1")
}
btn2.onclick = function() {
    popup2.style.display = "block";
}
btn3.onclick = function() {
    popup3.style.display = "block";
}


span1.onclick = function() {
    popup1.style.display = "none";
}
span2.onclick = function() {
    popup2.style.display = "none";
}
span3.onclick = function() {
    popup3.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == popup1) {
        popup1.style.display = "none";
    }
    if (event.target == popup2) {
        popup2.style.display = "none";
    }
    if (event.target == popup3) {
        popup3.style.display = "none";
    }
}
