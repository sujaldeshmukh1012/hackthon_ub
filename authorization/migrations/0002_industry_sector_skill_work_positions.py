# Generated by Django 4.2.3 on 2023-09-17 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry_Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_sector_name', models.CharField(max_length=100)),
                ('industry_sector_desc', models.CharField(max_length=1000)),
                ('industry_sector_level', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('skill_desc', models.CharField(max_length=1000)),
                ('skill_level', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Work_Positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_position_name', models.CharField(max_length=100)),
                ('work_position_desc', models.CharField(max_length=1000)),
                ('work_position_level', models.IntegerField(default=5)),
            ],
        ),
    ]
