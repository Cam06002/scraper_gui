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
ttk.Label(text="List HTML labels to search, separated by a comma:").grid(column=1, row=4, padx=15, pady=10)
label_list = ttk.Entry(root, width=50)
label_list.grid(column=1, row=5, padx=15, pady=5)


def scout():
    # Pulling results from URL
    # Main URL sourcing
    url_text = url_box.get()
    data = r.get(url_text)
    soup = data.text
    return soup


def add_labels():

    html_labels = str(label_list.get())
    html_labels_list = html_labels.split(', ')
    print(html_labels_list)


scout_button = ttk.Button(root, text="Scout", command=scout)
scout_button.grid(column=1, row=3, padx=30, pady=10)

add_labels_button = ttk.Button(root, text="Add Labels", command=add_labels)
add_labels_button.grid(column=1, row=6, padx=30, pady=10)

root.mainloop()
