# lab04 WWPD?

# preliminaries

def repeat():
    print("try again:")
    return input()


def intro():
    print("What Would Python Display?")
    print(
        "type the expected output, 'function' if you think the answer is a function object, 'infinite loop' if it loops forever, 'nothing' if nothing is displayed, or 'error' if it errors; use single quotes '' when needed\n"
    )


def outro():
    print("\nall questions for this question set complete")


# reference sequences
a = [1, 5, 4, [2, 3], 3]
pokemon = {'pikachu': 25, 'dragonair': 148}

# wwpd questions

def wwpd_lists():

    intro()

    print(">>> a = [1, 5, 4, [2, 3], 3]")
    print(">>> print(a[0], a[-1])")
    x = input()
    while x != "1 3":
        x - repeat()
    
    print(">>> len(a)")
    x = input()
    while x != str(len(a)):
        x = repeat()

    print(">>> 2 in a")
    x = input()
    while x != str(2 in a):
        x = repeat()

    print(">>> a[3][0]")
    x = input()
    while x != str(a[3][0]):
        x = repeat()
    
    outro()


def wwpd_dictionaries():
    
    intro()

    print(">>> pokemon = {'pikachu': 25, 'dragonair': 148}")
    x = input()
    while x != "{'pikachu': 25, 'dragonair': 148}":
        x = repeat()

    print(">>> 'mewtwo' in pokemon")
    x = input()
    while x != str('mewtwo' in pokemon):
        x = repeat()

    print(">>> len(pokemon)")
    x = input()
    while x != str(len(pokemon)):
        x = repeat()

    print(">>> pokemon['mew'] = pokemon['pikachu']")
    print(">>> pokemon[25] = 'pikachu'")
    print(">>> pokemon")

    pokemon['mew'] = pokemon['pikachu']
    pokemon[25] = 'pikachu'
    x = input()
    while x != "{'pikachu': 25, 'dragonair': 148, 'mew': 25, 25: 'pikachu'}":
        x = repeat()
