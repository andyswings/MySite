var range1 = document.getElementById("range1");
var range2 = document.getElementById("range2");
var imgOne = document.getElementsByClassName("img1")[0];
var imgTwo = document.getElementsByClassName("img2")[0];

range1.addEventListener("change", function() {
    imgOne.style.opacity = this.value / this.max;
});

range2.addEventListener("change", function() {
    imgTwo.style.opacity = this.value / this.max;
});
