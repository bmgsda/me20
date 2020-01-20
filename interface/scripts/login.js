// Onload da página login.html
window.onload = async function(){
  let windowsUserInfo = await requestWindowsUserInfo();
  let racf = windowsUserInfo['racf'];
  document.getElementById("racfInput").value = racf;
}

// Reação à resposta da requisição de Login
function Login_requestLoginReaction(responseLogin){
  if(responseLogin == "success"){
    Login_hideLoginFailedMessage();
    Login_changeCirclesColor("rgb(0,204,0,0.8)");
    setTimeout(() => window.location.href = "main.html", 1000);
    setTimeout(() => Login_toggleLoginButtonSpinner(), 1100);
  }
  else{
    Login_showLoginFailedMessage(responseLogin);
    Login_changeCirclesColor("rgb(204,0,0,0.8)");
    setTimeout(() => Login_toggleLoginButtonSpinner(), 500);
  }
}

// Muda a cor dos circulos do background
function Login_changeCirclesColor(rgb){
  let circlesList = document.querySelectorAll(".circles li");
  circlesList = Array.from(circlesList);
  circlesList.forEach(function(circle){
    circle.style.transition = "all 1.5s";
    circle.style.background = rgb;
  });
};

// Exibe caixa de erro inferior com mensagem
function Login_showLoginFailedMessage(message){
  let loginFailedContainer = document.getElementById("loginFailedContainer");
  loginFailedContainer.style.transition = "all 1s";
  loginFailedContainer.innerHTML = loginFailedContainer.innerHTML.replace(/<center>(.*)</, "<center>" + message + "<");
  loginFailedContainer.style.bottom = "0";
}

// Esconde a caixa de erro inferior
function Login_hideLoginFailedMessage(){
  let loginFailedContainer = document.getElementById("loginFailedContainer");
  loginFailedContainer.style.transition = "all 1s";
  loginFailedContainer.style.bottom = "-150px";
  Login_changeCirclesColor("rgb(255,255,255,0.2)");
}

// Troca o botão do login com o spinner e vice-verse
function Login_toggleLoginButtonSpinner(){
  let loginButton = document.getElementById("loginButton");
  let loginSpinner = document.getElementById("loginSpinner");
  if(loginButton.style.display == "none"){
    loginButton.style.display = "initial";
    loginSpinner.style.display = "none";
  }
  else{
    loginButton.style.display = "none";
    loginSpinner.style.display = "inline-block";
  }
}
