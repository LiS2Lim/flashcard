# Generated by Django 4.1.4 on 2022-12-30 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Flash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=30)),
                ('answer', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('count', models.IntegerField()),
                ('tags', models.ManyToManyField(to='flashcard.tag')),
            ],
        ),
    ]