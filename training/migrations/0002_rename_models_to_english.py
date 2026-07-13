from django.db import migrations


def rename_legacy_tables(apps, schema_editor):
    legacy_tables = {
        "training_atleta": "training_athlete",
        "training_grupomuscular": "training_musclegroup",
        "training_exercicio": "training_exercise",
        "training_fichadetreino": "training_workoutplan",
        "training_itemfichadetreino": "training_workoutitem",
    }
    existing_tables = set(schema_editor.connection.introspection.table_names())

    for old_table, new_table in legacy_tables.items():
        if old_table in existing_tables and new_table not in existing_tables:
            schema_editor.alter_db_table(None, old_table, new_table)


class Migration(migrations.Migration):
    dependencies = [
        ("training", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(rename_legacy_tables, migrations.RunPython.noop),
    ]
