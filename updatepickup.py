import pyautogui as pg
import time
import pyperclip
import pandas as pd
import tkinter as tk
from tkinter import messagebox
import os
import configparser
from tkinter import ttk

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
    time.sleep(wait_time)  # Short delay to ensure clipboard content is available
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

# Load coordinates and settings from config file
config = configparser.ConfigParser()
config.read('config.ini')

# Get wait_mode from config
wait_mode = config.get('Settings', 'wait_mode', fallback='normal')

# Set wait time based on the mode (normal or long)
if wait_mode == 'long':
    wait_time = 4  # Long waiting time (in seconds)
else:
    wait_time = 0.5  # Normal waiting time (in seconds)


import csv

def update_row_in_csv(csv_file, updated_row, row_index):
    temp_file = 'temp.csv'  # Temporary file for writing updated rows
    with open(csv_file, mode='r', newline='') as infile, open(temp_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Loop through the CSV and write the updated row when the index matches
        for i, row in enumerate(reader):
            if i == row_index:
                writer.writerow(updated_row)  # Write the updated row
            else:
                writer.writerow(row)  # Write the original row

    # Replace the original file with the updated file
    os.replace(temp_file, csv_file)

# Main processing function
def process_csv():
    # Read the CSV file
    df = pd.read_csv('Diploma mailing list(Name List).csv', delimiter=",")
    refresh()
    # Iterate through the rows of the DataFrame
    for index, row in df.iterrows():
        dawg_tag = str(row['Dawg Tag'])
        decision = str(row['decision'])
        update_status = str(row['update_date_status'])

        # Check if the Status is empty
        if update_status != "done" and (pd.isna(decision) or decision.strip() == "" or decision == 'nan'):
            print(f"Processing Dawg Tag: {dawg_tag}")

            # Simulate the action on the screen (e.g., typing the Dawg Tag)
            IdField_x = int(config['Coordinates']['IdField_x'])
            IdField_y = int(config['Coordinates']['IdField_y'])
            pg.click(IdField_x, IdField_y, duration=wait_time)
            pg.click(IdField_x, IdField_y, duration=wait_time)

            # Clear the Id field
            pg.keyDown("backspace")
            time.sleep(2*wait_time)
            pg.keyUp("backspace")

            # Type the new Id
            time.sleep(2*wait_time)
            pg.typewrite(dawg_tag)
            time.sleep(4*wait_time)

            Degree_seq_x = int(config['Coordinates']['Degree_seq_x'])
            Degree_seq_y = int(config['Coordinates']['Degree_seq_y'])
            pg.doubleClick(Degree_seq_x, Degree_seq_y, duration=wait_time)
            time.sleep(2*wait_time)

            Degree_num_x = int(config['Coordinates']['Degree_num_x'])
            Degree_num_y = int(config['Coordinates']['Degree_num_y'])
            pg.click(Degree_num_x, Degree_num_y, duration=wait_time)

            outcome_stat_x = int(config['Coordinates']['outcome_stat_x'])
            outcome_stat_y = int(config['Coordinates']['outcome_stat_y'])
            pg.click(outcome_stat_x, outcome_stat_y, duration=wait_time)

            time.sleep(wait_time)

            clear_clipboard()
            pg.hotkey('ctrl', 'c')
            time.sleep(wait_time)
            pg.hotkey('ctrl', 'c')
            if not check_clipboard("AW"):
                df.at[index, 'update_date_status'] = 'Update Failed'
            # Save the updated DataFrame back to the CSV file after each loop
            # Convert the updated DataFrame row back to a list to write into the CSV
                df.at[index, 'decision'] = ''
                updated_row = df.iloc[index].tolist()
                update_row_in_csv('Diploma mailing list(Name List).csv', updated_row, index+1)

                refresh()
                continue


            Grad_term_x = int(config['Coordinates']['Grad_term_x'])
            Grad_term_y = int(config['Coordinates']['Grad_term_y'])
            pg.click(Grad_term_x, Grad_term_y, duration=wait_time)

            time.sleep(wait_time)

            clear_clipboard()
            pg.hotkey('ctrl', 'c')
            time.sleep(wait_time)
            pg.hotkey('ctrl', 'c')
            if not check_clipboard("202440"):
                df.at[index, 'update_date_status'] = 'Update Failed'
            # Save the updated DataFrame back to the CSV file after each loop
            # Convert the updated DataFrame row back to a list to write into the CSV
                df.at[index, 'decision'] = ''
                updated_row = df.iloc[index].tolist()
                update_row_in_csv('Diploma mailing list(Name List).csv', updated_row, index+1)

                refresh()
                continue

            Degree_num_x = int(config['Coordinates']['Degree_num_x'])
            Degree_num_y = int(config['Coordinates']['Degree_num_y'])
            pg.doubleClick(Degree_num_x, Degree_num_y, duration=wait_time)
            pg.doubleClick(Degree_num_x, Degree_num_y, duration=wait_time)

            go_x = int(config['Coordinates']['go_x'])
            go_y = int(config['Coordinates']['go_y'])
            pg.doubleClick(go_x, go_y, duration=wait_time)

            date_x = int(config['Coordinates']['date_x'])
            date_y = int(config['Coordinates']['date_y'])
            pg.click(date_x, date_y, duration=wait_time)

            check_date_field()

            save_x = int(config['Coordinates']['save_x'])
            save_y = int(config['Coordinates']['save_y'])
            pg.doubleClick(save_x, save_y, duration=wait_time)

            message_x = int(config['Coordinates']['message_x'])
            message_y = int(config['Coordinates']['message_y'])
            pg.doubleClick(message_x, message_y)
            time.sleep(0.25)
            pg.doubleClick(message_x, message_y)

            pg.hotkey('ctrl', 'c')
            if check_clipboard("Saved successfully (1 rows saved)"):
                df.at[index, 'update_date_status'] = 'done'

            else:
                df.at[index, 'update_date_status'] = 'Update Failed'
            # Save the updated DataFrame back to the CSV file after each loop
            # Convert the updated DataFrame row back to a list to write into the CSV
            df.at[index, 'decision'] = ''
            updated_row = df.iloc[index].tolist()
            update_row_in_csv('Diploma mailing list(Name List).csv', updated_row, index+1)

            refresh()


def refresh():
    refresh_x = int(config['Coordinates']['refresh_x'])
    refresh_y = int(config['Coordinates']['refresh_y'])
    pg.click(refresh_x, refresh_y, duration=wait_time)
    time.sleep(4*wait_time)

    menu_x = int(config['Coordinates']['menu_x'])
    menu_y = int(config['Coordinates']['menu_y'])
    pg.click(menu_x, menu_y, duration=wait_time)
    time.sleep(2*wait_time)

    system_x = int(config['Coordinates']['system_x'])
    system_y = int(config['Coordinates']['system_y'])
    pg.click(system_x, system_y, duration=wait_time)

    time.sleep(4*wait_time)

# GUI
def run_gui():
    root = tk.Tk()
    root.title("Process Dawg Tags")
    root.geometry("300x150")

    label = tk.Label(root, text="Click 'Start' to process the CSV.")
    label.pack(pady=10)

    start_button = ttk.Button(root, text="Start", command=process_csv)
    start_button.pack(pady=10)

    root.mainloop()

# Determine whether to run in GUI or direct mode based on config
run_mode = config.get('Settings', 'run_mode', fallback='gui')

if run_mode == 'gui':
    run_gui()  # Launch the GUI
else:
    process_csv()  # Run directly
