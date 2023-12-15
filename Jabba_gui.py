import os
import subprocess
import threading
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import pyuac

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
    global button, remote_button, status_label #Add these lines
    selected_version = version.get()
    button['state'] = 'disabled' #Disable the button
    remote_button['state'] = 'disabled' #Disable the button
    status_label.config(text="Setting version...") #Update the status label
    threading.Thread(target=use_version, args=(selected_version,)).start()

def use_version(selected_version):
    global remote_button, button, status_label #Add these lines
    progress_bar.pack(padx=10, pady=10) #Show the progress bar
    progress_bar.start()
    subprocess.run(f"jabba use {selected_version}", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
    java_home = subprocess.check_output(f"jabba which {selected_version}", shell=True).decode().strip()
    subprocess.run(f"setx JAVA_HOME {java_home}", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
    subprocess.run(f'ftype jarfile="{java_home}\\bin\\javaw.exe" -jar "%1" %*', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
    #messagebox.showinfo("Info", f"JAVA_HOME updated to: {java_home}")
    progress_bar.stop()
    progress_bar.pack_forget() #Hide the progress bar
    status_label.config(text="Version set successfully!") #Update the status label
    button['state'] = 'normal' #Enable the button
    remote_button['state'] = 'normal' #Enable the button

def install_version():
    global remote_button, status_label, button #Add these lines
    selected_version = remote_version.get()
    button['state'] = 'disabled' #Disable the button
    remote_button['state'] = 'disabled' #Disable the button
    status_label.config(text="Installing version...") #Update the status label
    threading.Thread(target=install_version_thread, args=(selected_version,)).start()

def install_version_thread(selected_version):
    global remote_button, status_label, button #Add these lines
    progress_bar.pack(padx=10, pady=10) #Show the progress bar
    progress_bar.start()
    subprocess.run(f"jabba install {selected_version}", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
    #messagebox.showinfo("Info", f"Java version {selected_version} installed")
    progress_bar.stop()
    progress_bar.pack_forget() #Hide the progress bar
    versions = get_jabba_versions()
    version.set(versions[0])
    dropdown['values'] = versions
    status_label.config(text="Version installed successfully!") #Update the status label
    button['state'] = 'normal' #Enable the button
    remote_button['state'] = 'normal' #Enable the button

def main():
    global root, version, remote_version, dropdown, progress_bar, status_label, remote_button, button
    root = tk.Tk()
    root.title("Java Version Manager")
    root.geometry('400x300')
    root.resizable(False, False) #Prevent the window from being resized
    
    status_label = tk.Label(root, text="") #Create a label to display status messages
    status_label.pack(padx=10, pady=10)

    versions = get_jabba_versions()
    remote_versions = get_remote_versions()

    version = tk.StringVar()
    version.set(versions[0])

    remote_version = tk.StringVar()
    remote_version.set(remote_versions[0])

    dropdown = ttk.Combobox(root, textvariable=version, values=versions, width=30)
    dropdown.pack(padx=10, pady=10)

    button = tk.Button(root, text="Set Version", command=apply_version, width=20, height=2)
    button.pack(padx=10, pady=10)

    remote_dropdown = ttk.Combobox(root, textvariable=remote_version, values=remote_versions, width=30)
    remote_dropdown.pack(padx=10, pady=10)

    remote_button = tk.Button(root, text="Install Version", command=install_version, width=20, height=2)
    remote_button.pack(padx=10, pady=10)

    #Create the progress bar and hide it initially
    progress_bar = ttk.Progressbar(root, mode="indeterminate", length=200)

    center_window(root)  #Center the window
    root.mainloop()

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        main()
