console.log("Hi from main TWOO !")

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}




function sendPost(url, key, value) {
        const csrfToken = getCookie('csrftoken');

        fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
          },
          body: JSON.stringify({
            [key]: value,
          })
        })
          .then(response => response)
          .then(data => {
            console.log(data);
          })
          .catch(error => {
            console.error('Error:', error);
          });
    }



document.addEventListener('DOMContentLoaded', function() {
  const buttons = document.getElementsByClassName('delete-button');


    console.log(buttons)

  for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
      console.log('Button Delete clicked!');
       console.log(this.value);
        sendPost("http://"+window.location.host+"/card", "delete", this.value)
        setTimeout(function() {
              location.reload();
            }, 100);

    });
  }

});

  const payButton = document.getElementById('button-pay');

payButton.addEventListener('click', function() {
                sendPost("http://"+window.location.host+"/card", "pay", this.value);
                        setTimeout(function() {
                                  location.reload();
                                }, 200);
        })