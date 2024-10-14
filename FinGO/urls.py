from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="FinGO"),
    path('despesas', views.despesas, name="despesas"),
    path('receitas', views.receitas, name="receitas"),
    path('categorias', views.categorias, name="categorias"),
    path('metas', views.metas, name="metas"),
    path('configuracoes', views.configuracoes, name="configuracoes"),
]