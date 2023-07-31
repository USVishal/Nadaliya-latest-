# Generated by Django 4.2.3 on 2023-07-29 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NataliyaApp', '0007_category_rename_image1_item_image_remove_item_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='title_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NataliyaApp.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FileField(default='static/images/default.png', upload_to='images/items'),
        ),
    ]