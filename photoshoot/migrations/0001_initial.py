# Generated by Django 2.1.2 on 2019-02-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='static/pages')),
                ('caption', models.CharField(max_length=1000)),
                ('image_date', models.DateField()),
                ('date', models.DateTimeField(verbose_name='date logged')),
            ],
        ),
    ]
