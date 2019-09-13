# Generated by Django 2.2.5 on 2019-09-11 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('curriculum', models.FileField(upload_to='docs/')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professors',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('frequency', models.IntegerField()),
                ('relative_frequency', models.FloatField()),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professor', to='teacher.Professor')),
            ],
            options={
                'verbose_name': 'Word',
                'verbose_name_plural': 'Words',
                'unique_together': {('professor', 'word')},
            },
        ),
    ]