# Generated by Django 3.1.7 on 2021-02-28 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capstoneapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', related_query_name='resource', to='capstoneapi.resourcecategory')),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', related_query_name='resource', to='capstoneapi.journeyuser')),
            ],
        ),
    ]
