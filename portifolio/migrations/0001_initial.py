# Generated by Django 3.2.5 on 2021-09-01 09:34

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=130)),
                ('cover', models.ImageField(upload_to='')),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('content', django_quill.fields.QuillField()),
                ('views', models.IntegerField(default=0, editable=False)),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
            },
        ),
    ]
