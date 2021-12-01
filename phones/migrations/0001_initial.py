from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]
