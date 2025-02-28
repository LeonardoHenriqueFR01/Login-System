// Função para o spin
function get_submit() {
    // Pegando os "id" nessesários
    let btn_submit_cadastro = document.getElementById('btn_submit_cadastro');
    let btn_submit_login = document.getElementById('btn_submit_login');

    let box_load_cadastro = document.getElementById('box_load_cadastro');
    let box_load_login = document.getElementById('box_load_login');

    let name = document.getElementById('name').value.trim();
    let email = document.getElementById('email').value.trim();
    let password = document.getElementById('password').value.trim();

    // Validação dos campos
    if (name.length < 3) {
        return;
    }

    if (email.length < 12) {
        return;
    }

    if (password.length < 8) {
        return;
    }

    // Se tudo estiver correto, exibe o spin e esconde o botão
    btn_submit_cadastro.style.display = "none";
    btn_submit_login.style.display = "none";
    
    box_load_cadastro.style.display = "flex";
    box_load_login.style.display = "flex";

}

function toggleForms() {
    // Seleciona o container principal e alterna a classe "active"
    document.getElementById('content').classList.toggle('active');
}