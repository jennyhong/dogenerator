// function(window, document, undefined) {

  var DOGE_URL = '/generate_text/';
  var STATUS_OK = 200;
  var REQUEST_DONE = 4;

  var dogifyButton = document.getElementById('dogify');
  var toDogify = document.getElementById('user-input');
  var outputSpace = document.getElementById('result');

  dogifyButton.addEventListener('click', function(event) {
    event.preventDefault();
    var request = new XMLHttpRequest();
    var URIinput = encodeURIComponent(toDogify.value);
    request.open('GET', DOGE_URL + URIinput);
    request.send();
    request.addEventListener('readystatechange', function(event) {
      if (this.readyState === REQUEST_DONE) {
        if (this.status === STATUS_OK) {
          var response = this.responseText;
          outputSpace.innerHTML = response;
        } else {
          // $('.error')[0].innerHTML = this.responseText;
        }
      }
    });
  });

// })(this, this.document);
