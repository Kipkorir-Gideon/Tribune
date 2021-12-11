# Generated by Django 3.2.9 on 2021-12-09 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='moringamerch',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='news.tags'),
        ),
    ]