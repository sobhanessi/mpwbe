# Generated by Django 2.2 on 2019-09-04 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20190904_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='newscreatetm',
            name='pic',
            field=models.ImageField(default='nothing', upload_to='images/'),
            preserve_default=False,
        ),
    ]
