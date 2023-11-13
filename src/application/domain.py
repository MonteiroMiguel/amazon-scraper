import os.path
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

creds = None
def get_links(SCOPES: list, SPREADSHEET_ID: str, RANGE_NAME: str):
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])
    links = [link[0] for link in values[1:]]
  except HttpError as err:
    print(err)
  return links


    
def init_driver():
  options = webdriver.ChromeOptions()
  options.add_experimental_option('excludeSwitches', ['enable-logging'])
  options.add_experimental_option("detach", True)
  options.add_argument("--headless=new")
  myservice = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(options=options, service=myservice)
  return driver

def get_products_infos(links: list) -> list:
  driver = init_driver()  
  infos = []
  for link in links:
    driver.get(link)
    time.sleep(2)
    title = driver.find_element("id", "productTitle").get_attribute("textContent")
    price = driver.find_element("id", "price").get_attribute("textContent")
    infos.append([title,price])
  driver.quit()  
  return infos



def show_products_infos(products: list):
  for product in products:
    print(f"Title: {product[0]}\nPrice: {product[1]}\n")




