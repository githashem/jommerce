# Generated by Django 4.0.5 on 2022-07-11 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='id')),
                ('expire_date', models.DateTimeField(db_index=True, verbose_name='expire_date')),
                ('ip', models.GenericIPAddressField(verbose_name='ip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='auth.user', verbose_name='user')),
            ],
            options={
                'verbose_name': 'session',
                'verbose_name_plural': 'sessions',
            },
        ),
    ]
