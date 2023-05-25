# Generated by Django 3.2.4 on 2023-05-21 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interior_in', models.CharField(max_length=32, verbose_name='内部进货人')),
                ('interior_out', models.CharField(default='默认为空', max_length=32, verbose_name='外部进货人')),
                ('quality', models.CharField(max_length=32, verbose_name='质检人')),
                ('name', models.CharField(max_length=32, verbose_name='物资名称')),
                ('quantity', models.IntegerField(verbose_name='物资数量')),
                ('comment', models.CharField(max_length=64, verbose_name='备注')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.vendor', verbose_name='供货商')),
            ],
        ),
        migrations.CreateModel(
            name='Outbound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outbound_date', models.DateField(verbose_name='出库日期')),
                ('outbound_quantity', models.IntegerField(verbose_name='出库数量')),
                ('comment', models.CharField(max_length=64, verbose_name='备注')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.material', verbose_name='物资名称')),
            ],
        ),
    ]
