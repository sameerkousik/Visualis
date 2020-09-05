# Generated by Django 3.0.8 on 2020-09-05 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('title', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentDevelopment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('development', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('stream_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='JobRole',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('html_enabled', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('responsibilities', models.TextField()),
                ('salary', models.TextField()),
                ('working_hrs', models.TextField(blank=True)),
                ('qualifications', models.TextField(blank=True)),
                ('skills', models.TextField(blank=True)),
                ('experience', models.TextField(blank=True)),
                ('employer', models.TextField(blank=True)),
                ('prospects', models.TextField(blank=True)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streams.Branch')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='stream_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streams.Stream'),
        ),
    ]
