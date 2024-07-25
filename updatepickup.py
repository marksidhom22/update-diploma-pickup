import pyautogui as pg
import time
import pyperclip
import pandas as pd
import tkinter as tk
from tkinter import messagebox
import os

# Function to make a beep sound
def beep():
    try:
        # Windows
        import winsound
        winsound.Beep(1000, 500)
    except ImportError:
        # Other platforms
        os.system('echo -e "\a"')

# Function to show a pop-up message
def show_popup(message):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Notification", message)
    root.destroy()

# Function to check clipboard content and show a pop-up if it doesn't match the condition
def check_clipboard(expected_value):
    time.sleep(1)  # Ensure the clipboard content is available
    clipboard_content = pyperclip.paste().strip()
    if expected_value in clipboard_content:
        print(f"Match found: {clipboard_content}")
        return True
    else:
        issue_message = f"No match found. Clipboard contains: {clipboard_content}"
        print(issue_message)
        beep()
        show_popup(issue_message)
        return False

# Function to clear the clipboard
def clear_clipboard():
    pyperclip.copy('')  # Clear the clipboard

# Function to check if the date field is empty and act accordingly
def check_date_field():
    # Clear the clipboard
    clear_clipboard()
    
    # Copy the content of the date field
    pg.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Short delay to ensure clipboard content is available
    clipboard_content = pyperclip.paste().strip()
    
    # Check if the clipboard content is empty
    if clipboard_content:
        issue_message = f"Date field is not empty: {clipboard_content}"
        print(issue_message)
        beep()
        show_popup(issue_message)
        return False  # Date field was not empty
    else:
        # Type today's date (use the correct format for your need)
        pg.typewrite(time.strftime("%m/%d/%Y"))
        return True  # Date field was empty and updated

# Read the CSV file
df = pd.read_csv('Diploma mailing list(Name List).csv', delimiter=",")

# Iterate through the rows of the DataFrame
for index, row in df.iterrows():
    dawg_tag = str(row['Dawg Tag'])
    status = str(row['Status'])
    update_status = str(row['update_date_status'])

    # Check if the Status is empty
    if update_status != "done" and (pd.isna(status) or status.strip() == "" or status == 'nan'):
        print(f"Processing Dawg Tag: {dawg_tag}")

        # Simulate the action on the screen (e.g., typing the Dawg Tag)
        # Click to the Id field
        IdField_x = 373
        IdField_y = 170
        pg.click(IdField_x, IdField_y, duration=0.5)
        pg.click(IdField_x, IdField_y, duration=0.5)

        # Clear the Id field
        pg.keyDown("backspace")
        time.sleep(1)
        pg.keyUp("backspace")

        # Type the new Id
        time.sleep(1)
        pg.typewrite(dawg_tag)
        time.sleep(2)

        # Select Degree Sequence
        Degree_seq_x = 1300
        Degree_seq_y = 181
        pg.doubleClick(Degree_seq_x, Degree_seq_y, duration=0.5)

        # Select Degree Number
        Degree_num_x = 160
        Degree_num_y = 278
        pg.click(Degree_num_x, Degree_num_y, duration=0.5)
                
        # Select Outcome Status
        outcome_stat_x = 272
        outcome_stat_y = 284
        pg.click(outcome_stat_x, outcome_stat_y, duration=0.5)

        time.sleep(0.5)


        # Copy Outcome Status and check if it matches 'AW'
        clear_clipboard()
        pg.hotkey('ctrl', 'c')
        time.sleep(0.25)
        pg.hotkey('ctrl', 'c')
        check_clipboard("AW")

        # Select Graduation Term
        Grad_term_x = 1229
        Grad_term_y = 280
        pg.click(Grad_term_x, Grad_term_y, duration=0.5)

        time.sleep(0.5)

        # Copy Graduation Term and check if it matches '202420'
        clear_clipboard()
        pg.hotkey('ctrl', 'c')
        time.sleep(0.25)
        pg.hotkey('ctrl', 'c')
        check_clipboard("202420")

        # Double-click Degree Number to reset
        Degree_num_x = 160
        Degree_num_y = 278
        pg.doubleClick(Degree_num_x, Degree_num_y, duration=0.5)
        pg.doubleClick(Degree_num_x, Degree_num_y, duration=0.5)

        # Click Go
        go_x = 1845
        go_y = 172
        pg.doubleClick(go_x, go_y, duration=0.5)

        # Coordinates for the date field
        date_x = 348
        date_y = 670

        # Click Date field
        pg.click(date_x, date_y, duration=0.5)

        # Check if the date field is empty and act accordingly
        check_date_field()

        # Save
        save_x = 1896
        save_y = 970
        pg.doubleClick(save_x, save_y, duration=0.5)

        # Verify that the save was successful
        message_x = 1583
        message_y = 171
        pg.doubleClick(message_x, message_y)
        time.sleep(0.25)
        pg.doubleClick(message_x, message_y)

        pg.hotkey('ctrl', 'c')
        if check_clipboard("Saved successfully (1 rows saved)"):
            df.at[index, 'update_date_status'] = 'done'

        # Save the updated DataFrame back to the CSV file
        df.to_csv('Diploma mailing list(Name List).csv', index=False)

        # Refresh the screen
        refresh_x = 112
        refresh_y = 81
        pg.click(refresh_x, refresh_y, duration=0.5)
        time.sleep(2)

        # Navigate through the menu
        menu_x = 45
        menu_y = 551
        pg.click(menu_x, menu_y, duration=0.5)
        time.sleep(1)

        system_x = 192
        system_y = 407
        pg.click(system_x, system_y, duration=0.5)

        time.sleep(2)
