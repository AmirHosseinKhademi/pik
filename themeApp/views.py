from django.shortcuts import render

def profile_view(request):
    print('test')
    return render(request, 'Profile.html')
