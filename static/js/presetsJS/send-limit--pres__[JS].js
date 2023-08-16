function checkInput() {
    var input_title = document.getElementById('myInputTitle');
    var input_body = document.getElementById('myTextBody')
    var button = document.getElementById('myButtonSubmit');

    if (input_title.value.length > 0 && input_body.value.length > 0) {
      button.disabled = false;
    } else {
      button.disabled = true;
    }
  }