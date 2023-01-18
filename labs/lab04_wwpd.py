# lab04 WWPD?


# IMPORTS

import inspect
import tests.wwpd_storage as s

st = s.wwpd_storage 


# COLORED PRINTS - custom text type to terminal: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal, ANSI colors: http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

class bcolors:
    HIGH_MAGENTA = '\u001b[45m'
    HIGH_GREEN = '\u001b[42m'
    HIGH_YELLOW = '\u001b[43;1m'
    MAGENTA = ' \u001b[35m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33;1m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\u001b[0m'

def print_error(message):
    print("\n" + bcolors.HIGH_YELLOW + bcolors.BOLD + "ERROR:" + bcolors.RESET + bcolors.YELLOW + bcolors.BOLD + " " + message + bcolors.ENDC)

def print_message(message):
    print("\n" + bcolors.HIGH_MAGENTA + bcolors.BOLD + "MESSAGE:" + bcolors.RESET + bcolors.MAGENTA + bcolors.BOLD + " " + message + bcolors.ENDC)

def print_success(message):
    print("\n" + bcolors.HIGH_GREEN + bcolors.BOLD + "SUCCESS:" + bcolors.RESET + bcolors.GREEN + bcolors.BOLD + " " + message + bcolors.ENDC)


# INCORRECT ANSWER LOOP, INSTRUCTIONS, COMPLETE, OPTIONS

def repeat():
    print("Try again:")
    return input()

def intro(name):
    print("\nWhat Would Python Display?: " + name)
    print("Type the expected output, 'function' if you think the answer is a function object, 'infinite loop' if it loops forever, 'nothing' if nothing is displayed, or 'error' if it errors; use single quotes '' when needed.\n")

def complete():
    print_success("All questions for this question set complete.")

def options():
    print_message("All questions for this question set complete. Restart question set?")
    guess = input("Y/N?\n")
    guess = guess.lower()
    while guess != "y" and guess != "n":
        print_error("Unknown input, please try again.")
        guess = input()
    if guess == "y":
        return "restart"
    return False


# WWPD? ALGORITHM 

def wwpd(name, question_set, stored_list):

    intro(name)

    matched = str([i[:-1] for i in question_set])[1:-1] in str([i[:-1] for i in stored_list])
    restart = matched and options() == "restart"
    done = False

    for q in question_set:
        q[4] = True
        if q not in stored_list or restart:
            done = True 
            if q[1]:
                print(q[1])
            if q[2]:
                print(q[2])
            guess = input()
            while guess != q[3]:
                guess = repeat()
            if not matched:
                op = open("tests/wwpd_storage.py", "w")
                for j in range(len(stored_list)):
                    if q[0] < stored_list[j][0]:
                        stored_list.insert(j, q)
                        break
                if q not in stored_list: 
                    stored_list.append(q)
                op.write("wwpd_storage = " + str(stored_list))
                op.close()
    if done:
        complete()


# REFERENCE FUNCTIONS, CLASSES, METHODS, SEQUENCES, ETC.

# https://inst.eecs.berkeley.edu/~cs61a/su22/disc/disc04/

a = [1, 5, 4, [2, 3], 3]


# https://inst.eecs.berkeley.edu/~cs61a/su22/disc/disc04/

pokemon = {'pikachu': 25, 'dragonair': 148}


# QUESTION SET - ELEMENT FORMAT: [<QUESTION NUMBER>, <INITIAL PRINTS> (usually empty), <QUESTION>, <ANSWER>]
# INSPECT MODULE - convert function/class body into String: https://docs.python.org/3/library/inspect.html 
# wwpd questions

lists_qs = [
    [1, ">>> a = [1, 5, 4, [2, 3], 3]", ">>> print(a[0], a[-1])", "1 3"],
    [2, "", ">>> len(a)", str(len(a))],
    [3, "", ">>> 2 in a", str(2 in a)],
    [4, "", ">>> a[3][0]", str(a[3][0])]
]

dictionaries_qs = [
    [5, ">>> pokemon = {'pikachu': 25, 'dragonair': 148}", ">>> pokemon", str(pokemon)],
    [6, "", ">>> 'mewtwo' in pokemon", str('mewtwo' in pokemon)],
    [7, "", ">>> len(pokemon)", str(len(pokemon))],
    [8, ">>> pokemon['mew'] = pokemon['pikachu']\n>>> pokemon[25] = 'pikachu'", ">>> pokemon", "{'pikachu': 25, 'dragonair': 148, 'mew': 25, 25: 'pikachu'}"],
    [9, ">>> pokemon['mewtwo'] = pokemon['mew'] * 2", ">>> pokemon", "{'pikachu': 25, 'dragonair': 148, 'mew': 25, 25: 'pikachu', 'mewtwo': 50}"],
    [10, "", ">>> pokemon[['firetype', 'flying']] = 146", "error"]
]

list_mutation_qs = [
    [11, ">>> lst = [5, 6, 7, 8]", ">>> lst.append(6)", "nothing"],
    [12, "", ">>> lst", "[5, 6, 7, 8, 6]"],
    [13, ">>> lst.insert(0, 9)", ">>> lst", "[9, 5, 6, 7, 8, 6]"],
    [14, ">>> x = lst.pop(2)", ">>> lst", "[9, 5, 7, 8, 6]"],
    [15, ">>> lst.remove(x)", ">>> lst", "[9, 5, 7, 8]"],
    [16, ">>> a, b = lst, lst[:]", ">>> a is lst", "True"],
    [17, "", ">>> b == lst", "True"],
    [18, ">>> lst = [1, 2, 3]\n>>> lst.extend([4,5])", ">>> lst", "[1, 2, 3, 4, 5]"],
    [19, ">>> lst.extend([lst.append(9), lst.append(10)])", ">>> lst", "[1, 2, 3, 4, 5, 9, 10, None, None]"]
]

all_qs = [lists_qs, dictionaries_qs, list_mutation_qs]

for set in all_qs:
    for q in set:
        q.append(False)


# WWPD? QUESTIONS 

def wwpd_lists():
    wwpd("Lists", lists_qs, st)

def wwpd_dictionaries():
    wwpd("Dictionaries", dictionaries_qs, st)

def wwpd_list_mutation():
    wwpd("List Mutation", list_mutation_qs, st)
