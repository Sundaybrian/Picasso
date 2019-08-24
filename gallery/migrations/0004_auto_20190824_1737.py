# Generated by Django 2.2.4 on 2019-08-24 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(to='gallery.tags'),
        ),
        migrations.AlterField(
            model_name='image',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Photographer'),
        ),
    ]