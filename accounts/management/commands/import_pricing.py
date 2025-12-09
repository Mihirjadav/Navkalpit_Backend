import csv
import pandas as pd
from django.core.management.base import BaseCommand
from decimal import Decimal
from accounts.models import Technology, Material, MaterialPrice, Tier
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = "Import pricing from an Excel or CSV. Format expected: technology,material,tier,price_per_gram,density_g_per_cm3(optional)"

    def add_arguments(self, parser):
        parser.add_argument("path", type=str)

    def handle(self, *args, **options):
        path = options["path"]
        if path.lower().endswith(".csv"):
            df = pd.read_csv(path)
        else:
            df = pd.read_excel(path)
        # normalize columns
        for idx, row in df.iterrows():
            tech_slug = str(row.get("technology")).strip()
            tech_name = tech_slug
            tech, _ = Technology.objects.get_or_create(slug=tech_slug.lower(), defaults={"name": tech_name})

            material_name = str(row.get("material")).strip()
            density = row.get("density_g_per_cm3", None)
            mat, _ = Material.objects.get_or_create(technology=tech, name=material_name, defaults={"density_g_per_cm3": density})

            tier_slug = str(row.get("tier")).strip()
            tier_name = tier_slug
            tier, _ = Tier.objects.get_or_create(slug=tier_slug.lower(), defaults={"name": tier_name})

            price = Decimal(str(row.get("price_per_gram")))

            mp, created = MaterialPrice.objects.update_or_create(
                material=mat, tier=tier,
                defaults={"price_per_gram": price, "min_price_per_gram": None, "max_price_per_gram": None}
            )
            self.stdout.write(self.style.SUCCESS(f"Saved {mat.name} / {tier.slug} -> {price}"))
