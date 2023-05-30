from django.shortcuts import render, HttpResponse, redirect
from system.utils.plugins import Pagination, md5
from web.modelform import *
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
# 免除csrf_tokens检测
def vendor_add(request):
    # if request.method == 'GET':
    #     formset = VendorModelForm()
    #     return render(request, 'form.html', {'formset': formset})

    formset = VendorModelForm(data=request.POST)
    if formset.is_valid():
        formset.save()
        data_dict = {'status': True, }
        return HttpResponse(json.dumps(data_dict))
    else:
        data_dict = {'status': False, 'errors': formset.errors}
        return HttpResponse(json.dumps(data_dict))

@csrf_exempt
# 免除csrf_tokens检测
def warehouse_add(request):
    # if request.method == 'GET':
    #     formset = WarehouseModelForm()
    #     return render(request, 'form.html', {'formset': formset})

    formset = WarehouseModelForm(data=request.POST)
    if formset.is_valid():
        formset.save()
        data_dict = {'status': True, }
        return HttpResponse(json.dumps(data_dict))
    else:
        data_dict = {'status': False, 'errors': formset.errors}
        return HttpResponse(json.dumps(data_dict))

@csrf_exempt
# 免除csrf_tokens检测
def purchase_add(request):
    # if request.method == 'GET':
    #     formset = PurchaseModelForm()
    #     return render(request, 'form.html', {'formset': formset, 'title': '进货单'})

    formset  = PurchaseModelForm(data=request.POST)
    if formset.is_valid():
        data = formset.cleaned_data
        material_data = {}

        material_data['name'] = data.get('name')
        material_data['category'] = data.get('category')
        material_data['vendor'] = data.get('vendor')
        tmp = data.get('quantity')
        if Material.objects.filter(**material_data).exists():
            tmp += Material.objects.filter(**material_data).first().quantity
            Material.objects.filter(**material_data).update(quantity=tmp)
            material_data['quantity'] = data.get('quantity')
        else:
            material_data['quantity'] = data.get('quantity')
            Material.objects.create(**material_data)
        formset.save()
        data_dict = {'status': True, }
        return HttpResponse(json.dumps(data_dict))
    else:
        data_dict = {'status': False, 'errors': formset.errors}
        return HttpResponse(json.dumps(data_dict))

@csrf_exempt
# 免除csrf_tokens检测
def refund_add(request):
    # if request.method == 'GET':
    #     formset = RefundModelForm()
    #     return render(request, 'form.html', {'formset': formset, 'title': '退货单'})

    formset = RefundModelForm(data=request.POST)
    if formset.is_valid():
        data = formset.cleaned_data
        nid = data.get('material').id
        tmp = data.get('quantity')
        tmp = Material.objects.filter(id=nid).first().quantity - tmp
        if tmp < 0:
            formset.add_error('quantity', '再退货就为负了>-<')
            data_dict = {'status': False, 'errors': formset.errors}
            return HttpResponse(json.dumps(data_dict))

        Material.objects.filter(id=nid).update(quantity=tmp)
        formset.save()
        name = data.get('material').name
        vendor = data.get('material').vendor.name
        nid = Refund.objects.last().id
        Refund.objects.filter(id=nid).update(name=name, vendor=vendor)

        data_dict = {'status': True, }
        return HttpResponse(json.dumps(data_dict))
    else:
        data_dict = {'status': False, 'errors': formset.errors}
        return HttpResponse(json.dumps(data_dict))

# 免除csrf_tokens检测
@csrf_exempt
# 免除csrf_tokens检测
def outbound_add(request):
    # if request.method == 'GET':
    #     formset = OutboundModelForm()
    #     return render(request, 'form.html', {'formset': formset, 'title': '出库单'})

    formset = OutboundModelForm(data=request.POST)
    if formset.is_valid():
        data = formset.cleaned_data
        tmp = data.get('outbound_quantity')
        nid = data.get('material').id
        tmp = Material.objects.filter(id=nid).first().quantity - tmp
        if tmp < 0:
            formset.add_error('outbound_quantity', '再出库就为负了>-<')
            data_dict = {'status': False, 'errors': formset.errors}
            return HttpResponse(json.dumps(data_dict))

        Material.objects.filter(id=nid).update(quantity=tmp)
        formset.save()
        name = data.get('material').name
        nid = Outbound.objects.last().id
        Outbound.objects.filter(id=nid).update(name=name)

        data_dict = {'status': True,}
        return HttpResponse(json.dumps(data_dict))
    else:
        data_dict = {'status': False, 'errors': formset.errors}
        return HttpResponse(json.dumps(data_dict))