import tkinter as tk
from tkinter import ttk
import phonenumbers
import requests
from phonenumbers import geocoder, carrier, timezone
from apis import BLOCK_API

def search_number():
    user_input = phone_entry.get()
    pepnumber = phonenumbers.parse(user_input, "US")
    location = geocoder.description_for_number(pepnumber, "en")
    carrier_info = carrier.name_for_number(pepnumber, "en")
    tz_info = timezone.time_zones_for_number(pepnumber)

    for record in data:
        if record["caller_id_number"] == user_input:
            result_label.config(text=f"Location: {location}\nCarrier: {carrier_info}\nTimezone: {tz_info}\nCaller ID: {record['caller_id_number']}\nZipCode: {record['zip']}\nState: {record['state']}\nIssue: {record['issue']}\nType: {record['type_of_call_or_messge']}")
            return
        
    result_label.config(text="Number not found in database.")

def get_json_data():
    response = requests.get(BLOCK_API)
    response.raise_for_status()
    return response.json()

data = get_json_data()

root = tk.Tk()
root.title("Phone Number Search")

main_frame = ttk.Frame(root, padding ="20")
main_frame.grid()

phone_label = tk.Label(root, text="Enter phone number:")
phone_label.grid(row=0, column=0, sticky="w")

phone_entry = tk.Entry(root)
phone_entry.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(root, text="Search", command=search_number)
search_button.grid(row=0, column=2, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()
