# Generated by Django 3.2.3 on 2021-06-02 07:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('hero', models.CharField(max_length=30)),
                ('heroine', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=30)),
                ('genre', models.CharField(help_text='Seperate genre with spaces', max_length=150, null=True)),
                ('language', models.CharField(help_text='Seperate language with spaces', max_length=150, null=True)),
                ('description', models.TextField(default='Description Text')),
                ('release_date', models.DateField(help_text='mm/dd/yyyy')),
                ('runtime_in_minutes', models.IntegerField(validators=[django.core.validators.MaxValueValidator(200)])),
                ('trailer', models.CharField(max_length=1000)),
                ('thumbnail_image', models.ImageField(upload_to='movie_thumbs')),
                ('slideshow_image', models.ImageField(default='true', upload_to='movie_thumbs')),
            ],
        ),
        migrations.CreateModel(
            name='screen',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('no_of_rows', models.IntegerField(validators=[django.core.validators.MaxValueValidator(75)])),
                ('no_of_columns', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
            ],
        ),
        migrations.CreateModel(
            name='theatre_manager',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='theatre',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('theatre_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theatre', to='dashboard.theatre_manager')),
            ],
        ),
        migrations.CreateModel(
            name='show',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_movie', to='dashboard.movie')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_screen', to='dashboard.screen')),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_theatre', to='dashboard.theatre')),
            ],
        ),
        migrations.AddField(
            model_name='screen',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screen', to='dashboard.theatre'),
        ),
    ]