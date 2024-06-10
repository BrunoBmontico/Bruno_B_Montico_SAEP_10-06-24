from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_professor, name='login_professor'),
    path('logout/', views.logout_usuario, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar_turma/<int:id>/', views.cadastro_turma, name='cadastrar_turma'),
    path('cadastrar_atividade/<int:id_usuario>/<int:id_turma>/', views.cadastro_atividades, name='cadastrar_atividade'),
    path('tela_professor/<int:id>/', views.area_professor, name='area_professor'),
    path('tela_turma/<int:id>', views.area_turma, name='area_turma'),
    path('deletar/<int:id_turma>/', views.excluir_turma, name='deletar' ),
    path('confirmar/<int:id_turma>/', views.confirmar, name='confirmar')
]