from django.db import migrations


def populate_article_type(apps, schemaeditor):
    a_types = {
        "Report": "A journalistic piece",
        "Column": "A journalist's opinion piece",
        "Editorial": "An opinion piece by an editor"
    }
    ArticleType = apps.get_model("articles", "ArticleType")
    for name, description in a_types.items():
        at_obj = ArticleType(name=name, description=description)
        at_obj.save()


def populate_status(apps, schemaeditor):
    statuses = {
        "Pending": "An article that has not been reviewed",
        "Approved": "An article that has been approved by an editor",
        "Rejected": "An article that has been rejected by an editor"
    }
    Status = apps.get_model("articles", "Status")
    for name, description in statuses.items():
        st_obj = Status(name=name, description=description)
        st_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_article_type),
        migrations.RunPython(populate_status)
    ]
