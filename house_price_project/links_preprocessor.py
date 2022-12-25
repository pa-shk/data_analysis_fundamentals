with open('links.txt') as file:
    data = file.readlines()

with open('unique_links.txt', 'w') as file:
    file.writelines(set(data))
