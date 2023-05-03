# Generated by Django 4.1.7 on 2023-03-13 18:28

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Agrega tu titulo', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Agrega texto adicional', required=True))]))], blank=True, null=True, use_json_field=True),
        ),
    ]