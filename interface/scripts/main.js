// Onload da página main.html
document.body.onload = async function(){
  let windowsUserInfo = await requestWindowsUserInfo();
  document.getElementById("userName").innerHTML = windowsUserInfo["name"];
  document.getElementById("userRacf").innerHTML = windowsUserInfo["racf"];
}

// Destacar o botão clicado na sidebar
function clickSidebarButton(id){
  let button = document.getElementById(id);
  let activeButtonList = document.getElementsByClassName("sidebarButtonActive mb-4");
  if (activeButtonList.length == 1) activeButtonList[0].className = "sidebarButton mb-4";
  button.className = "sidebarButtonActive mb-4";
};

// Redirecionar a página no iframe
async function redirContent(url){
  await (window.frames["contentIframe"].location = url)();
  window.frames["contentIframe"].location.reload(true);
}
