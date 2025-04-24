import os
import subprocess
import tempfile
import urllib.request
import customtkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#---------- Colors and Fonts ----------#
PRIMARY_COLOR = "#ffffff"
BG_COLOR = "#1B1D1E"
BTN_COLOR = "#2a2a2a"
BTN_HOVER = "#333333"
TEXT_COLOR = "#FFFFFF"
FONT = ("Segoe UI", 10)

#---------- Tools ----------#
def installSpicetify():
    consent = messagebox.askyesno(
        "Your consent is required",
        "By continuing, or by pressing 'Yes', you acknowledge that Spicetify is not owned by or affiliated with Spotify in any way. You further understand that Spicetify is in against of Spotify's Terms of Service and that Spotify may terminate your account (and the associated subscription(s)) at any time and that Spicetify (and all persons and entities involved in this code) shall have no liability for this (neither the creator of this code nor the creators of Spicetify)."
        "\n"
        "\nSPICETIFY IS A THIRD PARTY TOOL AND IS NOT A PART OF SPOTIFY AND SHALL NOT BE LIABLE FOR ANY (INCIDENTAL) DAMAGES."
        "\n"
        "\nSpicetify: https://github.com/spicetify/cli"
        "\nSpotify Privacy Policy: https://www.spotify.com/privacy/"
        "\nSpotify Terms of Use: https://www.spotify.com/legal/end-user-agreement/"
        "\n"
        "\nIf you have Spotify installed from the Microsoft Store, please uninstall it first!"
        "\n"
        "\nBy clicking yes, you EXPRESSLY agree to these terms!"
    )

    if not consent:
        log("❌ Update canceled: No agreement to the terms.")
        return
    try:
        command = 'powershell -Command "iwr -useb https://raw.githubusercontent.com/spicetify/cli/main/install.ps1 | iex"'
        subprocess.Popen(f'start cmd /k {command}', shell=True)
        log("✅ Spicetify is being installed.")
        log("To install the Marketplace, please enter 'Y' in the terminal!")
        log("After the process if finished, you can close the Terminal")
        log("\n——————————————————————————————\n")
    except Exception as e:
        print(f"Error when executing the command: {e}")
        log("\n——————————————————————————————\n")

#----- Update Spicetify -----#
def update_spicetify():
    try:
        subprocess.Popen('start cmd /k "spicetify update"', shell=True)
        log("✅ Spicetify is updated.")
        log("\n——————————————————————————————\n")
    except Exception as e:
        log(f"❌ Error when updating: {e}")
        log("\n——————————————————————————————\n")

#----- Reactivate Spicetify -----#
def reactivate_spicetify():
    try:
        temp_dir = tempfile.gettempdir()
        bat_path = os.path.join(temp_dir, "spicetify_auto.bat")
        with open(bat_path, "w") as f:
            f.write("@echo off\n")
            f.write("spicetify auto\n")
            f.write("pause\n")

        subprocess.Popen(f'start cmd /k "{bat_path}"', shell=True)
        log("✅ Spicetify is reactivated.")
        log("\n——————————————————————————————\n")
    except Exception as e:
        log(f"❌ Error during activation: {e}")
        log("\n——————————————————————————————\n")

#----- Update Spotify -----#
def update_spotify():
    consent = messagebox.askyesno(
        "Your consent is required",
        "To continue, you must agree to Spotify's Terms of Use and Privacy Policy."
        "\nTerms of Use: https://www.spotify.com/legal/end-user-agreement/"
        "\nPrivacy Policy: https://www.spotify.com/legal/privacy-policy/"
        "\n"
        "\nBy continuing or clicking “Yes”, you represent that you have read, understand, agree to and will abide by these Terms."
        "\n"
        "\nDo you agree?"
    )

    if not consent:
        log("❌ Update canceled: No agreement to the terms and conditions.")
        return

    temp_dir = tempfile.gettempdir()
    spotify_setup_path = os.path.join(temp_dir, "SpotifySetup.exe")
    url = "https://download.scdn.co/SpotifySetup.exe"

    try:
        log(" ⬇ Spotify-Installer wird heruntergeladen...")
        urllib.request.urlretrieve(url, spotify_setup_path)
        log("✅ Installer has been downloaded. The installer is started...")
        log("\n——————————————————————————————\n")
        os.startfile(spotify_setup_path)
    except Exception as e:
        log(f"❌ Error during update: {e}")
        log("\n——————————————————————————————\n")

def quit_program():
    root.destroy()

#---------- Legal and Spicetify ----------#
def  show_contact():
    log("\nDiscord: itsmarian.mc")
    log("\nMail: business.itsmarian@gmail.com")
    log("\nReddit: https://www.reddit.com/u/itsmarian_mc/")
    log("")
    log("If you find any errors or want to suggest improvements, feel free to contact me at these links. I am always open for feedback and improvements!")
    log("")
    log("\n——————————————————————————————\n")
    os.system("start \"\" https://discord.com/users/860122608682795028")
    os.system("start \"\" https://www.reddit.com/u/itsmarian_mc/")

