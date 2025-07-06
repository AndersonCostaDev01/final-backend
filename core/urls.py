"""
Configuração de URL para o projeto core.
A lista `urlpatterns` roteia URLs para views. Para mais informações, consulte:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Exemplos:
Views baseadas em função
    1. Adicione um import:  from my_app import views
    2. Adicione uma URL ao urlpatterns:  path('', views.home, name='home')
Views baseadas em classe
    1. Adicione um import:  from other_app.views import Home
    2. Adicione uma URL ao urlpatterns:  path('', Home.as_view(), name='home')
Incluindo outro URLconf
    1. Importe a função include: from django.urls import include, path
    2. Adicione uma URL ao urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # suas rotas aqui
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
]
