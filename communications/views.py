from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from .forms import CommunicationsForm

def communications(request):
    #return render(request,r'communications/contact_us_page.html')
    from_email = None
    if request.user.is_authenticated:
        from_email = request.user.email
        user = request.user.username

    if request.method == 'POST':
        form = CommunicationsForm(request.POST)
        if form.is_valid():
            category = request.POST.get('category')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            from_email = request.POST.get('from_email')

            try:
                title = "("+category+")"+" "+subject
                email = EmailMessage(
                    title,
                    message,
                    from_email,
                    ['mdas.160395@gmail.com','neelkanthgames777@gmail.com'],
                    reply_to=[from_email],
                )
                email.send()
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return render(request,r'communications/contact_success.html')
        else:
            messages.error(request, 'Email not sent. Expand Email tab to check errors.')
            return render(request, r'communications/contact_us_page.html',{'form':CommunicationsForm(request.POST)})
    else:
        return render(request, r'communications/contact_us_page.html',{'form':CommunicationsForm(initial={'from_email':from_email})})


