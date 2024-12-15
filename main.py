import tkinter as tk
from tkinter import ttk
import subprocess
import os
import platform
#added messagebox manually
from tkinter import messagebox

#1
class SetupApp:
    def __init__(self, root):
        self.root = root
        self.const_frame()

    #Added manually to make the GUI more dynammic (unsuccessfully). Also moved things around. 
    def const_frame(self):
        #Made changes to GUI manually
        self.root.geometry("500x500")
        self.root.title("Setup App")
        #7 
        self.cancel_button = tk.Button(root, text="Cancel", command=root.quit)
        self.cancel_button.pack(side='right', anchor='sw', padx=10, pady=40)
        self.select_apps_frame()


    def select_apps_frame(self):
        self.label = tk.Label(text="Select applications to install:", font=("Arial", 16))
        self.label.pack(pady=20)
       
        #6
        self.apps = ["Python", "G++", "Git", "VSCode", "SQLite", "Notepad++", "Docker", "Chrome", "CMake", "Arduino"]
        self.check_vars = {}
        for app in self.apps:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(root, text=app, variable=var)
            chk.pack(anchor='w')
            self.check_vars[app] = var

       
        #7. Replaced command install_apps with identify_and_install
        self.ok_btn = tk.Button(text="Install", command=self.identify_and_install)
        self.ok_btn.pack(side='left', anchor='sw', padx=10, pady=40)
        

    #3
    def install_apps_windows(self, selected_apps):

        total_apps = len(selected_apps)
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(pady=10)
        #8
        install_commands = {
            "Python": "winget install Python.Python.3",
            "G++": "winget install GnuWin32.Gcc",
            "Git": "winget install Git.Git",
            "VSCode": "winget install Microsoft.VisualStudioCode",
            "SQLite": "winget install SQLite.sqlite",
            "Notepad++": "winget install Notepad++.Notepad++",
            "Docker": "winget install Docker.DockerDesktop",
            "Chrome": "winget install Google.Chrome",
            "CMake": "winget install Kitware.CMake",
            "Arduino": "winget install Arduino.ArduinoIDE"
        }
        
        for i, app in enumerate(selected_apps):
            if app in install_commands:
                try:
                    subprocess.run(install_commands[app], check=True, shell=True)
                    print(f"{app} installed successfully on Windows.")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to install {app} on Windows: {e}")
            self.update_progress_bar(i + 1, total_apps)
        print("Windows installation process completed.")

    #4
    def install_apps_linux(self, selected_apps):
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(pady=10)
        print("Selected apps for installation on Linux:", selected_apps)
        #9
        install_commands = {
            "Snap": "sudo apt-get install -y snapd",
            "Python": "sudo apt-get install -y python3",
            "G++": "sudo apt-get install -y g++",
            "Git": "sudo apt-get install -y git",
            "VSCode": "sudo snap install --classic code",
            "SQLite": "sudo apt-get install -y sqlite3",
            "Notepad++": "sudo snap install notepad-plus-plus",
            "Docker": "sudo apt-get install -y docker.io",
            "Chrome": "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && sudo dpkg -i google-chrome-stable_current_amd64.deb && sudo apt-get -f install -y",
            "CMake": "sudo apt-get install -y cmake",
            "Arduino": "sudo apt-get install -y arduino"
        }

        #Added manually because I tried to solve the issue of parsing the password throgh the script
        self.run_commands_linux(selected_apps,install_commands)


    #had call the commands in a separate function
    def run_commands_linux(self, selected_apps, install_commands): 
        total_apps = len(selected_apps)
        subprocess.run(["sudo", "apt-get", "update"], shell=True)
        
        for i, app in enumerate(selected_apps):
            if app in install_commands:
                try:
                    command = f"sudo -S {install_commands[app]}"
                    subprocess.run(command, check=True, shell=True)
                    print(f"{app} installed successfully on Linux.")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to install {app} on Linux: {e}")
            self.update_progress_bar(i + 1, total_apps)
        print("Linux installation process completed.")


    #5
    def install_apps_mac(self, selected_apps):
        total_apps = len(selected_apps)
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(pady=10)
        print("Selected apps for installation on Mac:", selected_apps)
        #10
        install_commands = {
            "Python": "brew install python",
            "G++": "brew install gcc",
            "Git": "brew install git",
            "VSCode": "brew install --cask visual-studio-code",
            "SQLite": "brew install sqlite",
            "Notepad++": "brew install --cask notepad-plus-plus",
            "Docker": "brew install --cask docker",
            "Chrome": "brew install --cask google-chrome",
            "CMake": "brew install cmake",
            "Arduino": "brew install --cask arduino"
        }

        #Added brew manually
        subprocess.run(["/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""], shell=True)
        
        #Replaced first loop manually from "for app in selected_apps:""
        for i, app in enumerate(selected_apps):    
            if app in install_commands:
                try:
                    subprocess.run(install_commands[app], check=True, shell=True)
                    print(f"{app} installed successfully on Mac.")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to install {app} on Mac: {e}")
            self.update_progress_bar(i + 1, total_apps)
        print("Mac installation process completed.")

   #2
    def create_folder_structure(self):
      folders = ["Projects/Work", "Projects/Private", "Apps", "Program-files"]
      for folder in folders:
          os.makedirs(os.path.expanduser(f"~/{folder}"), exist_ok=True)

    #11
    def identify_and_install(self):
        self.create_folder_structure()

        selected_apps = [app for app, var in self.check_vars.items() if var.get()]
        if not selected_apps:
            tk.messagebox.showwarning("No Selection", "No applications selected for installation.")
            return

        os_name = platform.system()
        if os_name == "Windows":      
            self.install_windows_apps(selected_apps)
        elif os_name == "Linux":
            self.install_apps_linux(selected_apps)        
        elif os_name == "Darwin":
            self.install_apps_mac(selected_apps)
        else:
            tk.messagebox.showerror("Unsupported OS", f"{os_name} is not supported.")


    #12
    #moved this function out of install_apps_windows so that it can be used in other functions
    def update_progress_bar(self, current, total):
       progress = (current / total) * 100
       self.progress_var.set(progress)
       self.root.update_idletasks()  

if __name__ == "__main__":
    root = tk.Tk()
    app = SetupApp(root)
    root.mainloop()