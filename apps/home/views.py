from datetime import datetime

from django.shortcuts import render
import json
import os
from zap.settings import STATIC_DIR
from django.core.paginator import Paginator
from django.views.generic import DetailView


def home(request):
    return render(request, "home/index.html")


def homezap(request):
    json_data = open(os.path.join(STATIC_DIR, 'data.json'), encoding="utf8")
    data1 = json.load(json_data)
    json_data.close()
    zap = []
    minlon = -46.693419
    minlat = 23.568704
    maxlon = -46.641146
    maxlat = -23.546686
    for i in data1:
        try:
            if i['address']['geoLocation']['location']['lat'] != 0 \
                    and i['address']['geoLocation']['location']['lon'] != 0:
                if i['pricingInfos']['businessType'] == 'RENTAL' \
                        and int(i['pricingInfos']['rentalTotalPrice']) >= 3500 \
                        or i['pricingInfos']['businessType'] == 'SALE' \
                        and int(i['pricingInfos']['price']) >= 600000:
                    if minlat >= float(i['address']['geoLocation']['location']['lat']) <= maxlat \
                            and minlon >= float(i['address']['geoLocation']['location']['lon']) <= maxlon:
                        if i['usableAreas'] != 0 and (int(i['pricingInfos']['price']) / int(i['usableAreas'])) >= (3500*0,90):
                            zap.append(i)
                    else:
                        if i['usableAreas'] != 0 and (int(i['pricingInfos']['price']) / int(i['usableAreas'])) >= 3500:
                            zap.append(i)
        except:
            pass
    zap_page = Paginator(zap, 20)
    page_number = request.GET.get('page')
    zap = zap_page.get_page(page_number)
    return render(request, "home/include/zap.html", {'zap': zap})


def homeviva(request):
    json_data = open(os.path.join(STATIC_DIR, 'data.json'), encoding="utf8")
    data1 = json.load(json_data)
    json_data.close()
    vivareal = []
    minlon = -46.693419
    minlat = 23.568704
    maxlon = -46.641146
    maxlat = -23.546686
    for i in data1:
        try:
            if i['address']['geoLocation']['location']['lat'] != 0 \
                    and i['address']['geoLocation']['location']['lon'] != 0:
                if i['pricingInfos']['businessType'] == 'RENTAL' and \
                        int(i['pricingInfos']['rentalTotalPrice']) <= 4000 \
                        or i['pricingInfos']['businessType'] == 'SALE' \
                        and int(i['pricingInfos']['price']) <= 700000:
                    if minlat >= float(i['address']['geoLocation']['location']['lat']) <= maxlat \
                            and minlon >= float(i['address']['geoLocation']['location']['lon']) <= maxlon:
                        if i['pricingInfos']['monthlyCondoFee'].isdigit() and int(
                                i['pricingInfos']['monthlyCondoFee']) < (int(i['pricingInfos']['rentalTotalPrice']) * 0.50):
                            vivareal.append(i)
                    else:
                        if i['pricingInfos']['monthlyCondoFee'].isdigit() and int(
                                i['pricingInfos']['monthlyCondoFee']) < (int(i['pricingInfos']['rentalTotalPrice']) * 0.30):
                            vivareal.append(i)
        except:
            pass
    viva_page = Paginator(vivareal, 20)
    page_number = request.GET.get('page')
    vivareal = viva_page.get_page(page_number)
    return render(request, "home/include/vivareal.html", {'vivareal': vivareal})


def imoveldetail(request, pk=None):
    json_data = open(os.path.join(STATIC_DIR, 'data.json'), encoding="utf8")
    data1 = json.load(json_data)
    json_data.close()
    detail = None
    vivareal = None
    for i in data1:
        if i['id'] == pk:
            detail = i
    date = datetime.strptime(i['createdAt'], "%Y-%m-%dT%H:%M:%S.%fZ")
    if request.get_full_path().split('/')[1] == 'vivareal':
        vivareal = True
    return render(request, "home/detail.html", {'detail': detail, 'createdAt': date, 'vivareal': vivareal})
