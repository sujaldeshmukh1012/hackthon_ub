# Generated by Django 4.2.3 on 2023-09-17 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authorization', '0002_industry_sector_skill_work_positions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('banner', models.ImageField(blank=True, upload_to='project-banners/')),
                ('description', models.TextField()),
                ('contact_email', models.EmailField(max_length=200)),
                ('purpose', models.CharField(blank=True, max_length=400)),
                ('want_to_expand', models.BooleanField(default=False)),
                ('industry', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='authorization.industry_sector')),
                ('skills_used', models.ManyToManyField(blank=True, to='authorization.skill')),
                ('team_members', models.ManyToManyField(blank=True, to='authorization.userprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRecruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('open_till', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('description', models.CharField(max_length=500)),
                ('paid', models.BooleanField(default=False)),
                ('pay', models.CharField(max_length=200)),
                ('position', models.ManyToManyField(blank=True, to='authorization.work_positions')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('message', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]