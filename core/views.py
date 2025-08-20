from django.shortcuts import render
from .models import Trainer
from .models import AboutSection
from .models import WhyUs
from .models import CarouselSlide
from .models import ContactInfo
from .models import ContactUs
from django.contrib import messages



# Create your views here.
def home(request):
    trainers = Trainer.objects.all()
    about = AboutSection.objects.first()
    whyus_list = WhyUs.objects.all()
    slides = CarouselSlide.objects.all()
    contact_infos = ContactInfo.objects.all()
    success = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("message")

        if name and email and number and message:
            ContactUs.objects.create(
                name=name,
                email=email,
                number=number,
                message=message
            )
            success = True
            messages.success(request, "Mesajınız uğurla göndərildi ")
        else:
            messages.error(request, "Bütün sahələri doldurun ")

    return render(request, "index.html", {
        "trainers": trainers,
        "about": about,
        "whyus_list": whyus_list,
        "slides": slides,
        "contact_infos": contact_infos,
        "success": success,
        "name": request.POST.get("name", ""),
        "email": request.POST.get("email", ""),
        "number": request.POST.get("number", ""),
        "message": request.POST.get("message", "")
    })
def trainer(request):
    contact_infos = ContactInfo.objects.all()
    trainers = Trainer.objects.all()
    return render(request, "trainer.html", {"trainers": trainers , "contact_infos": contact_infos})
def contact(request):
    contact_infos = ContactInfo.objects.all()
    success = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("message")

        if name and email and number and message:
            ContactUs.objects.create(
                name=name,
                email=email,
                number=number,
                message=message
            )
            success = True
            messages.success(request, "Mesajınız uğurla göndərildi ")
        else:
            messages.error(request, "Bütün sahələri doldurun ")

    return render(request, "contact.html", {
        "contact_infos": contact_infos,
        "success": success,
        "name": request.POST.get("name", ""),
        "email": request.POST.get("email", ""),
        "number": request.POST.get("number", ""),
        "message": request.POST.get("message", "")
    })
    
def why(request):
    contact_infos = ContactInfo.objects.all()
    whyus_list = WhyUs.objects.all()
    return render(request, "why.html", {"whyus_list": whyus_list , "contact_infos": contact_infos})
