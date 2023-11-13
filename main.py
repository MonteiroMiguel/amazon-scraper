import os
from dotenv import load_dotenv

from src.application.domain import get_links, get_products_infos, show_products_infos

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
load_dotenv()
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
RANGE_NAME =  os.getenv("RANGE_NAME")

links = get_links(SCOPES, SPREADSHEET_ID, RANGE_NAME)
products = get_products_infos(links)
show_products_infos(products)