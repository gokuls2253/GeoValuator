# Generated by Django 5.1.2 on 2024-10-12 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('total_sqft', models.FloatField()),
                ('bhk', models.IntegerField()),
                ('bath', models.IntegerField()),
                ('balcony', models.IntegerField()),
                ('price', models.FloatField()),
                ('area_type', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
        ),
    ]