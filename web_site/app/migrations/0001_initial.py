# Generated by Django 4.2.5 on 2024-04-09 18:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NationalTeam",
            fields=[
                ("id_team", models.AutoField(primary_key=True, serialize=False)),
                (
                    "country_team",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
                ("year_of_start_team", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "national_team",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                ("id_player", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=45, null=True)),
                ("surname", models.CharField(blank=True, max_length=45, null=True)),
                ("date_of_birthday", models.DateField(blank=True, null=True)),
                ("city", models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                "db_table": "player",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="PlayerNumber",
            fields=[
                ("id_number", models.AutoField(primary_key=True, serialize=False)),
                ("number", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "player_number",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="PlayerPosition",
            fields=[
                ("id_position", models.AutoField(primary_key=True, serialize=False)),
                ("position", models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                "db_table": "player_position",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="PlayerStat",
            fields=[
                ("id_stat", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name_of_stat",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
                (
                    "value_of_stat",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
            ],
            options={
                "db_table": "player_stat",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="StartEndTeam",
            fields=[
                ("id_timedelta", models.AutoField(primary_key=True, serialize=False)),
                ("start", models.DateField(blank=True, null=True)),
                ("end", models.DateField(blank=True, null=True)),
            ],
            options={
                "db_table": "start_end_team",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                ("id_team", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name_of_team",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
                (
                    "country_team",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
            ],
            options={
                "db_table": "team",
                "managed": False,
            },
        ),
    ]
