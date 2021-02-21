from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from django.urls import reverse
from .forms import rehber, ekleForm,sorgulaForm,updateForm
from django.http import JsonResponse
from .models import rehber
import json

def home_wiev(request):
    return HttpResponse('<b> Anasayfaya Hoşgeldiniz </b>')

def index_wiev(request):#veritabanı kayıtlarını index sayfasında görüntüledik
    tel_rehber=rehber.objects.all()
    print(tel_rehber)
    return render(request,'rehber/index.html',{'tel_rehber':tel_rehber})

def detail_wiev(request,id):
    tel_rehber=get_object_or_404(rehber,id=id)
    context = {
        'tel_rehber': tel_rehber,
    }
    return render(request,'rehber/detail.html',context)
#POST
#VERİ TABANINA VERİ EKLEDİK
def kisi_ekle_view(request):
    if (request.method == 'POST'):
        if request.POST.get("save"):
            form = ekleForm(request.POST)
            print(request.POST.get("save"))
            if form.is_valid():
                form.save()
                #TEMİZLE BUTONU
        elif request.POST.get("clean"):
            print(request.POST.get("clean"))
            form = ekleForm()
    else:
        print("test")
        form = ekleForm()
    context = {
        'form': form
    }
    return render(request,'rehber/kisi_ekle.html',context)
   # return HttpResponse('<b>Kişi Ekle Sayfası </b>')

def connectDB():
    client = MongoClient('localhost', 27017)
    db = client["rehber"]
    # conn = db.rehber_rehber

    return client, db


# GET
# SORGULAMA
# @csrf_exempt
def kisi_sorgula_view(request):
    if request.is_ajax() and request.method == "POST":
        tel_rehber = ''
        searchText = request.POST['searchText']
        #
        client, db = connectDB()
        conn = db["rehber_rehber"]

        try:
            tel_rehber = conn.find_one({"number": int(searchText)})
            del tel_rehber["_id"]
        except:
            print("hata")
            client.close()

            tel_rehber["message"] = "Böyle bir kişi bulunamadı!!!"
            return HttpResponse(json.dumps({'results': tel_rehber}), content_type="application/json")
        #
        if not tel_rehber:
            tel_rehber["message"] = "Böyle bir kişi bulunamadı!!!"
        else:
            tel_rehber["message"] = ''
        #
        rst = {'results': tel_rehber}
        #        rst = {'results': {"id":17, "name": "Kadir Can", "surname": "Murat",
        #                           "number":"23475", "address": "test", "message": "test"}}
        client.close()
        return HttpResponse(json.dumps(rst), content_type="application/json")
        # return JsonResponse({'results': tel_rehber})
    # elif request.method == "GET" or request.method == "POST":
    return render(request, 'rehber/kisi_sorgula.html', context={'form': sorgulaForm()})


def search_tel_number(request):
    context = {
        'search': None,
    }
    if request.is_ajax():
        if request.method == 'POST':
            search_text = request.POST['search_text']
        else:
            search_text = ''

        try:
            client, db = connectDB()
            conn = db["rehber_rehber"]
            #            search = rehber.objects.filter(number__icontains=int(search_text)).first()
            search = conn.find_one({"number": int(search_text)})
            print(search)
            del search["_id"]
        except:
            pass

        context = {
            'search': search,
        }
        #        html = render_to_string('ajax_search.html',context)
        return HttpResponse(json.dumps(context), content_type="application/json")
    return render(request, 'ajax_search.html', context)




def update_wiev(request,id):
    tel_rehber = get_object_or_404(rehber, id=id)
    form = updateForm(request.POST or None,instance=tel_rehber)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request,'rehber/update.html',context)

def delete_wiev(request,id):
    tel_rehber = get_object_or_404(rehber, id=id)
    tel_rehber.delete()
    return redirect ('/rehber/index')
