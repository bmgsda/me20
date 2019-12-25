// Funções onload
document.body.onload = async function(){
  let responseUserInfo = await eel.getSessionUserInfo()();
  document.getElementById("userName").innerHTML = responseUserInfo["userName"];
  document.getElementById("userRacf").innerHTML = responseUserInfo["userRacf"];
}

// Funções de controle do front-end chamados pelo html

function clickSidebarButton(id){
  let button = document.getElementById(id);
  let activeButtonList = document.getElementsByClassName("sidebarButtonActive mb-4");
  if (activeButtonList.length == 1) activeButtonList[0].className = "sidebarButton mb-4";
  button.className = "sidebarButtonActive mb-4";
};

async function redirContent(url){
  await (window.frames["contentIframe"].location = url)();
  window.frames["contentIframe"].location.reload(true);
}
