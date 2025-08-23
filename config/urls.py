"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

# импорт текущих настроек, чтобы в DEBUG отдавать медиа-файлы локально
from django.conf import settings
from django.conf.urls.static import static

# импорт админки Django
from django.contrib import admin

# импорт path и include для маршрутизации
from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# основной список URL-ов для проекта
urlpatterns = [
    # URL для админки: /admin/
    path("admin/", admin.site.urls),
    # подключаем URL-ы приложения catalog на корневой путь ''
    # все пути, описанные в catalog/urls.py, будут доступны с корня сайта
    path("", include("catalog.urls")),
]

# в режиме DEBUG (локально) отдаём медиа-файлы через Django (не для продакшена)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
