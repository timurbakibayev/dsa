# Generated by Django 2.1.7 on 2019-04-04 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190403_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='google_forms',
            field=models.TextField(default='https://docs.google.com/forms/d/154PrmgPscbmq01MXtt2SugR8rAOgHc1Evdtt4g6cyTU'),
        ),
    ]
