
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_entry_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry",
            name="view_counter",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Счетчик просмотров"
            ),
        ),
    ]