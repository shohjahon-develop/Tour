from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from blog.forms import *
from blog.models import *
from django.db.models import Q


# Create your views here.

def index(request):
    tips = Tips.objects.all()
    dir = Direct.objects.all()
    ned = Your_emailForms(request.POST or None)
    if request.method == "POST" and ned.is_valid():
        ned.save()
        return HttpResponse(
            "      <h2>Obunangiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/>"
            "<h2> Ishonchingiz uchun raxmat ")
    context = {
        "tips":tips,
        "dir":dir
    }
    return render(request,'index.html',context)


def foods(request):
    food = Food.objects.all()
    ned = Your_emailForms(request.POST or None)
    if request.method == "POST" and ned.is_valid():
        ned.save()
        return HttpResponse(
            "      <h2>Obunangiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/>"
            "<h2> Ishonchingiz uchun raxmat ")
    context = {
        "food":food
    }
    return render(request,"detail_pages/foods.html",context)

def medical(request):
    med = Medical.objects.all()
    ned = Your_emailForms(request.POST or None)
    if request.method == "POST" and ned.is_valid():
        ned.save()
        return HttpResponse(
            "      <h2>Obunangiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/>"
            "<h2> Ishonchingiz uchun raxmat ")
    context = {
        "med":med
    }
    return render(request,"detail_pages/medical.html",context)


def services(request):
    ser = Services.objects.all()
    ned = Your_emailForms(request.POST or None)
    if request.method == "POST" and ned.is_valid():
        ned.save()
        return HttpResponse(
            "      <h2>Obunangiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/>"
            "<h2> Ishonchingiz uchun raxmat ")
    context = {
        "ser":ser
    }
    return render(request,"detail_pages/services.html",context)

def jobs(request):
    job = Jobs.objects.all()
    ned = Your_emailForms(request.POST or None)
    if request.method == "POST" and ned.is_valid():
        ned.save()
        return HttpResponse(
            "      <h2>Obunangiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/>"
            "<h2> Ishonchingiz uchun raxmat ")
    context = {
        'job':job
    }
    return render(request,"detail_pages/jobs.html",context)


def auto(request):
    avto = Automotive.objects.all()
    ned = Your_emailForms(request.POST or None)
    if request.method == "POST" and ned.is_valid():
        ned.save()
        return HttpResponse(
            "      <h2>Obunangiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/>"
            "<h2> Ishonchingiz uchun raxmat ")
    context = {
        'avto':avto
    }
    return render(request,"detail_pages/auto.html",context)

def hotel(request):
    hotels = Hotel.objects.all()
    ned = Your_emailForms(request.POST or None)
    if request.method == "POST" and ned.is_valid():
        ned.save()
        return HttpResponse(
            "      <h2>Obunangiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/>"
            "<h2> Ishonchingiz uchun raxmat ")
    context = {
        'hotels':hotels
    }
    return render(request,"detail_pages/hotels.html",context)

def shopping(request):
    shop = Shopping.objects.all()
    ned = Your_emailForms(request.POST or None)
    if request.method == "POST" and ned.is_valid():
        ned.save()
        return HttpResponse(
            "      <h2>Obunangiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/>"
            "<h2> Ishonchingiz uchun raxmat ")
    context = {
        'shop':shop
    }
    return render(request,"detail_pages/shop.html",context)

def dir_detail(request, pk):
    dir = get_object_or_404(Direct, pk=pk)
    comments2 = dir.comments_2.all()  # Tipsga oid barcha izohlar
    return render(request, 'detail_pages/direct_Detail.html', {'dir': dir, 'comments2': comments2})

@login_required
def add_comment_2(request, dir_id):
    dir = get_object_or_404(Direct, id=dir_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if not text:
            return HttpResponseForbidden("Izoh bo'sh bo'lishi mumkin emas!")

        # Izohni yaratish
        D_comment.objects.create(
            dir=dir,
            user=request.user,
            text=text
        )
        return redirect('dir_detail', pk=dir.id)  # Izoh qo'shilgandan keyin tips_detail sahifasiga qaytish

    return HttpResponseForbidden("Boshqa metodda ruxsat berilmagan.")











def tips_detail(request, pk):
    tips = get_object_or_404(Tips, pk=pk)
    comments = tips.comments.all()  # Tipsga oid barcha izohlar
    return render(request, 'comments_detail_page/tips_detail.html', {'tips': tips, 'comments': comments})


# Izoh qo'shish
@login_required
def add_comment(request, tips_id):
    tips = get_object_or_404(Tips, id=tips_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if not text:
            return HttpResponseForbidden("Izoh bo'sh bo'lishi mumkin emas!")

        # Izohni yaratish
        Comment.objects.create(
            tips=tips,
            user=request.user,
            text=text
        )
        return redirect('tips_detail', pk=tips.id)  # Izoh qo'shilgandan keyin tips_detail sahifasiga qaytish

    return HttpResponseForbidden("Boshqa metodda ruxsat berilmagan.")
























def search_view(request):
    query = request.GET.get('q', '')  # URL'dan qidiruv so'zini olamiz
    tips = Tips.objects.filter(name__icontains=query)
    directs = Direct.objects.filter(name__icontains=query)
    foods = Food.objects.filter(name__icontains=query)
    medicals = Medical.objects.filter(name__icontains=query)
    services = Services.objects.filter(name__icontains=query)
    shoppings = Shopping.objects.filter(name__icontains=query)
    hotels = Hotel.objects.filter(name__icontains=query)

    context = {
        'query': query,
        'tips': tips,
        'directs': directs,
        'foods': foods,
        'medicals': medicals,
        'services': services,
        'shoppings': shoppings,
        'hotels': hotels,
    }
    return render(request, 'search/search_results.html', context)







































































































