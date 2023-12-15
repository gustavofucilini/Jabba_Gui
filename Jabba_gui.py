import os
import subprocess
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import threading

def center_window(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def get_jabba_versions():
    output = subprocess.check_output("jabba ls", shell=True).decode()
    versions = [line for line in output.splitlines() if line]
    return versions

def get_remote_versions():
    output = subprocess.check_output("jabba ls-remote", shell=True).decode()
    versions = [line for line in output.splitlines() if line]
    return versions

def apply_version():
    selected_version = version.get()
    threading.Thread(target=use_version, args=(selected_version,)).start()

def use_version(selected_version):
    progress_bar.pack()  # Show the progress bar
    progress_bar.start()
    os.system(f"jabba use {selected_version}")
    java_home = subprocess.check_output(f"jabba which {selected_version}", shell=True).decode().strip()
    os.system(f"setx JAVA_HOME {java_home}")
    messagebox.showinfo("Info", f"JAVA_HOME updated to: {java_home}")
    progress_bar.stop()
    progress_bar.pack_forget()  # Hide the progress bar

def install_version():
    selected_version = remote_version.get()
    threading.Thread(target=install_version_thread, args=(selected_version,)).start()

def install_version_thread(selected_version):
    progress_bar.pack()  # Show the progress bar
    progress_bar.start()
    os.system(f"jabba install {selected_version}")
    messagebox.showinfo("Info", f"Java version {selected_version} installed")
    progress_bar.stop()
    progress_bar.pack_forget()  # Hide the progress bar
    versions = get_jabba_versions()
    version.set(versions[0])
    dropdown['values'] = versions

root = tk.Tk()
root.title("Java Version Manager")
root.geometry('400x200')

versions = get_jabba_versions()
remote_versions = get_remote_versions()

version = tk.StringVar()
version.set(versions[0])

remote_version = tk.StringVar()
remote_version.set(remote_versions[0])

dropdown = ttk.Combobox(root, textvariable=version, values=versions, width=30)
dropdown.pack()

button = tk.Button(root, text="Set Version", command=apply_version, width=20, height=2)
button.pack()

remote_dropdown = ttk.Combobox(root, textvariable=remote_version, values=remote_versions, width=30)
remote_dropdown.pack()

remote_button = tk.Button(root, text="Install Version", command=install_version, width=20, height=2)
remote_button.pack()

# Create the progress bar and hide it initially
progress_bar = ttk.Progressbar(root, mode="indeterminate", length=200)

center_window(root)  # Center the window
root.mainloop()
