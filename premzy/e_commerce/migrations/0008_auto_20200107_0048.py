# Generated by Django 2.2 on 2020-01-06 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0007_auto_20200107_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_commerce',
            name='picture',
            field=models.ImageField(max_length=1000, null=True, upload_to='pictures'),
        ),
    ]
