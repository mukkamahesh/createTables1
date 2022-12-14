# Generated by Django 4.1.3 on 2022-12-08 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollnum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mahesh',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='suresh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('rollnum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.loki')),
            ],
        ),
        migrations.AddField(
            model_name='loki',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mahesh'),
        ),
    ]
