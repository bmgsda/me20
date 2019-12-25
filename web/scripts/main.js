// Funções de controle do front-end chamados pelo html

function clickSidebarButton(id){
  let button = document.getElementById(id);
  let activeButtonList = document.getElementsByClassName("sidebarButtonActive mb-4");
  if (activeButtonList.length == 1) activeButtonList[0].className = "sidebarButton mb-4";
  button.className = "sidebarButtonActive mb-4";
};

function redirContent(url){
  let iframe = document.getElementById('contentIframe');
  iframe.src = url;
}
