# Generated by Django 4.1.6 on 2023-04-10 12:05

import Test.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0009_alter_noise_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noise',
            name='audio',
            field=models.FileField(upload_to=Test.models.PathAndRenameAudio('noise_audio/')),
        ),
        migrations.AlterField(
            model_name='noise',
            name='text',
            field=models.FileField(upload_to=Test.models.PathAndRename('noise_csv/')),
        ),
    ]
