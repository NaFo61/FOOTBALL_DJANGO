from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def get_tables():
    tables = [
        {
            "name": NationalTeam,
            "url": NationalTeam._meta.db_table,
            "description": NationalTeam.desc(),
            "count": NationalTeam.objects.all().count(),
            "fields": ["ID", "Сборная", "Начало карьеры"],
            "form": NationalTeamForm,
        },
        {
            "name": Team,
            "url": Team._meta.db_table,
            "description": Team.desc(),
            "count": Team.objects.all().count(),
            "fields": ["ID", "Название команды", "Страна команды"],
        },
        {
            "name": Player,
            "url": Player._meta.db_table,
            "description": Player.desc(),
            "count": Player.objects.all().count(),
            "fields": ["ID", "Имя", "Фамилия", "Год рождения", "Город рождения", "Сборная"],
            "form": PlayerForm,
        },
        {
            "name": PlayerNumber,
            "url": PlayerNumber._meta.db_table,
            "description": PlayerNumber.desc(),
            "count": PlayerNumber.objects.all().count(),
            "fields": ["ID", "Номер"],
        },
        {
            "name": PlayerPosition,
            "url": PlayerPosition._meta.db_table,
            "description": PlayerPosition.desc(),
            "count": PlayerPosition.objects.all().count(),
            "fields": ["ID", "Позиция"],
        },
        {
            "name": PlayerStat,
            "url": PlayerStat._meta.db_table,
            "description": PlayerStat.desc(),
            "count": PlayerStat.objects.all().count(),
            "fields": ["ID", "Параметр", "Значение", "Игрок"],
        },
        {
            "name": StartEndTeam,
            "url": StartEndTeam._meta.db_table,
            "description": StartEndTeam.desc(),
            "count": StartEndTeam.objects.all().count(),
            "fields": ["ID", "Начало", "Конец", "Игрок", "Команда", "Позиция", "Номер"],
        },
    ]
    return tables


def tables(request):
    template_dir = "app/tables.html"

    models = [NationalTeam, PlayerStat, Player, PlayerNumber, PlayerPosition, StartEndTeam, Team]

    tables_data = []
    for model in models:
        description = model.desc() if hasattr(model, 'desc') else "Здесь описание"
        tables_data.append({
            "name": model,
            "url": model._meta.db_table,
            "description": description,
            "count": model.objects.count(),  # Определение количества записей в модели
        })

    context = {
        "tables": tables_data
    }
    return render(request, template_dir, context=context)


def table(request, table):
    template_dir = "app/table.html"
    model = None
    for tbl in get_tables():
        if tbl.get("url") == table:
            model = tbl.get("name")
            fields = tbl.get("fields")
            break

    if model is not None:
        rows = model.objects.all()
        context = {
            "table": table,
            "table_name": model,
            "rows": rows,
            "fields": fields,
        }
        return render(request, template_dir, context=context)
    else:
        return HttpResponseNotFound("Table not found")


def add(request, table):
    template_dir = "app/add.html"

    if request.user.is_authenticated:
        model = None
        for tbl in get_tables():
            if tbl.get("url") == table:
                model = tbl.get("name")
                Form = tbl.get("form")
                break
        if model is not None:
            if request.method == 'POST':
                form = Form(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect("app:table", table=table)
            else:
                form = Form()

            context = {
                "table": table,
                "table_name": model,
                "form": form,
            }
            return render(request, template_dir, context=context)
        return redirect("app:tables")
    return redirect("app:table", table=table)