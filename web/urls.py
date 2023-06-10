from django.contrib import admin
from django.urls import path
from web.views import account, list, add, edit, delete, material

urlpatterns = [
    path('', account.homepage),
    path('login/', account.login),
    path('image/code/', account.img_code),
    path('logout/', account.logout),

    path('purchase/list/', list.purchase_list),
    path('refund/list/', list.refund_list),
    path('outbound/list/', list.outbound_list),
    path('material/list/', list.material_list),
    path('vendor/list/', list.vendor_list),
    path('warehouse/list/', list.warehouse_list),

    path('purchase/add/', add.purchase_add),
    path('refund/add/', add.refund_add),
    path('outbound/add/', add.outbound_add),
    path('vendor/add/', add.vendor_add),
    path('warehouse/add/', add.warehouse_add),

    path('material/<int:nid>/edit/', edit.material_edit),
    path('purchase/<int:nid>/edit/', edit.purchase_edit),
    path('outbound/<int:nid>/edit/', edit.outbound_edit),
    path('vendor/<int:nid>/edit/', edit.vendor_edit),
    path('warehouse/<int:nid>/edit/', edit.warehouse_edit),

    path('material/delete/', delete.material_delete),
    path('purchase/delete/', delete.purchase_delete),
    path('outbound/delete/', delete.outbound_delete),
    path('vendor/delete/', delete.vendor_delete),
    path('warehouse/delete/', delete.warehouse_delete),

    path('api/material/', material.MaterialListView.as_view()),
    path('api/material/<int:pk>/', material.MaterialDetailView.as_view()),
]