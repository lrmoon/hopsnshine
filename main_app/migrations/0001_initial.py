# Generated by Django 3.1.13 on 2022-06-06 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=50)),
                ('article_text', models.CharField(max_length=200)),
                ('article_date', models.DateTimeField(verbose_name='created At')),
            ],
        ),
    ]
