import keyboard
import time
from tqdm import tqdm

# the series of buttons used to toggle grayscale (values used are scan codes)
# the buttons below correlate to keys [1, 2, 0, 2, 1] (for keypad and the number row.)
# - I chose these because of the error thrown during the Apollo 11 mission; easy to
#   remember.
commands_for_toggle = [[2, 3, 11, 3, 2], [79, 80, 82, 80, 79]]

# in seconds
time_to_sleep_for = 150

current_commands = []

def tmp_toggle_grayscale():
	global time_to_sleep_for

	keyboard.send('win+ctrl+c')
	for i in tqdm(range(time_to_sleep_for)):
		time.sleep(1)
	keyboard.send('win+ctrl+c')

def on_press(e):
	global current_commands
	global commands_for_toggle

	events = [i for i in keyboard._pressed_events]
	for event_code in events:
		current_commands.append(event_code)

		if len(current_commands) > len(commands_for_toggle[0]):
			current_commands = current_commands[1:]

		for command in commands_for_toggle:
			if current_commands == command:
				tmp_toggle_grayscale()

if __name__ == "__main__":
	keyboard.on_press(on_press)
	keyboard.wait()
