# Generated by Django 4.2.3 on 2023-07-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NataliyaApp', '0005_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image2',
            field=models.FileField(blank=True, default='static/images/default.jpg', upload_to='images/items'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image3',
            field=models.FileField(blank=True, default='static/images/default.jpg', upload_to='images/items'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image4',
            field=models.FileField(blank=True, default='static/images/default.jpg', upload_to='images/items'),
        ),
    ]
