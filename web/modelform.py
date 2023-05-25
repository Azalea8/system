from web.models import *
from django import forms

class Bootstrap_model_form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if 'class' not in field.widget.attrs.keys():
                field.widget.attrs['class'] = 'form-control'
            if 'placeholder' not in field.widget.attrs.keys():
                field.widget.attrs['placeholder'] = field.label

class VendorModelForm(Bootstrap_model_form):
    class Meta:
        model = Vendor
        fields = '__all__'
        widgets = {

        }

class WarehouseModelForm(Bootstrap_model_form):
    class Meta:
        model = Warehouse
        fields = '__all__'
        widgets = {

        }

class PurchaseModelForm(Bootstrap_model_form):

    class Meta:
        model = Purchase
        fields = ['name', 'quantity', 'category', 'price', 'vendor', 'interior_in',
                  'interior_out', 'quality', 'date', 'comment']
        widgets = {

        }

class RefundModelForm(Bootstrap_model_form):
    class Meta:
        model = Refund
        fields = ['material', 'quantity', 'return_in', 'return_out',
                  'quality', 'comment']
        widgets = {

        }

class MaterialModelForm(Bootstrap_model_form):

    class Meta:
        model = Material
        fields = '__all__'
        widgets={

        }

class OutboundModelForm(Bootstrap_model_form):

    class Meta:
        model = Outbound
        fields = ['material', 'outbound_quantity', 'date', 'comment']
        widgets={

        }













