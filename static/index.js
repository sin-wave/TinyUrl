const typedTextSpan = document.querySelector(".typed-text");
const cursorSpan = document.querySelector(".cursor");
const url = document.getElementById("url");
const clip = document.getElementById("clip");
const foo = document.getElementById("foo");
clip.style.display="none";
const textArray = [
  "Welcomes You",
  "Short URL",
  "Have 😜",
  "Made with ❤️ in India",
];
const typingDelay = 200;
const erasingDelay = 100;
const newTextDelay = 2000; // Delay between current and next text
let textArrayIndex = 0;
let charIndex = 0;

function type() {
  if (charIndex < textArray[textArrayIndex].length) {
    if (!cursorSpan.classList.contains("typing"))
      cursorSpan.classList.add("typing");
    typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
    charIndex++;
    setTimeout(type, typingDelay);
  } else {
    cursorSpan.classList.remove("typing");
    setTimeout(erase, newTextDelay);
  }
}

function erase() {
  if (charIndex > 0) {
    if (!cursorSpan.classList.contains("typing"))
      cursorSpan.classList.add("typing");
    typedTextSpan.textContent = textArray[textArrayIndex].substring(
      0,
      charIndex - 1
    );
    charIndex--;
    setTimeout(erase, erasingDelay);
  } else {
    cursorSpan.classList.remove("typing");
    textArrayIndex++;
    if (textArrayIndex >= textArray.length) textArrayIndex = 0;
    setTimeout(type, typingDelay + 1100);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  // On DOM Load initiate the effect
  if (textArray.length) setTimeout(type, newTextDelay + 250);
});
function validURL(string) {
    let url;
    
    try {
      url = new URL(string);
    } catch (_) {
      return false;  
    }
  
    return url.protocol === "http:" || url.protocol === "https:";
  }
function fun1(){
    let given_url = url.value;
    let isUrl = validURL(given_url);
    if(isUrl){
        var req = new XMLHttpRequest();
        req.onreadystatechange = function()
        {
          if(this.readyState == 4 && this.status == 200) {
            clip.style.display="block";
            foo.value=JSON.parse(this.responseText)["short_url"];
          }
        }

        req.open('POST', '/', true);
        req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
        req.send("url=" + given_url);
    }
    else{
        alert("Please provid a valid url adress!!!");
    }
}

$(function() {
    new Clipboard('#test');
});
