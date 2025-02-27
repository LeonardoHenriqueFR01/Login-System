# Login-System

Um sistema de login simples desenvolvido com **HTML, CSS, JavaScript, Python/Flask e SQLite**. 
Os usuários poderão se cadastrar inserindo **nome, e-mail e senha**, e posteriormente fazer login utilizando **e-mail e senha**.

## Tecnologias Utilizadas

- **Front-end:** HTML, CSS, JavaScript
- **Back-end:** Flask (Python)
- **Banco de Dados:** SQLite

## Requisitos

Antes de executar o projeto, certifique-se de ter o Python instalado. Todas as bibliotecas necessárias estão listadas no arquivo `requirements.txt`.

### Instalando as Dependências

Execute o seguinte comando no terminal para instalar as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

## Executando o Projeto

Após instalar as dependências, execute o seguinte comando para iniciar o servidor Flask:

```bash
python main.py
```

O servidor será iniciado e você poderá acessar o sistema pelo navegador no endereço:

```
http://127.0.0.1:5000
```

## Estrutura do Projeto

```
Login-System/
|── app/
│──│── static/         # Arquivos CSS e JS
│──│── templates/      # Páginas HTML
│──│── models.py       # Configurações do banco de dados
│──│── routes.py       # Configurações de rotas da aplicação
│──│── database.db     # Banco de dados SQLite
│──│── __init__.py     # Configurações iníciais da aplicação
│── main.py            # Aplicação Flask
│── requirements.txt   # Dependências do projeto
│── README.md          # Documentação
│── venv/              # Maquina virtual
```

## Funcionalidades

- **Cadastro de Usuário:** Nome, e-mail e senha.
- **Login de Usuário:** Utilizando e-mail e senha.
- **Armazenamento Seguro:** Senhas serão armazenadas de forma segura no banco de dados.

## Contribuição

Sinta-se à vontade para contribuir com melhorias no projeto. Para isso:

1. Faça um fork do repositório
2. Crie uma nova branch: `git checkout -b minha-feature`
3. Faça suas alterações e commit: `git commit -m 'Minha nova funcionalidade'`
4. Envie as alterações: `git push origin minha-feature`
5. Abra um Pull Request

## Licença

Este projeto é de código aberto e pode ser utilizado livremente.
