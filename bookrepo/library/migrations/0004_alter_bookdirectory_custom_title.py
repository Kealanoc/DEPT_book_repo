# Generated by Django 4.2.2 on 2023-06-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_rename_author_image_bookdirectory_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdirectory',
            name='custom_title',
            field=models.CharField(blank=True, help_text='OverWrites Existing default title', max_length=100),
        ),
    ]
