# Generated by Django 2.2.5 on 2022-02-08 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('kind', models.CharField(choices=[('free', 'Free'), ('member', 'Member'), ('humor', 'Humor'), ('study', 'Study'), ('notice', 'Notice'), ('Q&A', 'Q&A')], max_length=10)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
