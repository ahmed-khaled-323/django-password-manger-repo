from django.shortcuts import render ,redirect
from .models import ex_accounts
import uuid
from django.contrib.auth import authenticate
from cryptography.fernet import Fernet
from django.conf import settings
from django.contrib import messages
EK = settings.ENCRYPTION_KEY
f = Fernet(EK)
# Create your views here.
def add_new_account(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            gmail = request.POST.get('gamil')
            password =request.POST.get('password')
            bio =  request.POST.get('bio')
            if gmail and password and bio:
                Encrypted_gmail = f.encrypt(bytes(gmail,"utf-8"))
                Encrypted_password = f.encrypt(bytes(password,"utf-8"))
                Encrypted_bio = f.encrypt(bytes(bio,"utf-8"))
                print (Encrypted_gmail)
                exaccount = ex_accounts.objects.create(owner=request.user,UserName =Encrypted_gmail,Password=Encrypted_password,bio=Encrypted_bio)
                return redirect('/Guardpass/')
            else:
                messages.error(request,'Some fields Is Empty')
    else:
        return redirect('/')
            
    return render(request ,'gardpass-pages/add-account.html')

def show_accounts_list(request):
    if request.user.is_authenticated:
        accounts = ex_accounts.objects.filter(owner = request.user)
    else:
       return redirect('/')
    return render(request,'gardpass-pages/manager.html',{'accounts':accounts})

def show_account(request , account_id):
    if request.user.is_authenticated:
        account = ex_accounts.objects.filter(id = account_id)
    else:
        return redirect('/')
    return render(request , 'gardpass-pages/account.html',{"accounts": account })

def delete(request , account_id): 
    if request.method =='POST':
        if request.user.is_authenticated:
            account =ex_accounts.objects.filter(id=account_id)
            account.delete()
        else:
            return redirect('/')
    else: return redirect('/Guardpass/')
    return redirect('/Guardpass/')




    