# Generated by Django 4.1.7 on 2023-04-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_alter_userdata_isexpert'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='Certificate',
            field=models.ImageField(null=True, upload_to='Certificates/'),
        ),
        migrations.AddField(
            model_name='userdata',
            name='isAdmin',
            field=models.BooleanField(default=False),
        ),
    ]
