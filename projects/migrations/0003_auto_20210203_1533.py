# Generated by Django 2.2.7 on 2021-02-03 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210203_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='E:\\Python\\Django\rp-portfolio\\projects\\static\\img'),
        ),
    ]
