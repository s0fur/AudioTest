# Generated by Django 4.1.6 on 2023-03-15 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertest1',
            name='audioNoise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers_noise', to='Test.noise'),
        ),
    ]
