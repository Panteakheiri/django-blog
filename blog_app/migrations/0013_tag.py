# Generated by Django 4.2.3 on 2023-07-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0012_savedpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
    ]
