# Generated by Django 2.2.2 on 2019-06-17 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0008_auto_20190617_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cityID',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='planner.CITY'),
        ),
    ]
