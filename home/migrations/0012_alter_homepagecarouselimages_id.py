# Generated by Django 4.1.7 on 2023-03-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_homepagecarouselimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagecarouselimages',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
