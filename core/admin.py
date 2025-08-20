# Register your models here.
# trainers/admin.py
from django.contrib import admin
from .models import Trainer ,ContactInfo, SiteSettings ,ContactUs
from core.models import AboutSection, WhyUs, CarouselSlide, ContactInfo, SiteSettings






@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name",)

from .models import AboutSection

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_read_more')

from .models import WhyUs

@admin.register(WhyUs)
class WhyUsAdmin(admin.ModelAdmin):
    list_display = ('title',)

from .models import CarouselSlide

@admin.register(CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ('title',)



# @admin.register(ContactUs)
# class ContactUsAdmin(admin.ModelAdmin):
#     list_display = ("name", "email", "number", "message")
#     search_fields = ("name", "email", "number", "message") 
      

admin.site.register(SiteSettings)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "number", "message")  # short_message çıxarıldı
    search_fields = ("name", "email", "number", "message")