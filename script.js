function checkPassword() {
      var password = document.getElementById("passwordBox");
      var passwordText = password.value;
      if (passwordText == "aaa") {
        window.location.href = '/chat';
      }
      else if (passwordText == "bbb") {
        window.location.href = '/secret';
      }
      else
      alert("Access Denied! Incorrect Password");
      return false;
    }
