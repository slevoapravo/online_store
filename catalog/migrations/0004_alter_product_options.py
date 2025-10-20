
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_category_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["id"],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]