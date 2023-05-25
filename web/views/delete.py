from django.shortcuts import render, HttpResponse, redirect
from web.models import *
from django import forms
from system.utils.plugins import Pagination, md5

def vendor_delete(request, nid):
    Vendor.objects.filter(id=nid).delete()
    return redirect('/vendor/list/')

def warehouse_delete(request, nid):
    Warehouse.objects.filter(id=nid).delete()
    return redirect('/warehouse/list')

def material_delete(request, nid):
    Material.objects.filter(id=nid).delete()
    return redirect('/material/list/')

def purchase_delete(request, nid):
    Purchase.objects.filter(id=nid).delete()
    return redirect('/purchase/list/')

def outbound_delete(request, nid):
    Outbound.objects.filter(id=nid).delete()
    return redirect('/outbound/list/')