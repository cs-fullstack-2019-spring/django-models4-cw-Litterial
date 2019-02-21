# Generated by Django 2.0.6 on 2019-02-21 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('phoneNumber', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='child_mom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cwApps.Mom'),
        ),
    ]
