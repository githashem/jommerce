from .models import Session, AnonymousUser
from django.http import HttpRequest
from django.conf import settings


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        session_key = request.COOKIES.get(settings.AUTH_SESSION_COOKIE_NAME, None)
        try:
            session = Session.objects.get(pk=session_key)
        except Session.DoesNotExist:
            request.session = None
            request.user = AnonymousUser()
        else:
            request.session = session
            request.user = session.user
        response = self.get_response(request)

        response.set_cookie(
            settings.AUTH_SESSION_COOKIE_NAME,
            request.session.id,
            max_age=settings.AUTH_SESSION_COOKIE_AGE,
            expires=None,
            domain=settings.AUTH_SESSION_COOKIE_DOMAIN,
            path=settings.AUTH_SESSION_COOKIE_PATH,
            secure=settings.AUTH_SESSION_COOKIE_SECURE,
            httponly=settings.AUTH_SESSION_COOKIE_HTTPONLY,
            samesite=settings.AUTH_SESSION_COOKIE_SAMESITE,
        )
        return response
