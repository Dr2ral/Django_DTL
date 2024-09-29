from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
# Create your views here.

#def sign_up_by_html(request):
#    users = ['Vladislav', 'Alexander', 'Vitalik']
#    info = {}
#    if request.method == 'POST':
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        password2 = request.POST.get('password2')
#        age = request.POST.get('age')
#        if password == password2 and int(age) >= 18 and username not in users:
#            return HttpResponse(f"Приветствуем, {username}!")
#        elif password != password2:
#            info['error'] = 'Пароли не совпадают'
#            return render(request, 'registration_page.html', {'info': info})
#            #return HttpResponse(info['error'])
#        elif int(age) < 18:
#            info['error'] = 'Вы должны быть старше 18'
#            return HttpResponse(info['error'])
#        elif username in users:
#            info['error'] = 'Пользователь уже существует'
#            return HttpResponse(info['error'])
#
#    return render(request, 'registration_page.html', {'info': info})


def sign_up_by_django(request):
    users = ['Vladislav', 'Alexander', 'Vitalik']
    if request.method == 'POST':
        info = UserRegister(request.POST)
        if info.is_valid():
            username = info.cleaned_data['username']
            password = info.cleaned_data['password']
            repeat_password = info.cleaned_data['repeat_password']
            age = info.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                return HttpResponse(f"Приветствуем, {username}!")
            if password != repeat_password:
                return HttpResponse('Пароли не совпадают')
            elif int(age) < 18:
                return HttpResponse('Вы должны быть старше 18')
            elif username in users:
                return HttpResponse('Пользователь уже существует')

    else:
        info = UserRegister()
    return render(request, 'registration_page.html', {'info': info})

