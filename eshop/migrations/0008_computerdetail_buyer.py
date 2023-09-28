# Generated by Django 4.2.1 on 2023-07-26 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0007_order_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='computerdetail',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eshop.customer'),
        ),
    ]