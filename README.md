# Django Login and Register System

Este projeto é um sistema de autenticação desenvolvido com o Framework Django, permitindo que usuários realizem login e cadastro em um banco de dados SQLite3 usando as funções de autenticação padrão do Django.

## Funcionalidades

##📌 Tela de Login
Autenticação via e-mail e senha.
Validação dos campos (e-mail e senha não podem estar vazios).
Tratamento de erros:
E-mail errado, mas existente no banco: "E-mail inválido".
Senha errada, mas existente no banco: "Senha inválida".
E-mail não cadastrado: "E-mail inexistente".
Senha não cadastrada: "Senha inexistente".
Redirecionamento para a tela de registro ao clicar em "Registre-se".
Após login bem-sucedido, o usuário é direcionado para a tela "Menu".

##📌 Tela de Registro
Formulário com os campos: Nome, E-mail, Senha e Confirmar Senha.
Validações:
Nome: Aceita apenas letras.
E-mail: Deve conter um formato válido com "@"
Senha: Mínimo de 8 caracteres, 1 número, 1 caractere especial e 1 letra maiúscula.
Confirmação de senha: Deve ser idêntica à senha inserida.
Opção para visualizar ou ocultar os caracteres da senha.
Botões:
Registrar: Salva os dados no banco.
Cancelar: Retorna para a tela de login.

##✨ Extras
Envio de um e-mail confirmando o cadastro.
Navbar com Logo indicando "Index", e dois botões que variam dependendo se o usuaria está logado ou não.
Não Logado: Botões "Login" e "Registro" disponiveis levando a essas telas.
Logado: Botão "Perfil" e "Sair", com o primeiro levando a uma tela que mostra nome do usuario e email, enquanto no botão sair fazerá Logout no sistema.
Tela inicial Index com botão para acesso ao Admin nativo do Django. 

##🛠 Tecnologias Utilizadas
Django - Framework principal
SQLite3 - Banco de dados
Python - Linguagem principal
HTML/CSS - Estruturação e estilização das telas

## 🚀 Instalação e Execução

### 1️⃣ Clone este repositório ou baixe esse reposítório.

### 2️⃣ Crie e ative um ambiente virtual
python -m venv venv
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

###3️⃣ Instale as dependências
pip install -r requirements.txt

###4️⃣ Aplique as migrações do banco de dados
python manage.py migrate

###5️⃣ Coloque o Email para envio de confirmação de cadastro
No arquivo settings.py da pasta 'setup', você encontrará o código a seguir:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

Preencha os campos 'EMAIL_HOST', 'EMAIL_HOST_USER' e 'EMAIL_HOST_PASSWORD' de acordo com o email utilizado, sua senha de aplicativo e o servidor SMTP do email, de acordo com o exemplo abaixo utilizando Gmail:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Servidor SMTP do Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seuemail@gmail.com'  # Endereço do Gmail
EMAIL_HOST_PASSWORD = 'suasenha'  # Senha do Gmail ou senha de aplicativo

###6️⃣ Execute o servidor Django
python manage.py runserver








