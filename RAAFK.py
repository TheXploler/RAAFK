import random
import time
import pygetwindow as gw
from pynput import keyboard
from datetime import datetime

# Setup keystroke controller
controller = keyboard.Controller()

# CONFIGURATION : List of keys
keys = [
    keyboard.KeyCode.from_char('w'),
    keyboard.KeyCode.from_char('a'),
    keyboard.KeyCode.from_char('s'),
    keyboard.KeyCode.from_char('d'),
    keyboard.Key.space,
    keyboard.KeyCode.from_char('i'),
    keyboard.KeyCode.from_char('o'),
    keyboard.Key.left,
    keyboard.Key.right
]

# CONFIGURATION : Timings for key presses and delays
min_press_time = 0.3  # Minimum time to hold keys (seconds)
max_press_time = 2.2  # Maximum time to hold keys (seconds)
min_key_delay = 0.3    # Minimum delay between key presses (seconds)
max_key_delay = 0.8    # Maximum delay between key presses (seconds)
min_cycle_delay = 1.5  # Minimum delay between action cycles (seconds)
max_cycle_delay = 4.0  # Maximum delay between action cycles (seconds)

# Generate random integer
def rand_int(min_value, max_value):
    return random.randint(min_value, max_value)

# Get current timestamp
def current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


# Main()
try:
    # Track if the window is focused
    was_window_focused = True
    print("RAAFK ready")

    while True:
        active_window = gw.getActiveWindow()
        is_window_focused = active_window is not None and active_window.title == "Roblox"

        if is_window_focused:
            if not was_window_focused:
                print(
                    f"[{current_timestamp()}] Window focused: {active_window.title}")
            was_window_focused = True

            # Press multi/single key
            if random.randint(0, 3) == 0:  # 25% chance multi
                num_keys = random.randint(2, 3)  # 2/3 keys
                keys_to_press = []

                # Select unique keys
                while len(keys_to_press) < num_keys:
                    key = random.choice(keys)
                    if key not in keys_to_press:
                        keys_to_press.append(key)

                # Press selected keys
                print(
                    f"[{current_timestamp()}] Pressing keys: {[str(key) for key in keys_to_press]}")
                for key in keys_to_press:
                    controller.press(key)

                # Hold keys
                duration = rand_int(int(min_press_time * 1000),
                                    int(max_press_time * 1000)) / 1000
                time.sleep(duration)

                # Release keys
                for key in keys_to_press:
                    controller.release(key)

                print(
                    f"[{current_timestamp()}] Held keys for {duration:.2f} seconds")

                # Add random delay before next key press
                cycle_delay = rand_int(
                    int(min_cycle_delay * 1000), int(max_cycle_delay * 1000)) / 1000
                time.sleep(cycle_delay)

            else:
                # Randomly select single key
                current_key = random.choice(keys)

                # Press n release single key
                print(f"[{current_timestamp()}] Pressing key: {current_key}")
                start_time = time.time()
                duration = rand_int(int(min_press_time * 1000),
                                    int(max_press_time * 1000)) / 1000
                controller.press(current_key)
                time.sleep(duration)
                controller.release(current_key)

                # Log duration
                press_duration = (time.time() - start_time) * \
                    1000  # Convert to milliseconds
                print(
                    f"[{current_timestamp()}] Pressed key: {current_key} for {press_duration:.2f} ms")

                # Random delay before next key press
                key_delay = rand_int(
                    int(min_key_delay * 1000), int(max_key_delay * 1000)) / 1000
                time.sleep(key_delay)

                # Press extra key
                if random.randint(0, 1) == 1:  # 50% chance
                    extra_key = random.choice(keys)
                    extra_duration = rand_int(100, 400) / 1000
                    print(
                        f"[{current_timestamp()}] Pressing extra key: {extra_key}")
                    controller.press(extra_key)
                    time.sleep(extra_duration)
                    controller.release(extra_key)

                    # Log
                    print(
                        f"[{current_timestamp()}] Pressed extra key: {extra_key} for {extra_duration * 1000:.2f} ms")

                # Random delay before next key press
                cycle_delay = rand_int(
                    int(min_cycle_delay * 1000), int(max_cycle_delay * 1000)) / 1000
                time.sleep(cycle_delay)

        else:
            # Notify when window is unfocused
            if was_window_focused:
                print(
                    f"[{current_timestamp()}] Not focused on the game. Current active window: {active_window.title if active_window else 'None'}")
            was_window_focused = False
            time.sleep(1)

except KeyboardInterrupt:
    print("Script interrupted by the user.")
