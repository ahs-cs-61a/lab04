# lab04 tests


# IMPORTS

import labs.lab04 as lab
import tests.wwpd_storage as s
import re
import inspect
import git

st = s.wwpd_storage


# COLORED PRINTS - custom text type to terminal: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal, ANSI colors: http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

class bcolors:
    HIGH_MAGENTA = '\u001b[45m'
    HIGH_GREEN = '\u001b[42m'
    HIGH_YELLOW = '\u001b[43m'
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


# TESTS

def test_map_new():
    assert lab.map_new(lambda x: x * x, [1, 2, 3]) == [1, 4, 9]
    assert lab.map_new(lambda x: x + 6, [6, 2, 3]) == [12, 8, 9]


def test_filter_new():
    assert lab.filter_new(lambda x: x % 2 == 0, [1, 2, 3, 4]) == [2, 4]
    assert lab.filter_new(lambda x: x > 5, [1, 2, 3, 4]) == []


def test_reduce_new():
    assert lab.reduce_new(lambda x, y: x + y, [1, 2, 3, 4]) == 10
    assert lab.reduce_new(lambda x, y: x * y, [1, 2, 3, 4]) == 24
    assert lab.reduce_new(lambda x, y: x * y, [4]) == 4
    assert lab.reduce_new(lambda x, y: x + 2 * y, [1, 2, 3]) == 11


def test_count_palindromes():
    assert lab.count_palindromes(("Acme", "Madam", "Pivot", "Pip")) == 2

    # BAN ITERATION
    count_palindromes_text = inspect.getsource(lab.count_palindromes)
    count_palindromes_search = re.search(r"(while|for).*:{1}", count_palindromes_text)
    if count_palindromes_search is not None:
        print_error("Iteration detected in count_palindromes; please implement without using.")
    assert count_palindromes_search is None

    # BAN RECURSION
    count_palindromes_text = inspect.getsource(lab.count_palindromes)   
    count = 0
    while "count_palindromes" in count_palindromes_text:
        index = count_palindromes_text.index("count_palindromes")
        count += 1
        count_palindromes_text = count_palindromes_text[index + len("count palindromes"):]
    if count > 2:
        print_error("Recursion detected in count_palindromes; please implement with using.")
    assert count <= 2 

    
def test_even_weighted():
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 3, 5, 8]
    assert lab.even_weighted(x) == [0, 6, 20]
    assert lab.even_weighted(y) == [0, 10]


def test_max_product():
    assert lab.max_product([10,3,1,9,2]) == 90
    assert lab.max_product([5,10,5,10,5]) == 125
    assert lab.max_product([]) == 1


def test_flatten():
    assert lab.flatten([1, 2, 3]) == [1, 2, 3]
    x = [1, [2, 3], 4]
    y = lab.flatten(x) 
    assert y == [1, 2, 3, 4]
    assert x == [1, [2, 3], 4]
    w = [[1, [1, 1]], 1, [1, 1]]
    z = lab.flatten(w)
    assert z == [1, 1, 1, 1, 1, 1]
    assert w == [[1, [1, 1]], 1, [1, 1]]


def test_insert_items():
    assert lab.insert_items([1, 5, 8, 5, 2, 3], 5, 7) == [1, 5, 7, 8, 5, 7, 2, 3]
    assert lab.insert_items([1, 2, 1, 2, 3, 3], 3, 4) == [1, 2, 1, 2, 3, 4, 3, 4]
    large_lst = [1, 4, 8]
    large_lst2 = lab.insert_items(large_lst, 4, 4)
    assert large_lst2 == [1, 4, 4, 8]
    large_lst3 = lab.insert_items(large_lst2, 4, 6)
    assert large_lst3 == [1, 4, 6, 4, 6, 8]
    assert large_lst3 is large_lst


def test_couple():
    assert lab.couple([1, 2, 3], [4, 5, 6]) == [[1, 4], [2, 5], [3, 6]]
    assert lab.couple(['c', 6], ['s', '1']) == [['c', 's'], [6, '1']]
    

def test_merge():
    assert lab.merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert lab.merge([], [2, 4, 6]) == [2, 4, 6]
    assert lab.merge([1, 2, 3], []) == [1, 2, 3]
    assert lab.merge([5, 7], [2, 4, 6]) == [2, 4, 5, 6, 7]
    assert lab.merge([2, 3, 4], [2, 4, 6]) == [2, 2, 3, 4, 4, 6]


def test_remove_odd_indices():
    s = [1, 2, 3, 4]
    t = lab.remove_odd_indices(s, True)
    assert s == [1, 2, 3, 4]
    assert t == [1, 3]
    l = [5, 6, 7, 8]
    m = lab.remove_odd_indices(l, False)
    assert l == [5, 6, 7, 8]
    assert m == [6, 8]
    assert lab.remove_odd_indices([9, 8, 7, 6, 5, 4, 3], False) == [8, 6, 4]
    assert lab.remove_odd_indices([2], False) == []

    # BAN ITERATION
    remove_odd_text = inspect.getsource(lab.remove_odd_indices)
    remove_odd_search = re.search(r"(while|for).*:{1}", remove_odd_text)
    if remove_odd_search is not None:
        print_error("Iteration detected in remove_odd_indices; implement without using.")
    assert remove_odd_search is None 


# CHECK WWPD? IS ALL COMPLETE

wwpd_complete = True

def test_wwpd():
    if len(st) != 19 or not all([i[4] for i in st]):
        print_error("WWPD? is incomplete.")
        wwpd_complete = False
    assert len(st) == 19
    assert all([i[4] for i in st])


# AUTO-COMMIT WHEN ALL TESTS ARE RAN

user = []

def test_commit():
    try:
        # IF CHANGES ARE MADE, COMMIT TO GITHUB
        user.append(input("\n\nWhat is your GitHub username (exact match, case sensitive)?\n"))
        repo = git.Repo("/workspaces/lab04-" + user[0])
        repo.git.add('--all')
        repo.git.commit('-m', 'update lab')
        origin = repo.remote(name='origin')
        origin.push()
        print_success("Changes successfully committed.")  
    except git.GitCommandError: 
        # IF CHANGES ARE NOT MADE, NO COMMITS TO GITHUB
        print_message("Already up to date. No updates committed.")
    except git.NoSuchPathError:
        # IF GITHUB USERNAME IS NOT FOUND
        print_error("Incorrect GitHub username; try again.")
        raise git.NoSuchPathError("")