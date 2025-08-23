# импортируем HttpResponse для быстрого возврата текста (удобно для теста)
from django.http import HttpResponse

# Create your views here.


def index(request):
    """
    Простая тестовая view для каталога.
    При запросе на корень сайта вернёт текст — это позволит проверить,
    что приложение подключено корректно.
    """
    # возвращаем HTTP-ответ с коротким текстом
    return HttpResponse("Hello, Bookstore — catalog OK")
