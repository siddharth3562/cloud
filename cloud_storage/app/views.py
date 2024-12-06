from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User

# Create your views here.

def e_login(req):
    if 'user' in req.session:
        return redirect(user_home)
    if req.method == 'POST':
        uname = req.POST['uname']
        password = req.POST['password']
        data = authenticate(username=uname, password=password)
        if data:
            login(req, data)
            req.session['user'] = uname
            return redirect(user_home)
        else:
            messages.warning(req, "invalid username or password")
            return redirect(e_login)
    else:
        return render(req, 'login.html')


def user_home(req):
    if 'user' in req.session:
        user = User.objects.get(username=req.session['user'])  # Get the logged-in user
        user_files = Files.objects.filter(user=user)  # Fetch the files uploaded by the user

        if req.method == 'POST' and req.FILES.get('file'):  # Check if file is uploaded via POST
            dis = req.POST.get('dis')  # Get the description from the form
            file = req.FILES.get('file')  # Get the uploaded file from the form
            files = Files(dis=dis, file=file, user=user)  # Create the file object
            files.save()  # Save the file object in the database

        return render(req, 'home.html', {'user_files': user_files})  # Render home page with user's files
    else:
        return redirect('e_login')
    
def e_logout(req):
    logout(req)
    req.session.flush()
    return redirect(e_login)

def user_reg(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['pswd']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswd)
            data.save()
        except:
            messages.warning(req, "email already in use")
            return redirect(user_reg)   
        return redirect(e_login)
    else:
        return render(req,'reg.html')
    
def delete_product(req,fid):
    file = Files.objects.get(pk=fid)
    file_path = file.file.name  
    file_name = file_path.split('/')[-1]
    os.remove('media/'+file_name)
    file.delete()  
    return redirect(user_home)  


