from django.http.response import JsonResponse, HttpResponse
from django.views import View
from web.models import *
import json



class MaterialListView(View):
    """列表视图"""
    def get(self, request):
        """查询所有"""
        materials = Material.objects.all()
        materials_list = []
        for material in materials:
            material_dict = {
                'id': material.id,
                'name': material.name,
                'quantity': material.quantity,
                'price': material.price,
                'category': material.get_category_display(),
                'vendor': material.vendor.name,
                'warehouse': material.warehouse.name,
            }
            materials_list.append(material_dict)
        return JsonResponse(materials_list, safe=False)


    def post(self, request):
        """新增一条"""
        json_str_bytes = request.body
        json_str = json_str_bytes.decode()
        material_dict = json.loads(json_str)

        material = Material(
            name=material_dict['name'],
            quantity=material_dict['quantity'],
            price=material_dict['price'],
            category=material_dict['category'],
            vendor_id=material_dict['vendor_id'],
            warehouse_id=material_dict['warehouse_id']
        )
        material.save()

        material_dict = {
            'id': material.id,
            'name': material.name,
            'quantity': material.quantity,
            'price': material.price,
            'category': material.get_category_display(),
            'vendor': material.vendor.name,
            'warehouse': material.warehouse.name,
        }
        return JsonResponse(material_dict, status=201)


class MaterialDetailView(View):
    """详情视图"""
    def get(self, request, pk):
        """查询指定一条数据"""
        try:
            material = Material.objects.filter(id=pk).get()
        except Material.DoesNotExist:
            return JsonResponse({'message': '查询的数据不存在'}, status=404)
        material_dict = {
            'id': material.id,
            'name': material.name,
            'quantity': material.quantity,
            'price': material.price,
            'category': material.get_category_display(),
            'vendor': material.vendor.name,
            'warehouse': material.warehouse.name,
        }
        return JsonResponse(material_dict)

    def put(self, request, pk):
        """修改指定一条数据"""
        try:
            material = Material.objects.filter(id=pk).get()
        except Material.DoesNotExist:
            return JsonResponse({'message': '查询的数据不存在'}, status=404)

        json_str_bytes = request.body
        json_str = json_str_bytes.decode()
        material_dict = json.loads(json_str)

        material.name = material_dict['name']
        material.quantity = material_dict['quantity']
        material.price = material_dict['price']
        material.category = material_dict['category']
        material.vendor_id = material_dict['vendor_id']
        material.warehouse_id = material_dict['warehouse_id']
        material.save()

        material_dict = {
            'id': material.id,
            'name': material.name,
            'quantity': material.quantity,
            'price': material.price,
            'category': material.get_category_display(),
            'vendor': material.vendor.name,
            'warehouse': material.warehouse.name,
        }
        return JsonResponse(material_dict)

    def delete(self, request, pk):
        """删除指定一条数据"""
        try:
            material = Material.objects.filter(id=pk).get()
        except Material.DoesNotExist:
            return JsonResponse({'message': '查询的数据不存在'}, status=404)
        material.delete()
        return HttpResponse(status=204)