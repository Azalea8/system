from django.shortcuts import render, HttpResponse, redirect
from web.models import *
from web.modelform import *
from django import forms
from system.utils.plugins import Pagination, md5


# Create your views here.

def material_list(request):
    formset = PurchaseModelForm()
    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['name__contains'] = search_data

    data_list = Material.objects.filter(**data_dict)
    page_object = Pagination(request, data_all_list=data_list, page_size=10)

    context = {
        'data_list': page_object.data_list,
        'search_data': search_data,
        'formset': formset,
        'page_string': page_object.html(),
    }

    return render(request, 'material_list.html', context)

def vendor_list(request):
    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['name__contains'] = search_data

    data_list = Vendor.objects.filter(**data_dict)
    page_object = Pagination(request, data_all_list=data_list)

    context = {
        'data_list': page_object.data_list,
        'search_data': search_data,

        'page_string': page_object.html()
    }

    return render(request, 'vendor_list.html', context)


def warehouse_list(request):

    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['name__contains'] = search_data

    data_list = Warehouse.objects.filter(**data_dict)
    page_object = Pagination(request, data_all_list=data_list)

    context = {
        'data_list': page_object.data_list,
        'search_data': search_data,

        'page_string': page_object.html()
    }

    return render(request, 'warehouse_list.html', context)

def purchase_list(request):
    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['name__contains'] = search_data

    data_list = Purchase.objects.filter(**data_dict)
    page_object = Pagination(request, data_all_list=data_list)

    context = {
        'data_list': page_object.data_list,
        'search_data': search_data,

        'page_string': page_object.html(),
    }

    return render(request, 'purchase_list.html', context)

def refund_list(request):
    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['name__contains'] = search_data

    data_list = Refund.objects.filter(**data_dict)
    page_object = Pagination(request, data_all_list=data_list)

    context = {
        'data_list': page_object.data_list,

        'search_data': search_data,
        'page_string': page_object.html()
    }
    return render(request, 'refund_list.html', context)

def outbound_list(request):
    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['name__contains'] = search_data

    data_list = Outbound.objects.filter(**data_dict)
    page_object = Pagination(request, data_all_list=data_list)

    context = {
        'data_list': page_object.data_list,
        'search_data': search_data,

        'page_string': page_object.html(),
    }

    return render(request, 'outbound_list.html', context)

