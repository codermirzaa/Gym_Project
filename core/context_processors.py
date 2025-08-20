# from about.models import About
from core.models import  SiteSettings
# from services.models import ServiceDetailPage


def navbar_footer_menu(request):

    context = {
        'site_settings': SiteSettings.objects.last() if SiteSettings.objects.last() else None,

        # 'services': ServiceDetailPage.objects.all(),

        # 'about': About.objects.last(),
    }

    return context