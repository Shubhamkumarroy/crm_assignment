from django.http import HttpResponse
from django.shortcuts import render
from re import template
from companyapi.settings import EMAIL_HOST_USER,EMAIL_HOST_PASSWORD
from django.core.mail import send_mail 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import render,HttpResponse
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import email
import time
from re import template
import re
from datetime import datetime
from unittest import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date,datetime
from django.db import IntegrityError
from django.utils import timezone
import random






def dashboard(request):
    customer=Newcustomer.objects.all()
    context={
        'customer':customer
    }
    return render(request,'index.html',context)



@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            print(request.POST)
            name = request.POST['name']
            email = request.POST['email']
            phone=request.POST['phone']
            address=request.POST['address']
            # print(address)
            pass1 = request.POST['password']
            # type=request.POST['type']
            # print(type)
            check_user_admin=False
            if 'type' in request.POST:
                check_user_admin=True

            print(check_user_admin)
           
            myuser = User.objects.create_user(name, email,pass1)
            myuser.save()
            otp=random.randint(100000,999999)
            newuser=User_detail(user_detail_name=name, user_detail_email=email, user_detail_phone=phone,user_detail_address=address,user_detail_otp=otp,user_detail_password=pass1,check_admin_user=check_user_admin)
            newuser.save()
            return redirect('/loginuser')
        except IntegrityError:
            error_message = "Username or email already taken. Please choose a different username or email."
            return render(request, 'signup.html', {'error_message': error_message})
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'error_page.html', {'error_message': error_message})
    else:
        return render(request, 'signup.html')
    

def loginuser(request):
    if request.method == "POST":
        try:
            user_d = request.user
            email = request.POST['email']
            pass1 = request.POST['password']
            user=User_detail.objects.get(user_detail_email=email)
            u1=User.objects.get(email=email)
            login(request,u1)
            print(user)
            if user.user_detail_password==pass1 :
                if user.check_admin_user == True:
                    customer=Newcustomer.objects.all()
                    context={
                        'customer':customer
                    }
                    return render(request,'index.html',context)
                else:
                    customer=Newcustomer.objects.filter(email=email)
                    sz=len(customer)
                    if sz ==0:
                        error_message="Currently you are not customer on this plateform so admin have to add u as a customer"
                        return render(request, 'error_page.html', {'error_message': error_message})
                    else:
                        customer=customer[0]
                        receiver_email=customer.manager.user_detail_email
                        return redirect(f'/msgdisplay/{receiver_email}')
            else:
                error_message = "Invalid username or password."
                return render(request, 'loginpage.html', {'error_message': error_message})
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'error_page.html', {'error_message': error_message})
    else:
        return render(request, 'loginpage.html')


def logoutuser(request):
    try:
        logout(request)
    except Exception as e:
        # Handle exceptions by displaying an error page or message
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})
    
    return render(request, 'loginpage.html')
def index(request):
    return render(request,'signup.html')

def adddata(request):
    return render(request,'addcustomer.html')
def addcustomer(request):
    if request.method =="POST":
        try:
            user=request.user
            print(-111111)
            print(user)
            username=user.username
            manager=User_detail.objects.get(user_detail_name=username)
            print(manager)
            name = request.POST['name']
            email = request.POST['email']
            phone=request.POST['phone']
            address=request.POST['address']
            gstnumber=request.POST['gstnumber']
            mailreminder=request.POST['mailreminder']
            cus=Newcustomer(username=username,name=name,email=email,phone=phone,address=address,gstnumber=gstnumber,mailreminder=mailreminder,manager=manager)
            cusc=Newcustomer.objects.filter(email=email,manager=manager)
            sz=len(cusc)
            if sz>0:
                error_message = "Customer already exist"
                return render(request,'error_page.html',{'error_message':error_message})
            else:
                cus.save()
                customer=Newcustomer.objects.all()   
                context={
                    'customer':customer
                }
                return render(request,'index.html',context)

        except Exception as e:
        # Handle exceptions by displaying an error page or message
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'error_page.html', {'error_message': error_message})


    else:
        customer=Newcustomer.objects.all()
        context={
            'customer':customer
        }
        return render(request,'index.html',context)

# def mailbyuser(request):

def edit(request,id1):
        if request.method =="POST":
            name = request.POST['name']
            email = request.POST['email']
            phone=request.POST['phone']
            address=request.POST['address']
            gstnumber=request.POST['gstnumber']
            mailreminder=request.POST['mailreminder']
            cus=Newcustomer.objects.get(id=id1)
            cus.name=name
            cus.email=email
            cus.phone=phone
            cus.address=address
            cus.gstnumber=gstnumber
            cus.mailreminder=mailreminder
            cus.save()
            return redirect('/dashboard')
        else:
            cus=Newcustomer.objects.get(id=id1)
            return render(request,'editpage.html',{'cus':cus})



def delete(request,id1):
    cus=Newcustomer.objects.get(id=id1)
    cus.delete()
    return redirect('/dashboard')
def sendemail(request,id1):
    if request.method =="POST":
        sender_email = EMAIL_HOST_USER
        sender_password = EMAIL_HOST_PASSWORD
        customer=Newcustomer.objects.get(id=id1)
        receiver_email = customer.email
        subject = request.POST['subject']
        body = request.POST['body']
        email_body = MIMEText(body, 'plain')
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(email_body)
        customer=Newcustomer.objects.all()
        context={
            'customer':customer
        }
        print(msg,sender_email,sender_password)
        
        error_message = "Email sent successfully"
        customer=Newcustomer.objects.get(id=id1)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)  # For Gmail
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            print("Email sent successfully")
            return render(request,'sendemail.html',{'customer':customer,'error_message':error_message})
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    else:
        customer=Newcustomer.objects.get(id=id1)
        return render(request,'sendemail.html',{'customer':customer})


   
# @login_required

def msgdisplay(request,receiver_email):
    receiver1=User_detail.objects.get(user_detail_email=receiver_email)
    messages =ChatMess.objects.filter(
        (models.Q(sender_email=request.user.email, receiver_email=receiver_email) | models.Q(sender_email=receiver_email, receiver_email=request.user.email))
    ).order_by('timestamp')
    
    return render(request, 'chattemp.html', {'receiver_email': receiver_email, 'messages': messages, 'receiver1':receiver1})
def chat(request, receiver_email):
    newcustomer=User_detail.objects.filter(user_detail_email=receiver_email)
    sz=len(newcustomer)
    if sz==0:
        error_message="to enable chat option customer have to create account on this plateform"
        customer=Newcustomer.objects.all()   
        context={
            'customer':customer
        }
        context['error_message']=error_message
        return render(request,'index.html',context)
        
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message:
           ChatMess.objects.create(sender_email=request.user.email, receiver_email=receiver_email, message=message)

        messages =ChatMess.objects.filter(
            (models.Q(sender_email=request.user.email, receiver_email=receiver_email) | models.Q(sender_email=receiver_email, receiver_email=request.user.email))
        ).order_by('timestamp')
        return redirect(f'/msgdisplay/{receiver_email}')
        return render(request, 'chattemp.html', {'receiver_email': receiver_email, 'messages': messages})
    else:
        messages =ChatMess.objects.filter(
            (models.Q(sender_email=request.user.email, receiver_email=receiver_email) | models.Q(sender_email=receiver_email, receiver_email=request.user.email))
        ).order_by('timestamp')
        return redirect(f'/msgdisplay/{receiver_email}')


    






        


