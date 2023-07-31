from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import uuid
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth import update_session_auth_hash
from .forms import *
import random
import string
from django.http import HttpResponse
from django.http import JsonResponse

######################################################################### <<<<<<<<<< LANDING MODULE >>>>>>>>>>>>>>
def index(request):
    return render(request, 'index/index.html')



def user_type(request):
  
    return render(request, 'index/user_type.html')

def login_main(request):
    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('login_main')
        
        if User_Registration.objects.filter(username=request.POST['username'], password=request.POST['password'],role="user1").exists():

            member = User_Registration.objects.get(username=request.POST['username'],password=request.POST['password'])
            
            request.session['userid'] = member.id
            if User_Registration.objects.filter(username=request.POST['username'], password=request.POST['password'],role="user1", status="Approved").exists():
                return redirect('staff_home')
            else:
               return redirect('staff_validate') 


       

        elif User_Registration.objects.filter(username=request.POST['username'], password=request.POST['password'],role="user2").exists():
            member = User_Registration.objects.get(username=request.POST['username'],password=request.POST['password'])
            request.session['userid'] = member.id
            if Profile_User.objects.filter(user_id=member.id).exists():
                return redirect('user_home')
            else:
                return redirect('profile_user_creation')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,'index/login.html')

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if  User_Registration.objects.filter(email=email).exists():
            user =  User_Registration.objects.get(email=email)

        

            current_site = get_current_site(request)
            mail_subject = "Reset your password"
            message = render_to_string('index/forget-password/reset_password_email.html',{
                'user':user,
                'domain' :current_site,
                'user_id' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token(user),
            }) 

            to_email = email
            send_email = EmailMessage(mail_subject,message,to = [to_email])
            send_email.send()

            messages.success(request,"Password reset email has been sent your email address.")
            return redirect('login_main')
        else:
            messages.error(request,"This account does not exists !")
            return redirect('forgotPassword')
    return render(request,'index/forget-password/forgotPassword.html')


def resetpassword_validate(request,uidb64,token):
    try:
        user_id = urlsafe_base64_decode(uidb64).decode()
        user =  User_Registration._default_manager.get(pk=user_id)  
    except(TypeError,ValueError,OverflowError, User_Registration.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user,token):
        request.session['user_id'] = user_id 
        messages.success(request,"Please reset your password.")
        return redirect('resetPassword')
    else:
        messages.error(request,"The link has been expired !")
        return redirect('login_main')
    
def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('user_id') 
            user =  User_Registration.objects.get(pk=uid)
            user.password = password
            user.save()
            messages.success(request,"Password reset successfull.")
            return redirect('login_main')

        else:
            messages.error(request,"Password do not match")
            return redirect('resetPassword')
    else:
        return render(request,'index/forget-password/resetPassword.html')

############################################################# <<<<<<<<<< STAFF MODULE >>>>>>>>>>>>>>

def staff_validate(request):
    return render(request, 'staff/staff_validate.html')
    


def staff_home(request):
    items = item.objects.all()
    return render(request, 'staff/staff_home.html',{'items':items})
#################################
def delete_item(request,id):
    d1=item.objects.get(id=id)
    d1.delete()
    return redirect('/staff_home/')
    

# def item_edit(request, item_id):
#     its = item.objects.get(id=item_id)
#     its.user=request.POST.get('user')
#     its.category=request.POST.get('category')
#     its.title_description=request.POST.get('title_description')
#     its.description=request.POST.get('description')
#     its.price=request.POST.get('price')
#     its.rating=request.POST.get('rating')
#     its.buying_count=request.POST.get('buying_count')
#     its.offer=request.POST.get('offer')
#     its.image=request.POST.get('image')
#     its.save()
#     return redirect("/staff_home/")
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import item
# from .forms import itemForm

# def item_edit(request, item_id):
#     its = get_object_or_404(item, id=item_id)

#     if request.method == 'POST':
#         form = itemForm(request.POST, request.FILES, instance=its)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')  # Redirect to a page showing the updated product list.

#     else:
#         form = itemForm(instance=its)

#     return render(request, 'edit_item.html', {'form': form, 'data': its})


#######################################logout################### <<<<<<<<<< USER MODULE >>>>>>>>>>>>>>>>

def user_base(request):
    ids=request.session['userid']
    usr=Profile_User.objects.get(user=ids)
    context={
        'user':usr
    }
    return render(request, 'user/user_base.html',context)

def user_home(request):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=Profile_User.objects.get(user=ids)
    context={
        'user':usr
    }
    return render(request, 'user/user_home.html',context)

def user_registration(request):

    if request.method =='POST':
        form = User_RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User_Registration.objects.filter(email=email).exists():
                messages.error(request, 'Email Id already exists')
                return redirect('creator_registration')
            else:
                user_model=form.save()
            user_id = user_model.pk
            return redirect('index_user_confirmation',user_id=user_id)
    else:
        form = User_RegistrationForm()
        form.initial['role'] = 'user2'
    return render(request,'index\index_user\index_user_registraion.html',{'form':form})


def index_user_confirmation(request,user_id):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            print("success")
            if User_Registration.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('index_user_confirmation', user_id=user_id)
            else:
                artist_object = get_object_or_404(User_Registration, pk=user_id)
                artist_object.username=username
                artist_object.password = password
                artist_object.save()
                messages.success(request, 'Thank you for registering with us.')
                return redirect('login_main')
        else:
            messages.error(request, ' Password and Confirm Password are not matching. Please verify it.')
            return redirect('index_user_confirmation', user_id=user_id)

    return render(request,'index\index_user\index_user_confirmation.html',{'user_id':user_id})

def profile_user_creation(request):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    ids=request.session['userid']
    usr=User_Registration.objects.get(id=ids)
    if request.method =="POST":
        
        firstname = request.POST.get('firstname',None)
        lastname = request.POST.get('lastname',None)
        phonenumber = request.POST.get('phonenumber',None)
        email = request.POST.get('email',None)
        gender = request.POST.get('gender',None)
        address = request.POST.get('address',None)
        date_of_birth= request.POST.get('date_of_birth',None)
        pro_pics = request.FILES.get('propic',None)
        secondnumb = request.POST.get('secondnumb',None)
        profile_artist = Profile_User(
            firstname=firstname,
            lastname=lastname,
            phonenumber=phonenumber,
            email=email,
            gender=gender,
            date_of_birth=date_of_birth,
            address=address,
            pro_pic=pro_pics,
            user=usr,
            secondnumber=secondnumb
        )
        profile_artist.save()


        return redirect('user_home')
    context={
        'user':usr
    }
    return render(request,'index\index_user\profile_user_creation.html', context)


def logout(request):
    if 'userid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')
    

def product_view(request, item_id):
    try:
        item_instance = item.objects.get(id=item_id)
        oprice = item_instance.price

        if item_instance.offer:
            off = item_instance.offer
            rp = oprice - (oprice * (off / 100))
        else:
            rp = oprice

        return render(request, 'user/productview.html', {'item': item_instance, 'rp': rp})

    except item.DoesNotExist:
        # Handle the case where the item does not exist
        return HttpResponse("Item not found", status=404)
    
####################################################
def items_view(request):
    items = item.objects.all()
    item_data = []
    for x in items:
        oprice = x.price
        if x.offer:
            off = x.offer
            rp = oprice - (oprice * (off/100))
        else:
            rp = oprice
        item_data.append({'item': x, 'rp': rp})

    return render(request, 'user/items_view.html', {'item_data': item_data})

######################################################
