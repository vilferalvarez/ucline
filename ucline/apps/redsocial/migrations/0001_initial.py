# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-10 05:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area_conocimiento',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=50)),
                ('descripcion', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='like_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('content_type', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='redsocial.Post')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.TextField(primary_key=True, serialize=False)),
                ('password', models.TextField(blank=True, null=True, verbose_name=django.db.models.deletion.SET_NULL)),
                ('email', models.TextField(unique=True)),
                ('name', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redsocial.User'),
        ),
        migrations.AddField(
            model_name='like_post',
            name='ownwr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redsocial.User'),
        ),
        migrations.AddField(
            model_name='like_post',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='redsocial.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redsocial.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='redsocial.Post'),
        ),
        migrations.AddField(
            model_name='area_conocimiento',
            name='usuarios',
            field=models.ManyToManyField(to='redsocial.User'),
        ),
    ]
