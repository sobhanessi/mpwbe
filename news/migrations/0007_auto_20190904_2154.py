# Generated by Django 2.2 on 2019-09-04 21:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0006_createnewstm'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreateNewsTM',
            new_name='NewsCreateTM',
        ),
    ]
