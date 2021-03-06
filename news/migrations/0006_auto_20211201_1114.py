# Generated by Django 3.2.9 on 2021-12-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20211124_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterRecipients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='news.tags'),
        ),
    ]
