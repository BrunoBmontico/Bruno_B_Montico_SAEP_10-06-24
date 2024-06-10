from django.shortcuts import render, get_object_or_404, redirect                    # REQUESTS PADROES DJANGO
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout                         # REQUERIMENTO DE LOGIN
from django.db.models import ProtectedError
from core.models import *


# Create your views here.
def login_professor(request):
    if request.method == 'GET':
        return render(request, 'core/login.html')
    else:
        email_professor = request.POST.get('email_professor')
        senha_professor = request.POST.get('senha_professor')

        usuario = authenticate(username=email_professor, password=senha_professor)

        if usuario:
            login(request, usuario)
            return redirect(f'/tela_professor/{request.user.id}')
        
        else:
            return HttpResponse('E-mail ou Senha incorretos')
        
# logout
def logout_usuario(request):
    logout(request)
    return redirect('/')
        
#Cadastrar Professor
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'core/cadastro.html')
    else:
        nome_professor = request.POST.get('nome_professor')
        sobrenome_professor = request.POST.get('sobrenome_professor')
        senha_professor = request.POST.get('senha_professor')
        email_professor = request.POST.get('email_professor')

        if nome_professor and sobrenome_professor and senha_professor and email_professor !='':
            usuario = User.objects.filter(username=email_professor).first()
            if usuario:
                return HttpResponse('Esse E-mail ja existe!')
            else:
                usuario = User.objects.create_user(

                    first_name=nome_professor,
                    last_name=sobrenome_professor,
                    email=email_professor,
                    username=email_professor, 
                )

                usuario.set_password(senha_professor)
                usuario.save()
                return redirect('/')
            
#Cadastro Turma
def cadastro_turma(request, id):
    usuario = get_object_or_404(User, pk=id)
    if request.method == 'GET':
        return render(request, 'core/cadastro_turma.html')
    else:
        nome_turma = request.POST.get('nome_turma')

        if nome_turma != '':
            turma = Turma.objects.create(
                nome_turma = nome_turma,
                id_professor = usuario,
                nome_professor = usuario.first_name,
            )
            turma.save()
            return redirect(f'/tela_professor/{request.user.id}')
        else:
            return HttpResponse('Verifique os campos')

#area da turma
def area_turma(request, id):
    if request.method == 'GET':
        turma = get_object_or_404(Turma, pk=id)
        atividades = Atividade.objects.all()

        atividades_turma = atividades.filter(id_turma=turma)

        context = {
            'turma': turma,
            'atividades_turma': atividades_turma,
        }
        return render(request, 'core/tela_turma.html', context)

#cadastro Atividades
def cadastro_atividades(request, id_professor, id_turma):
    usuario = get_object_or_404(User, pk=id_professor)
    turma = get_object_or_404(Turma, pk=id_turma)

    context = {
        'usuario': usuario,
        'turma': turma
    }

    if request.method == 'GET':
        return render(request, 'core/cadastro_atividade.html', context)
    else:
        nome_atividade = request.POST.get('nome_atividade')

        atividade = Atividade.objects.create(
            nome_atividade = nome_atividade,
            id_professor = usuario,
            nome_professor = usuario.first_name,
            id_turma = turma,
            nome_turma = turma.nome_turma,
        )
        atividade.save()
        return redirect(f'/tela_turma/{turma.id}')

#area do professor
def area_professor(request, id):
    if request.method == 'GET':
        turmas = Turma.objects.all()
        turmas_professor = turmas.filter(id_professor=request.user.id)
        return render(request, 'core/tela_professor.html', {'turmas_professor': turmas_professor})
    

#excluir turma
def excluir_turma(request, id_turma):
    turma = get_object_or_404(Turma, pk=id_turma)
    atividades = Atividade.objects.all()

    try:
        for atividade in atividades:
            turma.delete()
            return redirect(f'/tela_professor/{request.user.id}')
    except ProtectedError:
        return HttpResponse('Essa turma tem atividades não e possivel excluir')

def confirmar(request, id_turma):
    turma = get_object_or_404(Turma, pk=id_turma)
    return render(request, 'core/confirmar_excluir.html',{'turma':turma})