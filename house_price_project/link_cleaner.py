with open('unique_links.txt') as file:
    links = file.readlines()

with open('processed.txt') as file:
    processed = file.readlines()

with open('unique_links.txt', 'w') as file:
    unique = [i for i in links if i not in processed]
    file.writelines(unique)
