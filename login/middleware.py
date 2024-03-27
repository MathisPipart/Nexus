from django.shortcuts import redirect
from django.contrib import messages
from .adapters import EmailNotAllowedException  # Assurez-vous que le chemin d'importation est correct


class SocialAuthExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, EmailNotAllowedException):
            messages.error(request, exception.args[0])
            return redirect('/access_denied')
