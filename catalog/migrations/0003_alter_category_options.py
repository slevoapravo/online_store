

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_product_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["id"],
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
    ]