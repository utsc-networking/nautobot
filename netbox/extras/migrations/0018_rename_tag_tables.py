# Generated by Django 2.1.4 on 2019-02-20 06:59

from django.db import migrations


class AppTaggitAlterModelTable(migrations.AlterModelTable):
    """
    A special subclass of AlterModelTable which hardcodes the app_label to 'taggit'

    This is needed because the migration deals with models which belong to the taggit
    app, however because taggit is a 3rd party app, we cannot create our own migrations
    there.
    """

    def state_forwards(self, app_label, state):
        super().state_forwards('taggit', state)

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        super().database_forwards('taggit', schema_editor, from_state, to_state)

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        super().database_backwards('taggit', schema_editor, from_state, to_state)

    def reduce(self, operation, app_label=None):
        if app_label:
            app_label = 'taggit'
        super().reduce(operation, app_label=app_label)


class Migration(migrations.Migration):
    """
    Rename the tables from taggit_* to extras_*

    Note that while we change the database state, we are not deleting the django
    model state for the taggit models. Doing so would result in makemigrations
    recreating them.
    """

    dependencies = [
        ('taggit', '0001_initial'),
        ('extras', '0017_tag_taggeditem'),
    ]

    operations = [
        AppTaggitAlterModelTable(
            name='Tag',
            table='extras_tag'
        ),
        AppTaggitAlterModelTable(
            name='TaggedItem',
            table='extras_taggeditem'
        ),
    ]
