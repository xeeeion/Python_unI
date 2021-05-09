def from_string_to_list(string, container):
    for i in map(int, string.split()):
        container.append(i)
    return container
