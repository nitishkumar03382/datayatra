# Generated by Django 5.2.2 on 2025-06-18 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_alter_like_unique_together_remove_like_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
