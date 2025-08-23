# импорт функции path для определения маршрутов
from django.urls import path

# импортируем локальные views (функции/классы), которые опишем в catalog/views.py
from . import views

# определяем список URL-паттернов для этого приложения
urlpatterns = [
    # пустой путь '' — корень сайта — вызывает views.index
    path("", views.index, name="catalog-index"),
    # позже здесь добавим маршруты для списка книг, деталей книги и т.д.
]
