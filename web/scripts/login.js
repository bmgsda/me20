// Funções de controle do front-end

document.getElementById("passwordInput").addEventListener("keyup", event => {
    if(event.key !== "Enter") return;
    document.getElementById("loginButton").click();
});

// Funções de comunicação com o back-end

async function requestLogin(){
  let responseLogin = await eel.tryLogin(parent.document.getElementById("racfInput").value,
                                               parent.document.getElementById("passwordInput").value)();
  if (responseLogin == "success")
    alert("Logado");
  else if (responseLogin == "Falha de conexão ao SQL")
    alert("Falha de conexão ao SQL");
  else if (responseLogin == "Sem cadastro na base")
    alert("Usuário não cadastrado");
}
