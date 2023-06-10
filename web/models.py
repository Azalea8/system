from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)


class Material(models.Model):
    name = models.CharField(verbose_name='物资名称', max_length=32)
    quantity = models.IntegerField(verbose_name='物资数量')
    price = models.DecimalField(verbose_name='单价', max_digits=10, decimal_places=2, default=0.00)

    category_choices = (
        (1, '读卡机'), (2, 'POS机'), (3, '热敏打印机'),
        (4, '打印纸'), (5, '敬老卡'), (6, '市民卡'),
    )
    category = models.SmallIntegerField(verbose_name='物资类别', choices=category_choices)

    vendor = models.ForeignKey(verbose_name='供应商', to='Vendor', to_field='id', null=True, blank=True, on_delete=models.SET_NULL)

    warehouse = models.ForeignKey(verbose_name='仓库', to='Warehouse', to_field='id', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'编号{self.id} {self.name}'


class Vendor(models.Model):
    name = models.CharField(verbose_name='供应商名称', max_length=32)
    maintenance = models.CharField(verbose_name='维护方式', max_length=64)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(verbose_name='仓库名称', max_length=32)
    location = models.CharField(verbose_name='仓库位置', max_length=64)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    interior_in = models.CharField(verbose_name='内部进货人', max_length=32)
    interior_out = models.CharField(verbose_name='外部进货人', max_length=32, default='默认为空')
    quality = models.CharField(verbose_name='质检人', max_length=32)
    vendor = models.ForeignKey(verbose_name='供货商', to='Vendor', to_field='id', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(verbose_name='物资名称', max_length=32)
    price = models.DecimalField(verbose_name='进货单价', max_digits=10, decimal_places=2, default=0.00)

    category_choices = (
        (1, '读卡机'), (2, 'POS机'), (3, '热敏打印机'),
        (4, '打印纸'), (5, '敬老卡'), (6, '市民卡'),
    )
    category = models.SmallIntegerField(verbose_name='物资类别', choices=category_choices)

    quantity = models.IntegerField(verbose_name='物资数量')
    date = models.DateField(verbose_name='入库日期')
    comment = models.CharField(verbose_name='备注', max_length=64)


class Refund(models.Model):
    material = models.ForeignKey(verbose_name='物资名称', to='Material', to_field='id', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(verbose_name='物资名称', max_length=32)
    quantity = models.IntegerField(verbose_name='退货数量')
    return_in = models.CharField(verbose_name='内部退货人', max_length=32)
    return_out = models.CharField(verbose_name='外部退货人', max_length=32, default='默认为空')
    quality = models.CharField(verbose_name='质检人', max_length=32)
    vendor = models.CharField(verbose_name='供货商', max_length=32)
    comment = models.CharField(verbose_name='备注', max_length=64)


class Outbound(models.Model):
    material = models.ForeignKey(verbose_name='物资名称', to='Material', to_field='id', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(verbose_name='物资名称', max_length=32)
    date = models.DateField(verbose_name='出库日期')
    outbound_quantity = models.IntegerField(verbose_name='出库数量')

    comment = models.CharField(verbose_name='备注', max_length=64)
































