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


# wwpd questions

def wwpd_lists():

    # reference sequences
    a = [1, 5, 4, [2, 3], 3]

    intro()

    print(">>> a = [1, 5, 4, [2, 3], 3]")
    print(">>> print(a[0], a[-1])")
    x = input()
    while x != "1 3":
        x = repeat()
    
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
    
    # reference sequences
    pokemon = {'pikachu': 25, 'dragonair': 148}

    intro()

    print(">>> pokemon = {'pikachu': 25, 'dragonair': 148}")
    print(">>> pokemon")
    x = input()
    while x.replace(" ", "") != str(pokemon).replace(" ", ""):
        x = repeat()

    print(">>> 'mewtwo' in pokemon")
    x = input()
    while x != str('mewtwo' in pokemon):
        x = repeat()

    print(">>> len(pokemon)")
    x = input()
    while x != str(len(pokemon)):
        x = repeat()

    pokemon['mew'] = pokemon['pikachu']
    pokemon[25] = 'pikachu'
    print(">>> pokemon['mew'] = pokemon['pikachu']")
    print(">>> pokemon[25] = 'pikachu'")
    print(">>> pokemon")
    x = input()
    while x.replace(" ", "") != str(pokemon).replace(" ", ""):
        x = repeat()

    pokemon['mewtwo'] = pokemon['mew'] * 2
    print(">>> pokemon['mewtwo'] = pokemon['mew'] * 2")
    print(">>> pokemon")
    x = input()
    while x.replace(" ", "") != str(pokemon).replace(" ", ""):
        x = repeat()

    pokemon[['firetype', 'flying']] = 146
    print(">>> pokemon[['firetype', 'flying']] = 146")
    x = input()
    while x != 'error':
        x = repeat()

    outro()


def wwpd_list_mutation():

    #reference sequences
    lst = [5, 6, 7, 8]

    intro()

    lst.append(6)
    print(">>> lst = [5, 6, 7, 8]")
    print(">>> lst.append(6)")
    x = input()
    while x != "nothing":
        x = repeat()

    print(">>> lst")
    x = input()
    while x.replace(" ", "") != str(lst).replace(" ", ""):
        x = repeat()

    lst.insert(0, 9)
    print(">>> lst.insert(0, 9)")
    print(">>> lst")
    x = input()
    while x.replace(" ", "") != str(lst).replace(" ", ""):
        x = repeat()

    y = lst.pop(2)
    print(">>> x = lst.pop(2)")
    print(">>> lst")
    x = input()
    while x.replace(" ", "") != str(lst).replace(" ", ""):
        x = repeat()

    lst.remove(y)
    print(">>> lst.remove(x)")
    print(">>> lst")
    x = input()
    while x.replace(" ", "") != str(lst).replace(" ", ""):
        x = repeat()

    a, b = lst, lst[:]
    print(">>> a, b = lst, lst[:]")
    print(">>> a is lst")
    x = input()
    while x != str(a is lst):
        x = repeat()

    print(">>> b == lst")
    x = input()
    while x != str(b == lst):
        x = repeat()

    lst = [1, 2, 3]
    lst.extend([4,5])
    print(">>> lst = [1, 2, 3]")
    print(">>> lst.extend([4,5])")
    print(">>> lst")
    x = input()
    while x.replace(" ", "") != str(lst).replace(" ", ""):
        x = repeat()

    lst.extend([lst.append(9), lst.append(10)])
    print(">>> lst.extend([lst.append(9), lst.append(10)])")
    print(">>> lst")
    x = input()
    while x.replace(" ", "") != str(lst).replace(" ", ""):
        x = repeat()

    outro()