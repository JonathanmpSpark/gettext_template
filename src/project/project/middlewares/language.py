# -*- encoding: utf-8 -*-

from django.utils import translation
from django.conf import settings
from django.utils import timezone
import pytz
from django.utils.deprecation import MiddlewareMixin

class SubdomainLanguageMiddleware(MiddlewareMixin):
    """
    Set the language for the site based on the prefix url on the request.path
    is being served on. For example, serving on 'localhost.com/es/account/login' would
    make the language Spanish (es).
    """
    language_codes = [l[0] for l in settings.LANGUAGES]
    lang = settings.LANGUAGE_CODE

    def process_request(self, request):
        try:
            url_lang = request.path_info.split('/')[1]
            if url_lang in self.language_codes:
                self.lang = url_lang
        except IndexError:
            pass
        request.session['django_timezone'] = 'Asia/Jakarta'
        print(pytz.timezone('Asia/Jakarta'))
        print(pytz.timezone('Asia/Jakarta'))
        print(pytz.timezone('Asia/Jakarta'))
        print(pytz.timezone('Asia/Jakarta'))
        timezone.activate(pytz.timezone('Asia/Jakarta'))
        if self.lang:
            translation.activate(self.lang)
            request.LANGUAGE_CODE = self.lang
    
            