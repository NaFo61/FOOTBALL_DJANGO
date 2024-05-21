from django.db import models


class NationalTeam(models.Model):
    id_team = models.AutoField(primary_key=True)
    country_team = models.CharField(max_length=45, blank=True, null=True)
    year_of_start_team = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'national_team'

    def __str__(self):
        return "Сборная"

    @classmethod
    def desc(cls):
        return "Здесь описание"

    def get_values(self):
        return [
            self.id_team,
            self.country_team,
            self.year_of_start_team
        ]



class Player(models.Model):
    id_player = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    surname = models.CharField(max_length=45, blank=True, null=True)
    date_of_birthday = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    national_team_id_team = models.ForeignKey(NationalTeam, models.DO_NOTHING, db_column='national_team_id_team')

    class Meta:
        managed = False
        db_table = 'player'

    def __str__(self):
        return "Игроки"

    @classmethod
    def desc(cls):
        return "Здесь описание"

    def get_values(self):
        return [
            self.id_player,
            self.name,
            self.surname,
            self.date_of_birthday,
            self.city,
            self.national_team_id_team.country_team
        ]


class PlayerNumber(models.Model):
    id_number = models.AutoField(primary_key=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_number'

    def __str__(self):
        return "Номер"

    @classmethod
    def desc(cls):
        return "Здесь описание"

    def get_values(self):
        return [
            self.id_number,
            self.number
        ]


class PlayerPosition(models.Model):
    id_position = models.AutoField(primary_key=True)
    position = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_position'

    def __str__(self):
        return "Позиция"

    @classmethod
    def desc(cls):
        return "Здесь описание"

    def get_values(self):
        return [
            self.id_position,
            self.position
        ]


class PlayerStat(models.Model):
    id_stat = models.AutoField(primary_key=True)
    name_of_stat = models.CharField(max_length=45, blank=True, null=True)
    value_of_stat = models.CharField(max_length=45, blank=True, null=True)
    player = models.ForeignKey(Player, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_stat'

    def __str__(self):
        return "Статистика"

    @classmethod
    def desc(cls):
        return "Здесь описание"

    def get_values(self):
        return [
            self.id_stat,
            self.name_of_stat,
            self.value_of_stat,
            f"{self.player.name} {self.player.surname}",
        ]


class StartEndTeam(models.Model):
    id_timedelta = models.AutoField(primary_key=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    player = models.ForeignKey(Player, models.DO_NOTHING, blank=True, null=True)
    team_id_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='team_id_team', blank=True, null=True)
    player_positions_id_position = models.ForeignKey(PlayerPosition, models.DO_NOTHING,
                                                     db_column='player_positions_id_position', blank=True, null=True)
    player_number_id_number = models.ForeignKey(PlayerNumber, models.DO_NOTHING, db_column='player_number_id_number',
                                                blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'start_end_team'

    def __str__(self):
        return "Промежутки игр"

    @classmethod
    def desc(cls):
        return "Здесь описание"

    def get_values(self):
        return [
            self.id_timedelta,
            self.start,
            self.end,
            f"{self.player.name} {self.player.surname}",
            self.team_id_team.name_of_team,
            self.player_positions_id_position.position,
            self.player_number_id_number.number
        ]


class Team(models.Model):
    id_team = models.AutoField(primary_key=True)
    name_of_team = models.CharField(max_length=45, blank=True, null=True)
    country_team = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'

    def __str__(self):
        return "Команды"

    @classmethod
    def desc(cls):
        return "Здесь описание"

    def get_values(self):
        return [
            self.id_team,
            self.name_of_team,
            self.country_team
        ]
