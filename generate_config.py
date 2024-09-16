import configparser
from pynput.mouse import Listener, Button

# Initialize the config parser
config = configparser.ConfigParser()
config['Coordinates'] = {}

# Predefined list of keys for the config file
coordinate_labels = [
    'IdField_x', 'IdField_y',
    'Degree_seq_x', 'Degree_seq_y',
    'Degree_num_x', 'Degree_num_y',
    'outcome_stat_x', 'outcome_stat_y',
    'Grad_term_x', 'Grad_term_y',
        "dummy_x" , "dummy_y",

    'go_x', 'go_y',
    'date_x', 'date_y',
    'save_x', 'save_y',
    'message_x', 'message_y',
    'refresh_x', 'refresh_y',
    'menu_x', 'menu_y',
    'system_x', 'system_y'
]

# Counter to keep track of the current coordinate label
coordinate_counter = 0

# Function called on a mouse click
def on_click(x, y, button, pressed):
    global coordinate_counter
    if pressed and button == Button.left:
        if coordinate_counter < len(coordinate_labels):
            # Assign the clicked position to the config labels
            config['Coordinates'][coordinate_labels[coordinate_counter]] = str(x)
            
            # Ensure there's a next label available for 'y' coordinate
            if coordinate_counter + 1 < len(coordinate_labels):
                config['Coordinates'][coordinate_labels[coordinate_counter + 1]] = str(y)
            
            coordinate_counter += 2
            print(f"Captured {coordinate_labels[coordinate_counter - 2]}: {x}, {coordinate_labels[coordinate_counter - 1]}: {y}")
            
            # If all coordinates are captured, save to config.ini and stop the listener
            if coordinate_counter >= len(coordinate_labels):
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
                print("All coordinates captured and saved to config.ini")
                return False  # Stop listener
        else:
            return False  # Stop listener

# Initialize the Listener to monitor mouse clicks
print("Please click the relevant positions in the order of the coordinate labels.")
with Listener(on_click=on_click) as listener:
    listener.join()
