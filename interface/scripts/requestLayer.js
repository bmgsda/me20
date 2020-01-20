// Requisição de login
async function requestLogin(){
  Login_toggleLoginButtonSpinner();
  let responseLogin = await eel.requestLogin(document.getElementById("racfInput").value)();
  Login_requestLoginReaction(responseLogin);
}

// Requisição de informações do usuário do Windows
async function requestWindowsUserInfo(){
  let responseWindowsUserInfo = await eel.requestWindowsUserInfo()();
  return responseWindowsUserInfo;
}
