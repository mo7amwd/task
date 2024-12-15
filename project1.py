import tkinter as tk
from tkinter import ttk

def download_video(resolution):
    link = link_entry.get()
    if not link:
        status_label.config(text="Please paste a valid link.", fg="red")
    else:
        status_label.config(text=f"Downloading {resolution}...", fg="green")
        
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x200")
root.resizable(False, False)


title_label = tk.Label(root, text="YouTube Downloader", font=("Arial", 14))
title_label.pack(pady=10)

link_label = tk.Label(root, text="Paste link here:")
link_label.pack()
link_entry = tk.Entry(root, width=50)
link_entry.pack(pady=5)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

high_res_button = ttk.Button(buttons_frame, text="High Resolution", command=lambda: download_video("High Resolution"))
high_res_button.grid(row=0, column=0, padx=5)

low_res_button = ttk.Button(buttons_frame, text="Low Resolution", command=lambda: download_video("Low Resolution"))
low_res_button.grid(row=0, column=1, padx=5)

audio_button = ttk.Button(buttons_frame, text="Audio Only", command=lambda: download_video("Audio Only"))
audio_button.grid(row=0, column=2, padx=5)


status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=10)

root.mainloop()
