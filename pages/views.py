from django.shortcuts import render
from django.forms import modelformset_factory

from .models import Videos, CurrentProject, CurrentProjectImages, News, Reviews
from accounts.models import UserProfileInfo
from .forms import VideosToUploadForm, CurrentProjectForm, CurrentProjectImageForm, NewsForm, ReviewsForm


def index_landing_page(request):
    return render(request,'pages/index_landing_page.html')


def homepage(request):
    # if request.user.is_authenticated:
    #     try:
    #         account = UserProfileInfo.objects.get(user=request.user)
    #         print(account.full_name)
    #     except:
    #         account = "NULL"
    # else:
    #     account = "NULL"
    try:
        currentProject = CurrentProject.objects.get()
        currentProjectImages = CurrentProjectImages.objects.filter(title=currentProject)
    except:
        currentProject = None
        currentProjectImages = None
    try:
        videos = Videos.objects.filter(active_flag=True).order_by('-created_date')[:10]
    except:
        videos = None
    try:
        news = News.objects.order_by("-created_date")
    except:
        news = News.objects.none()
    try:
        reviews = Reviews.objects.filter(active_flag=True)
    except:
        reviews = Reviews.objects.none()

    context = {
        'currentProject': currentProject,
        'currentProjectImages': currentProjectImages,
        'videos': videos,
        # 'account': account,
        'news': news,
        'reviews': reviews
    }
    return render(request,'pages/homepage.html',context)

def upload_videos(request):
    if request.method == 'POST':
        form = VideosToUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'pages/upload_videos_page.html',{'video_upload_form':VideosToUploadForm()})
        else:
            return render(request,'pages/upload_videos_page.html',{'video_upload_form':form})
    else:
        return render(request,'pages/upload_videos_page.html',{'video_upload_form':VideosToUploadForm()})


def upload_current_project(request):
    if request.method == 'POST':
        projectForm = CurrentProjectForm(request.POST)
        image_form = CurrentProjectImageForm(request.POST,request.FILES)
        images = request.FILES.getlist('image')
        if projectForm.is_valid() and image_form.is_valid():
            try:
                CurrentProject.objects.all().delete()
                CurrentProjectImages.objects.all().delete()
            except:
                pass
            instance = projectForm.save(commit=False)
            instance.title = request.POST.get('title')
            instance.save()
            for i in images:
                image_instance = CurrentProjectImages(image=i, title = instance)
                image_instance.save()
            return homepage(request)
        else:
            return render(request, 'pages/upload_current_project.html',
                          {'currentProjectForm': projectForm,
                           'imageForm': image_form})
    try:
        currentProject = CurrentProject.objects.get()
    except:
        currentProject = CurrentProject.objects.none()
        currentProject.title = None
        currentProject.desc = None
    return render(request, 'pages/upload_current_project.html',
                  {'currentProjectForm': CurrentProjectForm(initial={'title':currentProject.title,'desc':currentProject.desc}),
                   'imageForm': CurrentProjectImageForm()}
                  )

def upload_news(request):
    if request.method == 'POST':
        newsForm = NewsForm(request.POST)
        if newsForm.is_valid():
            newsForm.save()
            return homepage(request)
        else:
            return render(request,'pages/upload_news.html',{'newsForm':newsForm})
    else:
        return render(request,'pages/upload_news.html',{'newsForm':NewsForm()})


def upload_reviews(request):
    try:
        full_name = UserProfileInfo.objects.get(user=request.user).full_name
    except:
        full_name = None
    if request.method=='POST':
        reviewsForm = ReviewsForm(request.POST)
        if reviewsForm.is_valid():
            full_name = request.POST.get('full_name')
            #reviewsForm.save(user=request.user,full_name=full_name)
            reviewsForm.full_name=full_name
            reviewsForm.save()
            return homepage(request)
        else:
            return render(request,'pages/upload_reviews.html',{'reviewsForm':reviewsForm})
    else:
        return render(request,'pages/upload_reviews.html',
                      {'reviewsForm':ReviewsForm(initial={'full_name':full_name})})

def manage_website(request):
    return render(request,'pages/manage_website.html')