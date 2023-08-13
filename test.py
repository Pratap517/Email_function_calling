import requests
import json
import gspread  # pip install gspread

'''SETUP
- google developer console: https://console.developers.google.com
- new project -> activate drive and sheets api
- credentials -> service account -> name + role=editor
  ->create key and download json
- share client_email fom json in your sheets
'''


gc = gspread.service_account(filename="email.json")
sh = gc.open_by_key(
    "sheet id"
)  # or by sheet name: gc.open("TestList")
worksheet = sh.sheet1


url = "http://0.0.0.0:8000/extract_info_from_email"

email = """

I hope this message finds you well. I'm mike from Gucci;

I'm looking to purchase some company T-shirt for my team, we are a team of 2 people, and we want to get 5k t-shirt per personl

Please let me know the price and timeline you can work with;

Looking forward


"""


payload = {"from_email": "test@example.com", "content": email}
# payload = {"content": email}


response = requests.post(url, json=payload)

print("Response:", response.json())


response_json = response.json()

# Extracted values as a list
extracted_values = list(response_json.values())
#writing to sheets
worksheet.append_row(extracted_values)
