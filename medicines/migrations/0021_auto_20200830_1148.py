# Generated by Django 3.1 on 2020-08-30 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0020_auto_20200830_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='slug',
            field=models.SlugField(default='me..r<mNdmf.Fnh', unique=True),
        ),
    ]