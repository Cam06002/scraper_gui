import requests as r
from bs4 import BeautifulSoup as bs
from tkinter import *
import tkinter as tk
from tkinter import ttk
import pandas as pd
import streamlit as stl

# setting up window
root = tk.Tk()
root.title("ScrapeScout")
root.geometry("800x500")

# inside the window
    # URL Label and entry box
ttk.Label(text="Enter the URL you would like to scrape:").grid(column=1, row=1, padx=15, pady=5)
url_box = ttk.Entry(root, width=50)
url_box.grid(column=1, row=2, padx=15, pady=5)

    # listing all labels to search
ttk.Label(text="List Top Class levels to search, separated by a comma:").grid(column=1, row=3, padx=15, pady=10)
top_list = ttk.Entry(root, width=50)
top_list.grid(column=1, row=4, padx=15, pady=5)

ttk.Label(text="List Secondary Class levels to search, separated by a comma:").grid(column=1, row=5, padx=15, pady=10)
secondary_list = ttk.Entry(root, width=50)
secondary_list.grid(column=1, row=6, padx=15, pady=5)

ttk.Label(text="List HTML types to search, separated by a comma:").grid(column=1, row=7, padx=15, pady=10)
label_list = ttk.Entry(root, width=50)
label_list.grid(column=1, row=8, padx=15, pady=5)


def scout():
    # Pulling results from URL
    # Main URL sourcing
    url_text = url_box.get()
    data = r.get(url_text)
    soup = bs(data.content, "html.parser")

    html_labels = str(top_list.get())
    html_labels_list = html_labels.split(', ')

    for label in html_labels_list:
        item_finder = soup.find_all("div", class_=label)
        for content in item_finder:
            print(content, end="\n"*2)


scout_button = ttk.Button(root, text="Scout", command=scout)
scout_button.grid(column=1, row=9, padx=30, pady=10)

root.mainloop()
