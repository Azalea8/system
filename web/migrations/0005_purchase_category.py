# Generated by Django 3.2.4 on 2023-05-21 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20230521_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='category',
            field=models.SmallIntegerField(choices=[(1, '读卡机'), (2, 'POS机'), (3, '热敏打印机'), (4, '打印纸'), (5, '敬老卡'), (6, '市民卡'), (7, '王者荣耀皮肤')], default=7, verbose_name='物资类别'),
            preserve_default=False,
        ),
    ]
