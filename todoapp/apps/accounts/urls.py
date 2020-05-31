from django.urls import path
from . import views


app_name = 'accounts'


urlpatterns = [
    path('novo-usuario/', views.add_user, name='add_user'),
    path('login/', views.user_login, name='user_login'),
    path('sair/', views.user_logout, name='user_logout'),
    path('alterar-senha/', views.user_change_password, name='user_change_password'),
    path('novo-perfil/', views.add_user_profile, name='add_user_profile'),
    path('meu-perfil/', views.list_user_profile, name='list_user_profile'),
    path('alterar-perfil/<username>', views.user_change_profile, name='user_change_profile'),
    path('alterar-usuario/<username>', views.user_change_information, name='user_change_information'),
]
