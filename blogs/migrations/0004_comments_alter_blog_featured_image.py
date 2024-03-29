# Generated by Django 4.0.3 on 2022-10-19 17:38

import blogs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blog_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name=blogs.models.Blog)),
                ('title', models.CharField(max_length=200)),
                ('comment', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
