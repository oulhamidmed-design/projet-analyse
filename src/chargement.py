from pathlib import Path
import pandas as pd

RAW = Path(__file__).resolve().parent.parent / "data" / "raw"

DATES_COMMANDES = [
    "order_purchase_timestamp", "order_approved_at",
    "order_delivered_carrier_date", "order_delivered_customer_date",
    "order_estimated_delivery_date",
]


def charger_brut():
    """Charge les 5 fichiers utilisés, avec les types dès la lecture."""
    commandes = pd.read_csv(RAW / "olist_orders_dataset.csv", parse_dates=DATES_COMMANDES)
    articles = pd.read_csv(RAW / "olist_order_items_dataset.csv", parse_dates=["shipping_limit_date"])
    clients = pd.read_csv(RAW / "olist_customers_dataset.csv", dtype={"customer_zip_code_prefix": str})
    produits = pd.read_csv(RAW / "olist_products_dataset.csv")
    traduction = pd.read_csv(RAW / "product_category_name_translation.csv")
    return commandes, articles, clients, produits, traduction
