# Generated by Django 4.1.7 on 2023-03-10 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0005_alter_homepage_options_remove_homepage_banner_image_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPageGalleryImage',
            new_name='HomePageBannerImage',
        ),
    ]
