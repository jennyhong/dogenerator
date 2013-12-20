(function(window, document, undefined) {

  // Information for the HTTP request
  var DOGE_URL = '/dogify/';
  var STATUS_OK = 200;
  var REQUEST_DONE = 4;

  // DOM elements for basic text user input 
  var dogifyButton = document.getElementById('dogify');
  var toDogify = document.getElementById('user-input');
  var outputSpace = document.getElementById('result');
  
  // image
  var dogeImage = new Image();
  dogeImage.src = 'static/images/doge.jpg';

  // DOM elements for generating the doge image
  var imageCanvas = document.getElementById('image-canvas');
  var imageCtx;

  // Initializes the array phrases upon clicking dogifyButton
  var phrases;
  dogifyButton.addEventListener('click', function(event) {
    event.preventDefault();
    var request = new XMLHttpRequest();
    var URIinput = encodeURIComponent(toDogify.value);
    request.open('GET', DOGE_URL + URIinput);
    request.send();
    request.addEventListener('readystatechange', function(event) {
      if (this.readyState === REQUEST_DONE) {
        if (this.status === STATUS_OK) {
          $('.error')[0].innerHTML = "";
          var response = this.responseText;
          phrases = JSON.parse(response);
          makeWords(phrases);
        } else {
          $('.error')[0].innerText = "Uh oh! There was an error dogifying your text. Try another phrase. :(";
        }
      }
    });
  });

  window.onload = function() {
    imageCanvas.width = dogeImage.width;
    imageCanvas.height = dogeImage.height;
    imageCtx = imageCanvas.getContext('2d');
    imageCtx.drawImage(dogeImage, 0, 0, dogeImage.width, dogeImage.height);
  }

  function makeWords(phrases) {
    imageCtx.drawImage(dogeImage, 0, 0, dogeImage.width, dogeImage.height);
    var red = [];
    var green = [];
    var blue = [];
    var x = [];
    var y = [];
    var xmax = [];
    for (var i = 0; i < phrases.length; i++) {
      red[i] = Math.floor(Math.random() * (255 - 50 + 1)) + 50;
      green[i] = Math.floor(Math.random() * (255 - 50 + 1)) + 50;
      blue[i] = Math.floor(Math.random() * (255 - 50 + 1)) + 50;
      y[i] = Math.floor(Math.random() * (dogeImage.height - 20 + 1)) + 20;
      xmax[i] = dogeImage.width - phrases[i].length * 14;
      x[i] = Math.floor(Math.random() * (xmax[i] - 0 + 1)) + 0;
    }
    for (var i = 0;i < phrases.length; i++) { 
      imageCtx.fillStyle = "rgb(" + red[i] + ", " + green[i] + ", " + blue[i] + ")";
      imageCtx.font = "bold 24px 'Comic Sans MS'";
      imageCtx.fillText(phrases[i], x[i], y[i]);
    }
  }

})(this, this.document);