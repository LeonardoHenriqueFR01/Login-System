// Função para o spin form cadastro
function get_submit_cadastro() {
    // Pegando os "id" nessesários
    let btn_submit_cadastro = document.getElementById('btn_submit_cadastro');
    let box_load_cadastro = document.getElementById('box_load_cadastro');

    let name = document.getElementById('name').value.trim();
    let email = document.getElementById('email').value.trim();
    let password = document.getElementById('password').value.trim();

    // Validação dos campos
    if (name.length < 3) {
        alert("O nome precisa ter no mínimo 3 caracteres!")
        return;
    }

    if (email.length < 12) {
        alert("O email precisa ter no mínimo 12 caracteres!")
        return;
    }

    if (password.length < 8) {
        alert("A senha precisa ter no mínimo 8 caracteres!")
        return;
    }

    // Se tudo estiver correto, exibe o spin e esconde o botão
    btn_submit_cadastro.style.display = "none";    
    box_load_cadastro.style.display = "flex";

}

// Função para o spin form login
function get_submit_login() {
    // Pegando os "id" nessesários
    let btn_submit_login = document.getElementById('btn_submit_login');
    let box_load_login = document.getElementById('box_load_login');

    let name = document.getElementById('name_login').value.trim();
    let email = document.getElementById('email_login').value.trim();
    let password = document.getElementById('password_login').value.trim();

    // Validação dos campos
    if (name.length < 3) {
        alert("O nome precisa ter no mínimo 3 caracteres!")
        return;
    }

    if (email.length < 12) {
        alert("O email precisa ter no mínimo 12 caracteres!")
        return;
    }

    if (password.length < 8) {
        alert("A senha precisa ter no mínimo 8 caracteres!")
        return;
    }

    // Se tudo estiver correto, exibe o spin e esconde o botão
    btn_submit_login.style.display = "none";
    box_load_login.style.display = "flex";

}


function toggleForms() {
    // Seleciona o container principal e alterna a classe "active"
    document.getElementById('content').classList.toggle('active');
}
