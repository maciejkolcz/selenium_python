import time


# typing slowly as if it was human
def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.1)