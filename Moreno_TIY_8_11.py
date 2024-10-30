def show_messages(short_text_msgs):
    while short_text_msgs:
        for msg in short_text_msgs:
            print(msg)
        break

sent_messages = []

def send_messages(short_text_msgs, sent_messages):
    """prints each message and moves them to a list named 'sent_messages'"""
    while short_text_msgs:
        current_message = short_text_msgs.pop()
        print(current_message)
        sent_messages.append(current_message)

    # pop() - removes last item in list but lets you use it after removal
    # can be used for 'current' item in a loop as in this program

short_text_msgs = [
    'hi',
    'hello vro',
    'how are you',
]

send_messages(short_text_msgs[:], sent_messages)

print(f"\n'sent_messages' list: {sent_messages}")

print(f"\n'short_text_msgs' list: {short_text_msgs}")