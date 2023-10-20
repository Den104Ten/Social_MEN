const buttonLogin = document.getElementById('button-login');
const userPassword = document.getElementById('myInputPassword');
const userName = document.getElementById('myInputUsername');
console.log(buttonLogin);
buttonLogin.addEventListener('click', function () {
  if (userPassword.value == 0) {
    userPassword.classList.add('error');
    userPassword.placeholder = 'Обязательно к выполнению!';
  }
  if (userName.value == 0) {
    userName.classList.add('error');
    userName.placeholder = 'Обязательно к выполнению!';
  }
});