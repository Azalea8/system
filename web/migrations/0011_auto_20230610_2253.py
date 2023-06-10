# Generated by Django 3.2.4 on 2023-06-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20230521_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='category',
            field=models.SmallIntegerField(choices=[(1, '读卡机'), (2, 'POS机'), (3, '热敏打印机'), (4, '打印纸'), (5, '敬老卡'), (6, '市民卡')], verbose_name='物资类别'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='category',
            field=models.SmallIntegerField(choices=[(1, '读卡机'), (2, 'POS机'), (3, '热敏打印机'), (4, '打印纸'), (5, '敬老卡'), (6, '市民卡')], verbose_name='物资类别'),
        ),
    ]