from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]