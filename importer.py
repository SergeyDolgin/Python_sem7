def impo(new_person):
    with open('base.txt', 'a', encoding='utf-8') as file:
        file.write(new_person + '\n')