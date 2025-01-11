# Generated by Django 5.1.3 on 2025-01-07 09:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Blog category',
                'verbose_name_plural': 'Blog categories',
            },
        ),
        migrations.CreateModel(
            name='BlogTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Blog tag',
                'verbose_name_plural': 'Blog tags',
            },
        ),
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('image1', models.ImageField(upload_to='blogs')),
                ('image2', models.ImageField(upload_to='blogs')),
                ('short_description', models.CharField(max_length=255)),
                ('long_descriptions', models.TextField()),
                ('categories', models.ManyToManyField(related_name='blogs', to='blogs.blogcategorymodel')),
                ('tags', models.ManyToManyField(related_name='blogs', to='blogs.blogtagmodel')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='BlogLikeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_like', to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_likes', to='blogs.blogmodel')),
            ],
            options={
                'verbose_name': 'Blog like',
                'verbose_name_plural': 'Blog likes',
            },
        ),
        migrations.CreateModel(
            name='BlogCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('comment', models.CharField(max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to='blogs.blogmodel')),
            ],
            options={
                'verbose_name': 'Blog comment',
                'verbose_name_plural': 'Blog comments',
            },
        ),
    ]
