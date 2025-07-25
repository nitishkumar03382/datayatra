# Generated by Django 5.2.2 on 2025-06-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_author_blog_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AddField(
            model_name='blog',
            name='github_link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
