from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


@login_required
def vueProfil(request):
    return render(request, "profil.html")


@require_POST
@login_required
def reset_calendar_url(request):
    if request.user.is_authenticated:
        user_profile = request.user.userprofile
        user_profile.url = ''
        user_profile.save()
        return JsonResponse({'status': 'success', 'message': 'URL reset successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'User not authenticated'}, status=401)

