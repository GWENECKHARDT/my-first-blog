# Generated by Django 2.2.12 on 2020-06-05 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.CharField(default='topic', max_length=150),
            preserve_default=False,
        ),
    ]
