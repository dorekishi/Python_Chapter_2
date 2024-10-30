short_text_msgs = [
    'hi',
    'hello vro',
    'how are you',
]

def show_messages():
    while short_text_msgs:
        for msg in short_text_msgs:
            print(msg)
        break

show_messages()