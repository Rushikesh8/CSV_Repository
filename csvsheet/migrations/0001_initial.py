# Generated by Django 2.2.5 on 2021-03-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CSV_File', models.FileField(upload_to='csvsheet')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]