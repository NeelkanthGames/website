from django.shortcuts import render

def games_list(request):
    return render(request,'games/games_list.html')


