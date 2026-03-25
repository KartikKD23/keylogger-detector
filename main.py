import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import time

from detector import get_processes
from ai_model import classify
from utils import log_alert


def scan(output_box):
    while True:
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, "Scanning...\n\n")

        processes = get_processes()

        for name, pid, cpu, keyword_flag in processes:
            status = classify(cpu, keyword_flag)

            if status == "Suspicious":
                msg = f"{name} (PID: {pid}) CPU: {cpu}"
                output_box.insert(tk.END, f"[ALERT ⚠️] {msg}\n")
                log_alert(msg)

                messagebox.showwarning("Threat Detected!", msg)

            else:
                output_box.insert(tk.END, f"{name} (Safe)\n")

        time.sleep(5)


def start_app():
    window = tk.Tk()
    window.title("Keylogger Detector Pro")
    window.geometry("600x450")

    label = tk.Label(window, text="AI Keylogger Detection System", font=("Arial", 16))
    label.pack()

    output_box = scrolledtext.ScrolledText(window, width=70, height=20)
    output_box.pack()

    thread = threading.Thread(target=scan, args=(output_box,))
    thread.daemon = True
    thread.start()

    window.mainloop()


start_app()