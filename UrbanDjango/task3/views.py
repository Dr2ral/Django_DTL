from django.shortcuts import render

# Create your views here.
def main(request):
    title = 'Мой магазин'
    h1 = 'Главная страница'
    context = {
        'title': title,
        'h1': h1
    }
    return render(request, 'platform.html', context)

def game(request):
    return render(request, 'games.html')

def cart(request):
    return render(request, 'cart.html')