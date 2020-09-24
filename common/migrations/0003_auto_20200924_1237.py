# Generated by Django 3.0.6 on 2020-09-24 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20200924_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='common.Class'),
        ),
        migrations.AddField(
            model_name='user',
            name='_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='common.Class'),
        ),
    ]
