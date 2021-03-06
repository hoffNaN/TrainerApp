# Generated by Django 2.0 on 2018-02-16 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=3)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BasicUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('interests', models.TextField(max_length=200)),
                ('discription', models.TextField(max_length=400)),
                ('sex', models.CharField(max_length=1)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
                ('fb', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_gym', models.CharField(max_length=20)),
                ('discription', models.TextField(max_length=400)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='GymOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym', models.ManyToManyField(blank=True, to='trainer.Gym')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.TextField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('localization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion_type', models.CharField(choices=[('worse', 'worse'), ('bad', 'bad'), ('neutral', 'neutral'), ('good', 'good'), ('best', 'best')], default='neutral', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualifications', models.TextField(max_length=60)),
                ('experience', models.TextField(max_length=60)),
                ('gym', models.ManyToManyField(blank=True, to='trainer.Gym')),
                ('offert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trainer.Offer')),
                ('rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trainer.Opinion')),
            ],
        ),
        migrations.CreateModel(
            name='TrainType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_type', models.CharField(choices=[('joga', 'joga'), ('tbc', 'tbc'), ('fitness', 'fitness'), ('crossfit', 'crossfit')], default='joga', max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='trainer',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.TrainType'),
        ),
        migrations.AddField(
            model_name='offer',
            name='train_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.TrainType'),
        ),
        migrations.AddField(
            model_name='gymowner',
            name='offert',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trainer.Offer'),
        ),
        migrations.AddField(
            model_name='gym',
            name='offert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.TrainType'),
        ),
        migrations.AddField(
            model_name='basicuser',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.Contact'),
        ),
        migrations.AddField(
            model_name='basicuser',
            name='gymowner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trainer.GymOwner'),
        ),
        migrations.AddField(
            model_name='basicuser',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trainer.Trainer'),
        ),
        migrations.AddField(
            model_name='basicuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
