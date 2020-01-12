from django.shortcuts import render

def index_landing_page(request):
    return render(request,'pages/index_landing_page.html')


def homepage(request):
    return render(request,'pages/homepage.html')
