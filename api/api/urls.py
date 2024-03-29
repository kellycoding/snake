"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from api.boards import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('snake/api/getRandomSentence', views.getRandomSentence),
    path('snake/api/createWord', views.createWords),
    path('snake/api/getLevels', views.getLevels),
    path('snake/api/getProficiencies', views.getProficiencies),
    path('snake/api/getWordFullList', views.getWordFullList),
    path('snake/api/updateProficiencyInSnake', views.updateProficiencyInSnake),
    path('snake/api/getRandomWord', views.getRandomWord),
    path('snake/api/updateTestResult', views.updateTestResult),
    path('snake/api/getRandomPhrase', views.getRandomPhrase),
    path('snake/api/updatePhraseTestResult', views.updatePhraseTestResult),
    path('snake/api/createText', views.createText),
    path('snake/api/getTextList', views.getTextList),
    path('snake/api/getTextById', views.getTextById),
    path('snake/api/getTextByTitle', views.getTextByTitle),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
