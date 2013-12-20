(function(window, document, undefined) {

  // Information for the HTTP request
  var DOGE_URL = '/dogify/';
  var STATUS_OK = 200;
  var REQUEST_DONE = 4;

  // DOM elements for basic text user input 
  var main = document.getElementById('main');
  var dogifyButton = document.getElementById('dogify');
  var saveButton = document.getElementById('save');
  var toDogify = document.getElementById('user-input');
  toDogify.placeholder = "Hit \"Dogify\" to generate \
an image. Click \"Open Image\" to open the image in a \
new tab to save. Don't doge anything too short or \
too long. ";
  toDogify.style.height = 'auto';
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
    generateImage();
  });

  function generateImage() {
    var request = new XMLHttpRequest();
    var input = toDogify.value;
    if (input === "") {
      input = toDogify.placeholder;
    }
    var URIinput = encodeURIComponent(input);
    request.open('GET', DOGE_URL + URIinput);
    request.send();
    request.addEventListener('readystatechange', function(event) {
      if (this.readyState === REQUEST_DONE) {
        if (this.status === STATUS_OK) {
          $('.error')[0].innerHTML = "";
          var response = this.responseText;
          phrases = JSON.parse(response);
          addPhrasesToImage(phrases);
        } else {
          $('.error')[0].innerText = "Dogerror! Your text was \
              probably too long or too short. :( Try again!";
        }
      }
    });
  }

  window.onload = function() {
    imageCanvas.width = dogeImage.width;
    imageCanvas.height = dogeImage.height;
    imageCtx = imageCanvas.getContext('2d');
    imageCtx.drawImage(dogeImage, 0, 0, dogeImage.width, dogeImage.height);
    // This would be nice so that the div is the same size as the image
    // and you don't have awkward space to the right of the image
    // But I'm not good enough at css to make it look pretty. -- Jenny
    main.style.width = dogeImage.width + 120 + 'px';
    generateImage();
  }

  function addPhrasesToImage(phrases) {
    imageCtx.drawImage(dogeImage, 0, 0, dogeImage.width, dogeImage.height);
    var red = [];
    var green = [];
    var blue = [];
    var x = [];
    var y = [];
    var xmax = [];
    var fontsize = [];
    for (var i = 0; i < phrases.length; i++) {
      red[i] = Math.floor(Math.random() * (255 - 50 + 1)) + 50;
      green[i] = Math.floor(Math.random() * (255 - 50 + 1)) + 50;
      blue[i] = Math.floor(Math.random() * (255 - 50 + 1)) + 50;
      y[i] = Math.floor(Math.random() * (dogeImage.height - 40 + 1)) + 40;
      fontsize[i] = (Math.random() * 20) + 20;
      xmax[i] = dogeImage.width - phrases[i].length * fontsize[i];
      x[i] = Math.floor(Math.random() * (xmax[i] - 20 + 1)) + 20;
    }
    for (var i = 0;i < phrases.length; i++) { 
      imageCtx.fillStyle = "rgb(" + red[i] + ", " + green[i] + ", " + blue[i] + ")";
      imageCtx.font = "bold " + fontsize[i] + "px 'Comic Sans MS'";
      imageCtx.fillText(phrases[i], x[i], y[i]);
    }
  }

  saveButton.addEventListener('click', function(event) {
    window.open(imageCanvas.toDataURL('image/jpeg'));
  });



})(this, this.document);