# Generated by Django 3.0.13 on 2021-03-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='default.jpg', upload_to='articles/'),
        ),
    ]
