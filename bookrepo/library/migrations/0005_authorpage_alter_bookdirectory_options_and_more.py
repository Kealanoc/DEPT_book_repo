# Generated by Django 4.2.2 on 2023-06-26 13:21

from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('library', '0004_alter_bookdirectory_custom_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('content', wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.blocks.CharBlock(help_text='add your additional text', required=True))])), ('full_richtext', streams.blocks.RichtextBlock())], blank=True, null=True, use_json_field=True)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Author Page',
                'verbose_name_plural': 'Author Pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='bookdirectory',
            options={'verbose_name': 'Book Page', 'verbose_name_plural': 'Author Pages'},
        ),
        migrations.RemoveField(
            model_name='bookdirectory',
            name='book_image',
        ),
        migrations.RemoveField(
            model_name='bookdirectory',
            name='custom_title',
        ),
        migrations.AddField(
            model_name='bookdirectory',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bookdirectory',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.blocks.CharBlock(help_text='add your additional text', required=True))])), ('full_richtext', streams.blocks.RichtextBlock())], blank=True, null=True, use_json_field=True),
        ),
        migrations.DeleteModel(
            name='AuthorDirectory',
        ),
    ]
