# Generated by Django 4.1.7 on 2023-05-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_userdata_pending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='Certificate',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='pic',
            field=models.ImageField(null=True, upload_to='media/Certificates/'),
        ),
    ]