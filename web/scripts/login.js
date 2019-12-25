// Funções para setar comportamentos a elementos (deve ser OnLoad)

window.onload = function(){
  document.getElementById("racfInput").focus();
  document.getElementById("passwordInput").addEventListener("keyup", event => {
    if(event.key !== "Enter") return;
    document.getElementById("loginButton").click();
  });
}

// Funções de controle do front-end

function changeCirclesColor(rgb){
  let circlesList = document.querySelectorAll(".circles li");
  circlesList = Array.from(circlesList)
  circlesList.forEach(function(circle){
    circle.style.transition = "all 1.5s";
    circle.style.background = rgb;
  });
};

function showLoginFailedMessage(message){
  let loginFailedContainer = document.getElementById("loginFailedContainer");
  loginFailedContainer.style.transition = "all 1s";
  loginFailedContainer.innerHTML = loginFailedContainer.innerHTML.replace(/<center>(.*)</, "<center>" + message + "<");
  loginFailedContainer.style.bottom = "0";
}

function toggleLoginButtonSpinner(){
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

// Funções de controle do front-end chamados pelo html

function hideLoginFailedMessage(){
  let loginFailedContainer = document.getElementById("loginFailedContainer");
  loginFailedContainer.style.transition = "all 1s";
  loginFailedContainer.style.bottom = "-150px";
  changeCirclesColor("rgb(255,255,255,0.2)");
}

// Funções de comunicação com o back-end chamados pelo html

async function requestLogin(){
  toggleLoginButtonSpinner()
  let responseLogin = await eel.tryLogin(document.getElementById("racfInput").value,
                                         document.getElementById("passwordInput").value)();
  if(responseLogin == "success"){
    hideLoginFailedMessage();
    changeCirclesColor("rgb(0,204,0,0.8)");
    setTimeout(() => window.location.href = "main.html", 1000);
    setTimeout(() => toggleLoginButtonSpinner(), 1100);
  }

  else{
    showLoginFailedMessage(responseLogin);
    changeCirclesColor("rgb(204,0,0,0.8)");
    setTimeout(() => toggleLoginButtonSpinner(), 500);
  }
}
