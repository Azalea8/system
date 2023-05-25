from django.shortcuts import render, HttpResponse, redirect

from system.utils.plugins import Pagination, md5
from web.modelform import *

# Create your views here.

def vendor_edit(request, nid):
    obj = Vendor.objects.filter(id=nid).first()

    if request.method == 'GET':
        formset = VendorModelForm(instance=obj)
        return render(request, 'form.html', {'formset': formset, 'title': '编辑供应商'})

    formset = VendorModelForm(data=request.POST, instance=obj)
    if formset.is_valid():
        formset.save()
        return redirect('/vendor/list/', {'formset': formset, 'title': '编辑供应商'})
    else:
        return render(request, 'form.html', {'formset': formset, 'title': '编辑供应商'})

def warehouse_edit(request, nid):
    obj = Warehouse.objects.filter(id=nid).first()

    if request.method == 'GET':
        formset = WarehouseModelForm(instance=obj)
        return render(request, 'form.html', {'formset': formset, 'title': '编辑仓库'})

    formset = WarehouseModelForm(data=request.POST, instance=obj)
    if formset.is_valid():
        formset.save()
        return redirect('/warehouse/list/')
    else:
        return render(request, 'form.html', {'formset': formset, 'title': '编辑仓库'})

def material_edit(request, nid):

    obj = Material.objects.filter(id=nid).first()

    if request.method == 'GET':
        formset = MaterialModelForm(instance=obj)
        return render(request, 'form.html', {'formset': formset, 'title': '编辑物资'})

    formset = MaterialModelForm(data=request.POST, instance=obj)
    if formset.is_valid():
        formset.save()
        return redirect('/material/list/')
    else:
        return render(request, 'form.html', {'formset': formset, 'title': '编辑物资'})

def purchase_edit(request, nid):
    obj = Purchase.objects.filter(id=nid).first()

    if request.method == 'GET':
        formset = PurchaseModelForm(instance=obj)
        return render(request, 'form.html', {'formset': formset, 'title': '编辑进货单'})

    formset =  PurchaseModelForm(data=request.POST, instance=obj)
    if formset.is_valid():
        formset.save()
        return redirect('/purchase/list/')
    else:
        return render(request, 'form.html', {'formset': formset, 'title': '编辑进货单'})

def outbound_edit(request,nid):
    obj = Outbound.objects.filter(id=nid).first()

    if request.method == 'GET':
        formset = OutboundModelForm(instance=obj)
        return render(request, 'form.html', {'formset': formset, 'title': '编辑进货单'})

    formset = OutboundModelForm(data=request.POST, instance=obj)
    if formset.is_valid():
        formset.save()
        return redirect('/outbound/list/')
    else:
        return render(request, 'form.html', {'formset': formset, 'title': '编辑进货单'})