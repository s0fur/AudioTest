# Generated by Django 4.1.6 on 2023-03-15 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_alter_answertest1_audionoise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertest1',
            name='audioShorthand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers_shorthand', to='Test.shorthand'),
        ),
    ]
