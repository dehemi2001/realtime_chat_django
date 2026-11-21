from django.conf import settings
from django.db import migrations


def update_site_name(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    Site.objects.filter(id=settings.SITE_ID).update(name="Real-Time Chat")


def revert_site_name(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    Site.objects.filter(id=settings.SITE_ID).update(name="example.com")


class Migration(migrations.Migration):

    dependencies = [
        ("a_users", "0001_initial"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RunPython(update_site_name, revert_site_name),
    ]
