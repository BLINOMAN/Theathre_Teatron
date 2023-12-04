let sect = document.querySelector(".section");
let btn = document.querySelector(".btn");
btn.addEventListener("click", function(){
  sect.scrollIntoView({behavior: "smooth"});
});