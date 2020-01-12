from django.shortcuts import render

def communications(request):
    return render(request,r'communications/contact_us_page.html')


