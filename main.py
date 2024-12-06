import os
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox

class SetupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Developer Setup App")
        
        self.label = tk.Label(root, text="Select items to install", font=("Arial", 16))
        self.label.pack(pady=20)
        self.apps_var = ["python", "g++", "git", "vscode", "sqlite", "notepadplusplus", "docker"]
        self.checkbuttons = []
        self.check_vars = []
        
        for app in self.apps_var:
            var = tk.BooleanVar(value=True)
            chk = tk.Checkbutton(root, text=app, variable=var)
            chk.pack(anchor='w')
            self.checkbuttons.append(chk)
            self.check_vars.append(var)
        self.apps_listbox = tk.Listbox(root, listvariable=self.apps_var, selectmode=tk.MULTIPLE, height=10)
        self.apps_listbox.pack(pady=40)
        self.setup_button = tk.Button(root, text="Install", command=self.setup_environment)
        self.setup_button.pack(pady=40)
        
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)
    
    def setup_environment(self):
        os_name = platform.system()
        messagebox.showinfo("OS Information", f"Detected OS: {os_name}")
        
        self.create_folder_structure()
        self.install_apps(os_name)
        
        messagebox.showinfo("Setup Complete", "Environment setup is complete.")
    
    def create_folder_structure(self):
        folders = ["Projects/Work", "Projects/Private", "Programs"]
        for folder in folders:
            os.makedirs(os.path.expanduser(f"~/{folder}"), exist_ok=True)
    
    def install_apps(self, os_name):
        if os_name == "Windows":
            self.install_windows_apps()
        elif os_name == "Linux":
            self.install_linux_apps()
        elif os_name == "Darwin":
            self.install_mac_apps()
    
    def install_windows_apps(self):
        apps = ["python", "cppcompiler", "git", "vscode", "visualstudio2019community", "sqlite", "notepadplusplus", "docker-desktop"]
        for app in apps:
            subprocess.run(["choco", "install", app, "-y"])
        apps = ["git", "python", "nodejs"]
        for app in apps:
            subprocess.run(["choco", "install", app, "-y"])
    
    def install_linux_apps(self):
        apps = ["python3", "g++", "git", "code", "sqlite3", "docker.io"]
        subprocess.run(["sudo", "apt-get", "update"])
        for app in apps:
            subprocess.run(["sudo", "apt-get", "install", "-y", app])
        
        # Notepad++ is not available directly via apt-get, using snap instead
        subprocess.run(["sudo", "snap", "install", "notepad-plus-plus", "--classic"])
        
        # Visual Studio is not available on Linux, skipping it
    
    def install_mac_apps(self):
        apps = ["python", "gcc", "git", "visual-studio-code", "visual-studio", "sqlite", "notepad-plus-plus", "docker"]
        for app in apps:
            subprocess.run(["brew", "install", app])

if __name__ == "__main__":
    root = tk.Tk()
    app = SetupApp(root)
    root.mainloop()