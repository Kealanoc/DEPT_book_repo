# Generated by Django 4.2.2 on 2023-06-26 11:32

from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookDirectory',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('custom_title', models.CharField(help_text='OverWrites Existing default title', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AuthorDirectory',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('custom_title', models.CharField(help_text='OverWrites Existing default title', max_length=100)),
                ('content', wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.blocks.CharBlock(help_text='add your additional text', required=True))])), ('richtext', streams.blocks.RichtextBlock())], blank=True, null=True, use_json_field=True)),
                ('author_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
