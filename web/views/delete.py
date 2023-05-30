from django.shortcuts import render, HttpResponse, redirect
from web.models import *
from django import forms
from system.utils.plugins import Pagination, md5
import json

def vendor_delete(request, nid):
    Vendor.objects.filter(id=nid).delete()
    return redirect('/vendor/list/')

def warehouse_delete(request, nid):
    Warehouse.objects.filter(id=nid).delete()
    return redirect('/warehouse/list')

def material_delete(request):
    nid = request.GET.get('nid')
    Material.objects.filter(id=nid).delete()
    data_dict = {'status': True, }
    return HttpResponse(json.dumps(data_dict))

def purchase_delete(request, nid):
    Purchase.objects.filter(id=nid).delete()
    return redirect('/purchase/list/')

def outbound_delete(request, nid):
    Outbound.objects.filter(id=nid).delete()
    return redirect('/outbound/list/')