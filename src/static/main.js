console.log("Hi from main.js !")

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
  const buttons = document.getElementsByClassName('button-shop');
  const buttonsLink = document.getElementsByClassName('product-link');
  var divProducts = document.getElementsByClassName('one-product');

  for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
      console.log('Button clicked!');
       console.log(this.value);
        sendPost("http://"+window.location.host+"/", "shop_pk", this.value)
        setTimeout(function() {
              location.reload();
            }, 100);

    });
  }


    for (var i = 0; i < buttonsLink.length; i++) {
    buttonsLink[i].addEventListener('click', function() {
      console.log('Button clicked!');
       console.log(this.value);
        sendPost("http://"+window.location.host+"/", "product_pk", this.value)
        setTimeout(function() {
              location.reload();
            }, 100);

    });
  }


});


