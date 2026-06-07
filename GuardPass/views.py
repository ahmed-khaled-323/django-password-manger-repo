from django.shortcuts import render ,redirect
from .models import ex_accounts
import uuid
from django.contrib.auth import authenticate

# Create your views here.
def add_new_account(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            gmail = request.POST.get('gamil')
            password =request.POST.get('password')
            bio =  request.POST.get('bio')
            if gmail and password and bio:
                exaccount = ex_accounts.objects.create(owner=request.user,UserName =gmail,Password=password,bio=bio)
                exaccount.save()
                return redirect('/Guardpass/')
            else:
                print ("username or password is epty")
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
    if request =='POST':
        if request.user.is_authenticated:
            account =ex_accounts.objects.filter(id=account_id)
            account.delete()
        else:
            return redirect('/')
    else: return redirect('/Guardpass/')
    return redirect('/Guardpass/')




    