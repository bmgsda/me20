// Funções para setar comportamentos a elementos (deve ser OnLoad)

document.getElementById("passwordInput").addEventListener("keyup", event => {
  if(event.key !== "Enter") return;
  document.getElementById("loginButton").click();
});

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

// Funções de controle do front-end chamados pelo html

function hideLoginFailedMessage(){
  let loginFailedContainer = document.getElementById("loginFailedContainer");
  loginFailedContainer.style.transition = "all 1s";
  loginFailedContainer.style.bottom = "-150px";
  changeCirclesColor("rgb(255,255,255,0.2)");
}

// Funções de comunicação com o back-end

async function requestLogin(){
  let responseLogin = await eel.tryLogin(parent.document.getElementById("racfInput").value,
                                         parent.document.getElementById("passwordInput").value)();
  if(responseLogin == "success"){
    hideLoginFailedMessage();
    changeCirclesColor("rgb(0,204,0,0.8)");
  }
  else{
    showLoginFailedMessage(responseLogin);
    changeCirclesColor("rgb(204,0,0,0.8)");
  }
}
