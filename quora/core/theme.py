from django.conf import settings as django_settings

def site_settings(request):
    return {'SITE_TITLE': django_settings.SITE_TITLE}
