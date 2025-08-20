# Create your models here.
# trainers/models.py
from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="trainers/")
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name




class AboutSection(models.Model):
    title = models.CharField(max_length=200, default="HEALTHY MIND, HEALTHY BODY")
    content = models.TextField()
    show_read_more = models.BooleanField(default=False)

    def __str__(self):
        return self.title


WHYUS_IMAGE_CHOICES = [
    ("u-1.png", "Quality Equipment"),
    ("u-4.png", "Nutrition"),
    ("u-2.png", "Healthy Diet Plan"),
    ("u-3.png", "Sport Training"),
]

class WhyUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(
        max_length=50,
        choices=WHYUS_IMAGE_CHOICES,
        default="u-1.png"
    )

    def __str__(self):
        return self.title

    def image_url(self):
        return f"images/{self.image}"

class CarouselSlide(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    headline = models.CharField(max_length=100, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    




CONTACT_ICON_CHOICES = [
    ("icon1.png", "Location"),
    ("icon2.png", "Phone"),
    ("icon3.png", "Email"),
]

class ContactInfo(models.Model):
    text = models.CharField(max_length=255)  
    icon = models.CharField(
        max_length=50,
        choices=CONTACT_ICON_CHOICES,
        default="icon1.png"
    )
class ContactInfo(models.Model):
    text = models.CharField(max_length=255)  
    icon = models.CharField(
        max_length=50,
        choices=CONTACT_ICON_CHOICES,
        default="icon1.png"
    )

    def __str__(self):
        return self.text

    def icon_url(self):
        return f"images/{self.icon}"
    def __str__(self):
        return self.text

    def icon_url(self):
        return f"images/{self.icon}"

class SiteSettings(models.Model):
    company_name = models.CharField(max_length=100, null=True, blank=True)
    logo_navbar = models.FileField(upload_to='core/site_settings',
                                   null=True, blank=True)

    logo_navbar_alt_data = models.CharField(max_length=255, null=True, blank=True,
                                            help_text='Add data for increasing SEO performance')

    logo_footer = models.FileField(upload_to='core/site_settings',
                                   null=True, blank=True)
    footer_title = models.CharField(max_length=255, null=True, blank=True)
    footer_subtitle = models.CharField(max_length=255, null=True, blank=True)

    logo_footer_alt_data = models.CharField(max_length=255, null=True, blank=True,
                                            help_text='Add data for increasing SEO performance')

    favicon = models.FileField(upload_to='core/site_settings', null=True, blank=True)
    favicon_alt_data = models.CharField(max_length=255, null=True, blank=True,
                                        help_text='Add data for increasing SEO performance')

    address = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.DecimalField(max_digits=17, decimal_places=15, null=True, blank=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=15, null=True, blank=True)
    iframe = models.TextField(help_text="Just paste iframe src data from googlemap", null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True,
                                    help_text='Enter phone number starting with the code')

    fax = models.CharField(max_length=255, null=True, blank=True,
                                    help_text='Enter fax number starting with the code')

    facebook = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your facebook url')
    instagram = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your instagram url')
    twitter = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your twitter url')
    linkedin = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your linkedin url')
    youtube = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your youtube url')
    website = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your website url')


    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name_plural = "Site Settings"



class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.message[:50]}{'...' if len(self.message) > 50 else ''}"