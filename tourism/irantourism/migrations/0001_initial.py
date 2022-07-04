# Generated by Django 3.2.7 on 2021-12-30 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('detail', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('detail', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TouristAttraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('adress', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfAttraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Travelogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('tourist_attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='irantourism.touristattraction')),
            ],
        ),
        migrations.AddField(
            model_name='touristattraction',
            name='type_of_attraction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='irantourism.typeofattraction'),
        ),
        migrations.CreateModel(
            name='Souvenir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_num', models.IntegerField(max_length=11)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='irantourism.city')),
            ],
        ),
        migrations.CreateModel(
            name='HotelAndRestaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_building', models.CharField(choices=[('HOTEL', 'Hotel'), ('RESTAURANT', 'Restaurant')], default='HOTEL', max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('phone_num', models.IntegerField(max_length=11)),
                ('image', models.ImageField(upload_to='')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='irantourism.city')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='irantourism.state'),
        ),
    ]