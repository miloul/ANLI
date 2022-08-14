from codecs import getencoder
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from django.contrib import auth

# Create your views here.
def register(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        username = request.POST.get('username',None)   #딕셔너리형태
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')
        print(password)
        print(re_password)
        res_data = {} 
        if not (username and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
        else :
            #print(username)
            user = User(
                username = request.POST['username'],   #딕셔너리형태
                password = request.POST['password'],
                nickname = request.POST['nickname'],
                ph = request.POST['ph'],
                email = request.POST['email'],
                # gender = request.POST.get('gender',None)
                # birth_year = request.POST.get('birth_year',None)
                # birth_month = request.POST.get('birth_month',None)
                # birth_day = request.POST.get('birth_day',None)
                account_name = request.POST['account_name'],
                account_bank = request.POST['account_bank'],
                account = request.POST['account']
            )
            user.save()
            #auth.login(request, user) #로그인까지해줌
            return render(request, 'login.html')        
        return render(request, 'register.html', res_data) #register를 요청받으면 register.html 로 응답.
    
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not (username and password):
            return render(request, 'login.html', {'error': '아이디와 비밀번호 모두를 입력하세요'})
        else : 
            user = User.objects.get(username=username) 
            print(user)
            print(User.objects.get(username=username))
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if password == user.password:
                return redirect('/')
            else:
                return render(request, 'login.html', {'error': 'username or password is incorrect'})
