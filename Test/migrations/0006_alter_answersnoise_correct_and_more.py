# Generated by Django 4.1.6 on 2023-03-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0005_answersnoise_answersshorthand_delete_answertest1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answersnoise',
            name='correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answersshorthand',
            name='correct',
            field=models.BooleanField(default=False),
        ),
    ]
