import requests
import json
import gspread  # pip install gspread

gc = gspread.service_account(filename="email.json")
sh = gc.open_by_key(
    "1IRAW2sVEEHs-znI-oFPXbtbxYfw-xGCkEu9y3jFKbws"
)  # or by sheet name: gc.open("TestList")
worksheet = sh.sheet1


url = "http://127.0.0.1:8000/extract_info_from_email"

# email = """
# Dear Jason
# I hope this message finds you well. I'm Shirley from Gucci;

# I'm looking to purchase some company T-shirt for my team, we are a team of 2 people, and we want to get 5k t-shirt per personl

# Please let me know the price and timeline you can work with;

# Looking forward

# Shirley Lou
# """

email = """

hey i'm looking for a job as a software engineer. I have 5 years of experience in datasciece
"""

payload = {"from_email": "@example.com", "content": email}
# payload = {"content": email}


# print("Payload:", payload)


response = requests.post(url, json=payload)

print("Response:", response.json())


response_json = response.json()

# Extracted values as a list
extracted_values = list(response_json.values())
worksheet.append_row(extracted_values)
