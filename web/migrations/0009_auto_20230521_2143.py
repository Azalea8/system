# Generated by Django 3.2.4 on 2023-05-21 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_refund'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refund',
            name='return_out',
            field=models.CharField(default='默认为空', max_length=32, verbose_name='外部退货人'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='vendor',
            field=models.CharField(default=1, max_length=32, verbose_name='供货商'),
            preserve_default=False,
        ),
    ]