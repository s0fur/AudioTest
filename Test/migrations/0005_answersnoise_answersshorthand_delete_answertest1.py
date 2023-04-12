# Generated by Django 4.1.6 on 2023-03-15 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0004_answertest1_correct'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswersNoise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField()),
                ('text', models.CharField(max_length=255, null=True)),
                ('correct', models.BooleanField()),
                ('audioNoise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_noise', to='Test.noise')),
            ],
        ),
        migrations.CreateModel(
            name='AnswersShorthand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField()),
                ('text', models.CharField(max_length=255, null=True)),
                ('correct', models.BooleanField()),
                ('audioShorthand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_shorthand', to='Test.shorthand')),
            ],
        ),
        migrations.DeleteModel(
            name='AnswerTest1',
        ),
    ]
