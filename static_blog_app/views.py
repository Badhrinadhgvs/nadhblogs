from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.contrib.auth.decorators import login_required


from bs4 import BeautifulSoup
import requests

# Create your views here.



res=requests.get("https://techcrunch.com/category/artificial-intelligence/")
soup=BeautifulSoup(res.content,'html.parser')
ai=soup.find_all("a",class_="post-block__title__link")
Ai=[]
for i in ai:
    c=i.text
    Ai.append(c)
qlinks=[]
for i in ai:
    x=i.get("href")
    qlinks.append(x)
    qlinks
tech=zip(Ai,qlinks)        



@login_required(login_url="/register/")
def about(request):
  # Your logic for the About page (optional)
  return render(request, 'static_blog_app/about.html')  


def content(request):
   Tit=Des.Title()
   desc =Des.Desc()
   return render(request,'static_blog_app/content.html',{'title':Tit,'descri':desc})
 
 
def nothing(request):
  if request.method=="POST":
    tit=request.POST.get('hjmb')
    mail=request.POST.get('kljbf')
    ds=request.POST.get('lvkmf')
  return render(request,'static_blog_app/write.html')







def ai_blog(request):
    return render(request,'static_blog_app/Ai.html',{'TITLE':tech})
  
  
  
res=requests.get("https://techcrunch.com/category/venture/")
soup=BeautifulSoup(res.content,'html.parser')
stock=soup.find_all('a',class_="post-block__title__link")
stock_txt=[]
for i in stock:
    x=i.text
    stock_txt.append(x)
stock_links=[]
for i in stock:
    x=i.get("href")
    stock_links.append(x)
    
stock=zip(stock_txt,stock_links)


def stock_blog(request):
  return render(request,'static_blog_app/stock.html',{'stock':stock})
      
  

res=requests.get("https://techcrunch.com/category/cryptocurrency/")
soup=BeautifulSoup(res.content,'html.parser')
crypto=soup.find_all('a',class_="post-block__title__link")
crypto_txt=[]
for i in crypto:
    x=i.text
    crypto_txt.append(x)
crypto_links=[]
for i in crypto:
    x=i.get("href")
    crypto_links.append(x)
Crypto=zip(crypto_txt,crypto_links)

def crypto_blog(request):
  return render(request,'static_blog_app/crypto.html',{'cr':Crypto})          


main=zip(tech,stock,Crypto)
def show(request):
  return render(request,'static_blog_app/index.html',{'main':main})


def login_main(request):
  if request.method=="POST":
    username=request.POST.get("username")
    password=request.POST.get("password")
    if not User.objects.filter(username=username).exists():
      messages.info(request,'Username already taken')
      return redirect("login-portal")
    
    user=authenticate(username=username,password=password)
    
    if user is None:
      messages.info(request,'User did not exist')
      return redirect('login-portal')
    else:
      login(request,user)
      return redirect('Ai-blog')
      
      
    
  return render(request,'static_blog_app/Login.html')



def logout_main(request):
  logout(request)
  return redirect('login-portal')

def register(request):
  if request.method=="POST":
         username=request.POST.get("username")
         password=request.POST.get("password")
         email=request.POST.get("email")
         user=User.objects.filter(username=username)
         if user.exists():
           messages.info(request,'Username already taken')
           return redirect("register")
         c = User.objects.create_user(username=username,email=email,password=password)
         c.save()
         messages.info(request,'Account created successfully')
         return redirect("register")
         
  return render(request,"static_blog_app/register.html")


# if request.method=="POST":
#         username=request.POST.get("username")
#         password=request.POST.get("password")
#         email=request.POST.get("email")
#         c = User.objects.create_user(username=username,email=email,password=password)
#         c.save()
#         return redirect("login-portal")