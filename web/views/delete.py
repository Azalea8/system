from django.shortcuts import render, HttpResponse, redirect
from web.models import *
from django import forms
from system.utils.plugins import Pagination, md5
import json

def vendor_delete(request):
    nid = request.GET.get('nid')
    Vendor.objects.filter(id=nid).delete()
    data_dict = {'status': True, }
    return HttpResponse(json.dumps(data_dict))

def warehouse_delete(request):
    nid = request.GET.get('nid')
    Warehouse.objects.filter(id=nid).delete()
    data_dict = {'status': True, }
    return HttpResponse(json.dumps(data_dict))

def material_delete(request):
    nid = request.GET.get('nid')
    Material.objects.filter(id=nid).delete()
    data_dict = {'status': True, }
    return HttpResponse(json.dumps(data_dict))

def purchase_delete(request):
    nid = request.GET.get('nid')
    Purchase.objects.filter(id=nid).delete()
    data_dict = {'status': True, }
    return HttpResponse(json.dumps(data_dict))

def outbound_delete(request):
    nid = request.GET.get('nid')
    Outbound.objects.filter(id=nid).delete()
    data_dict = {'status': True, }
    return HttpResponse(json.dumps(data_dict))