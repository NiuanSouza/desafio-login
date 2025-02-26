# Django Login and Register System

Este projeto é um sistema de autenticação desenvolvido com o Framework Django, permitindo que usuários realizem login e cadastro em um banco de dados SQLite3 usando as funções de autenticação padrão do Django.

## Funcionalidades

### 📌 Tela de Login
- Autenticação via e-mail e senha.
- Validação dos campos (e-mail e senha não podem estar vazios).
- Tratamento de erros:
  - E-mail errado, mas existente no banco: **"E-mail inválido"**.
  - Senha errada, mas existente no banco: **"Senha inválida"**.
  - E-mail não cadastrado: **"E-mail inexistente"**.
  - Senha não cadastrada: **"Senha inexistente"**.
- Redirecionamento para a tela de registro ao clicar em **"Registre-se"**.
- Após login bem-sucedido, o usuário é direcionado para a tela **"Menu"**.

### 📌 Tela de Registro
- Formulário com os campos: **Nome, E-mail, Senha e Confirmar Senha**.
- Validações:
  - **Nome:** Aceita apenas letras.
  - **E-mail:** Deve conter um formato válido com "@".
  - **Senha:** Mínimo de 8 caracteres, 1 número, 1 caractere especial e 1 letra maiúscula.
  - **Confirmação de senha:** Deve ser idêntica à senha inserida.
- Opção para visualizar ou ocultar os caracteres da senha.
- **Botões:**
  - **Registrar:** Salva os dados no banco.
  - **Cancelar:** Retorna para a tela de login.

### ✨ Extras
- Envio de um e-mail confirmando o cadastro.
- **Navbar** com:
  - **Logo**:
    - **Autenticado:** Redireciona para o **Menu**.
    - **Não autenticado:** Redireciona para o **Index**.
  - **Botões variáveis conforme autenticação:**
    - **Não Logado:** Botões "Login" e "Registro" disponíveis levando a essas telas.
    - **Logado:** Botão "Perfil" e "Sair".
      - **Perfil:** Exibe o nome do usuário e e-mail.
      - **Sair:** Faz logout do sistema.
- Tela inicial **Index** com botão para acesso ao Admin nativo do Django.

## 🛠 Tecnologias Utilizadas
- **Django** - Framework principal
- **SQLite3** - Banco de dados
- **Python** - Linguagem principal
- **HTML/CSS/BootStrap** - Estruturação e estilização das telas

## 🛠 Pré-Requisitos
- Python intalador
- Prompt de comando
- Git instalado, opicional caso queira utilizar o "git clone", se não é possivel só baixar o reposítório.

## 🚀 Instalação e Execução

### 1️⃣ Clone este repositório ou baixe esse repositório.
```sh
git clone https://github.com/NiuanSouza/desafio-login.git

cd desafio-login

cd "Django Login and Register System"
```

### 2️⃣ Crie e ative um ambiente virtual
```sh
python -m venv venv
```
**No Windows:**
```sh
venv\Scripts\activate
```
**No macOS/Linux:**
```sh
source venv/bin/activate
```

### 3️⃣ Instale as dependências
```sh
pip install -r requirements.txt
```

### 4️⃣ Aplique as migrações do banco de dados
```sh
python manage.py migrate
```

### 5️⃣ Configure o envio de e-mails
No arquivo **settings.py** dentro da pasta `setup`, configure as credenciais do e-mail para envio de confirmação de cadastro:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.com'  # Servidor SMTP
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seuemail@mail.com'  # Endereço do Email
EMAIL_HOST_PASSWORD = 'suasenha'  # Senha do Email ou senha de aplicativo
```

No arquivo **views.py** dentro da pasta `users`, adicione o e-mail usado:

```python
    # Envia um email de boas-vindas
    subject = 'Bem-vindo ao nosso site!'
    message = f'Olá {username},\n\nVocê foi registrado no desafio técnico da Fidelity!!'
    from_email = 'seuemail@mail.com'  # Este deve ser o mesmo email configurado no settings.py
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
```

### 6️⃣ Execute o servidor Django
```sh
python manage.py runserver
```

Agora acesse `http://127.0.0.1:8000/` no seu navegador para usar o sistema! 🚀


