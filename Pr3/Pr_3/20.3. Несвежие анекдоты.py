list = []

def print_only_new(message):
    if message not in list:
        print(message)
        list.append(message)
