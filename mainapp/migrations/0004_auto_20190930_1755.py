# Generated by Django 2.2.4 on 2019-09-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_pet_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pets_list_photo', verbose_name='Фотография питомца'),
        ),
    ]
