# Generated by Django 4.1.7 on 2023-03-14 18:40

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0005_alter_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Agrega tu titulo', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Agrega texto adicional', required=True))])), ('Rich_text', streams.blocks.RichTextBlock()), ('cards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Agrega tu titulo', required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.blocks.CharBlock(max_length=200, required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='El boton de la pagina tiene prioridad sobre esto', required=False))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
