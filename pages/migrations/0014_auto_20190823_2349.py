# Generated by Django 2.2 on 2019-08-23 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_remove_loginformmodel_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='news_long_par',
            field=models.TextField(blank=True, max_length=100000, null=True),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='news_more_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
