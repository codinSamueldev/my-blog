# Generated by Django 5.0 on 2024-10-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='pic_source',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