#----- Credits -----#
def show_credits():
    log("")
    log("Author: itsmarian")
    log("Code licensed under Projekt City Ltd.")
    log("© 2025 Projekt City Ltd. | All rights reserved.")
    log("")
    log("Icon: Spicetify Logo by Spicetify")
    log("Copyright © 2025 Spicetify | All rights reserved.")
    log("")
    log("This code was created using Python and compiled using the \"pyinstaller\" library.")
    log("")
    log("Thank you to \"customtkinter\" for the modern and customizable GUI design based on Tkinter!")
    log("")
    log("The code for this programm is Open Source can be found here: https://github.com/itsmarianmc/itsmarian/tree/main/assets/public/spicetify/Spicetify_Manager_by_itsmarian.py")
    log("")
    log("\n——————————————————————————————\n")

#----- Licence -----#
def show_licence():
    log("")
    log("Copyright 2025 itsmarian & Projekt City Ltd.")
    log("Licensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License.")
    log("You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0")
    log("")
    log("Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.")
    log("See the License for the specific language governing permissions and limitations under the License.")
    log("")
    log("\n——————————————————————————————\n")

#----- About -----#
def openAbout():
    log("")
    log("About Spicetify:")
    log("Tutorial: https://www.reddit.com/r/spicetify/comments/1hrbeil/how_to_install_update_uninstall_spicetify_correct/")
    log("Spicetify Discord: https://discord.gg/VnevqPp2Rr")
    log("Spicetify Reddit: https://www.reddit.com/r/spicetify/")
    log("Spicetify Website: https://spicetify.app/")
    log("")
    log("\n——————————————————————————————\n")

#---------- Elements ----------#
def create_button(master, text, command):
    container = tk.Frame(master, bg=BG_COLOR)
    container.pack(fill='x', pady=6)

    btn = tk.Label(container, text=text, bg=BTN_COLOR, fg=TEXT_COLOR,
                   font=FONT, padx=14, pady=8, bd=0, relief="flat", cursor="hand2")
    btn.pack(fill='x', padx=5)

    btn.configure(highlightthickness=1, highlightbackground=BTN_COLOR)

    def on_enter(e): btn.config(bg=BTN_HOVER)
    def on_leave(e): btn.config(bg=BTN_COLOR)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.bind("<Button-1>", lambda e: command())

    return btn

def create_separator(master):
    sep = tk.Label(master, text="——————————————————————————————", bg=BG_COLOR, fg="#555555", font=("Segoe UI", 10, "bold"))
    sep.pack(pady=4)

#---------- Icon ----------#
icon_url = "http://raw.githubusercontent.com/itsmarianmc/itsmarian/refs/heads/main/assets/public/spicetify/spicetify-icon.ico"

temp_dir = tempfile.gettempdir()
temp_icon_path = os.path.join(temp_dir, "itsmariangithub-assets-public-spicetify-spicetify_icon.ico")

try:
    urllib.request.urlretrieve(icon_url, temp_icon_path)
except Exception as e:
    print(f"Error while getting logo: {e}")

def log(message):
    log_box.configure(state='normal')
    log_box.insert(tk.END, f"{message}\n")
    log_box.see(tk.END)
    log_box.configure(state='disabled')

#---------- Start and Build ----------#
root = tk.Tk()
root.title("Spicetify & Spotify Manager")

try:
    root.iconbitmap(temp_icon_path)
except Exception as e:
    print(f"Error while setting logo: {e}")

root.geometry("450x800")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

tk.Label(root, text="🎵 Spicetify & Spotify Manager\n[by itsmarian]", bg=BG_COLOR,
         fg=PRIMARY_COLOR, font=("Segoe UI", 16, "bold")).pack(pady=(15, 5))

button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=10, padx=30, fill="x")

#----- UI ------#
create_button(button_frame, "Install Spicetify", installSpicetify)
create_button(button_frame, "Update Spicetify", update_spicetify)
create_button(button_frame, "Reactivate Spicetify", reactivate_spicetify)
create_button(button_frame, "Update Spotify", update_spotify)
create_button(button_frame, "Close Program", quit_program)
create_separator(button_frame)
create_button(button_frame, "About", openAbout)
create_button(button_frame, "Contact", show_contact)
create_button(button_frame, "Credits", show_credits)
create_button(button_frame, "Licence", show_licence)

tk.Label(root, text="📋 LOG:", bg=BG_COLOR, fg=TEXT_COLOR,
         anchor='w', font=("Segoe UI", 11, "bold")).pack(padx=30, anchor="w", pady=(10, 0))

log_frame = tk.Frame(root, bg=BG_COLOR, padx=30)
log_frame.pack(fill='both', expand=True, pady=(0, 20))

text_frame = tk.Frame(log_frame, bg="#1e1e1e")
text_frame.pack(fill="both", expand=True)

log_box = tk.Text(text_frame, height=10, bg=BTN_COLOR, fg=TEXT_COLOR,
                  insertbackground=TEXT_COLOR, font=("Consolas", 10), wrap="word",
                  relief="flat", borderwidth=10)
log_box.pack(side="left", fill="both", expand=True, padx=(0, 5))
log_box.configure(state='disabled')

scrollbar = ttk.Scrollbar(text_frame, command=log_box.yview)
scrollbar.pack(side="right", fill="y")
log_box.config(yscrollcommand=scrollbar.set)

root.mainloop()

#
# Copyright (C) 2025 itsmarian | All rights reserved!
# Copyright (C) 2025 Projekt City Ltd. | All rights reserved!
# The code is distributed via Projekt City Ldt. and is the property of Projekt City Ldt.
# Code is distributed under the Apache 2.0 licence
# For more information see "Licence" in the App
#