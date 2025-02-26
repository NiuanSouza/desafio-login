from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('senha')

        # Verificando se o e-mail já está registrado
        email_verification = User.objects.filter(email=email).first()

        if email_verification:
            messages.warning(request, 'Já existe um usuário com esse e-mail cadastrado.')
            return redirect('register')  # redireciona para a página de registro

        # Cria e salva o usuário
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Envia um email de boas-vindas
        subject = 'Bem-vindo ao nosso site!'
        message = f'Olá {username},\n\nVocê foi registrado no desafio técnico da Fidelity!!'
        from_email = 'seuemail@mail.com'  # Este deve ser o mesmo email configurado no settings.py
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        messages.success(request, f'Conta criada com sucesso para {username}!')
        return redirect('index')
    return render(request, 'users/register.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        # Verifica se os campos estão preenchidos
        if not email:
            messages.warning(request, "E-mail inexistente")
            return render(request, 'users/login.html', {'email': email})
        if not password:
            messages.warning(request, "Senha inexistente")
            return render(request, 'users/login.html', {'email': email})
        
        # Tenta buscar o usuário com match exato no campo e-mail
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            # Se não houver match exato, tenta buscar de forma case-insensitive
            try:
                user_obj = User.objects.get(email__iexact=email)
                # Se encontrado apenas de forma case-insensitive, considere que o e-mail foi digitado de forma errada
                messages.warning(request, "E-mail inválido")
                return render(request, 'users/login.html', {'email': email})
            except User.DoesNotExist:
                messages.warning(request, "E-mail inexistente")
                return render(request, 'users/login.html', {'email': email})
        
        # Se o e-mail foi encontrado exatamente, tenta autenticar o usuário
        user = authenticate(request, username=user_obj.username, password=password)
        if user is not None:
            # Trata o "Lembrar de mim"
            if request.POST.get('remember_me'):
                request.session.set_expiry(1209600)  # 2 semanas
            else:
                request.session.set_expiry(0)  # Expira ao fechar o navegador
            
            auth_login(request, user)  # Usando auth_login para evitar conflito de nomes
            messages.success(request, f'Bem vindo, {user.username}!')
            return redirect('menu')
        else:
            messages.warning(request, "Senha inválida")
            return render(request, 'users/login.html', {'email': email})
    else:
        return render(request, 'users/login.html')  
    
@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu com sucesso.')
    return redirect('index')

@login_required
def menu(request):
    return render(request, 'users/menu.html')