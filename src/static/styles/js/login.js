window.generateUserID = function(){
  
  var text = btoa(String.fromCharCode.apply(null, window.crypto.getRandomValues((new Uint8Array(32)))));
  
  document.getElementById('userid').value=text
}