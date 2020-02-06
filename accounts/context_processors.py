from .models import UserProfileInfo

def account_processor(request):
    try:
        if request.user.is_authenticated:
            account = UserProfileInfo.objects.get(user=request.user)
        else:
            account = UserProfileInfo.objects.none()
    except:
        account = UserProfileInfo.objects.none()
    return ({'account':account})