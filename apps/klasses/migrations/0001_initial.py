# Generated by Django 3.2.6 on 2021-09-11 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klass_id', models.CharField(blank=True, max_length=255, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='klasses', to='courses.course')),
            ],
        ),
    ]
