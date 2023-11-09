from django.http import HttpResponse
from django.shortcuts import render
from re import template
from companyapi.settings import EMAIL_HOST_USER
from django.core.mail import send_mail 
def homepage(request):
    print("Home")
    return render(request,'homepage.html')
    return HttpResponse("my home page")

def index(request):
    return render(request,'index.html')
    return HttpResponse("home page")
    pass
def sendmail(request):
    subject = 'Subject of the email'
    message = 'Plain text version of the email.'
    from_email = EMAIL_HOST_USER
    print(from_email)
    recipient_list = ['shubhamkumar9264shu@gmail.com']
    print(recipient_list)
    html_message = '<p>HTML version of the email.</p>'
    print(html_message)

    send_mail(subject, message, from_email, recipient_list, html_message=html_message)
    return render(request,'index.html')

