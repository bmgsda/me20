document.getElementById("passwordInput").addEventListener("keyup", event => {
    if(event.key !== "Enter") return;
    document.getElementById("loginButton").click();
});
