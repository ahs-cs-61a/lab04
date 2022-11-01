# lab04 tests

import labs.lab04 as lab
import re
import inspect


def test_ban_iteration():
    count_palindromes_text = inspect.getsource(lab.count_palindromes)
    count_palindromes_search = re.search(r"(while|for).*:{1}", count_palindromes_text)
    assert count_palindromes_search is None # iteration detected in count_palindromes
    remove_odd_text = inspect.getsource(lab.remove_odd_indices)
    remove_odd_search = re.search(r"(while|for).*:{1}", remove_odd_text)
    assert remove_odd_search is None # iteration detected in remove_odd_indices 


def test_ban_recursion():
    count_palindromes_text = inspect.getsource(lab.count_palindromes)   
    count = 0
    while "count_palindromes" in count_palindromes_text:
        index = count_palindromes_text.index("count_palindromes")
        count += 1
        count_palindromes_text = count_palindromes_text[index + len("count palindromes"):]
    assert count <= 2 # recursion detected in count_palindromes


def test_map_new():
    assert lab.map_new(lambda x: x*x, [1, 2, 3]) == [1, 4, 9]
    assert lab.map_new(lambda x: x + 6, [6, 2, 3]) == [12, 8, 9]


def test_filter_new():
    assert lab.filter_new(lambda x: x % 2 == 0, [1, 2, 3, 4]) == [2, 4]
    assert lab.filter_new(lambda x: x > 5, [1, 2, 3, 4]) == []


def test_reduce_new():
    assert lab.reduce_new(lambda x, y: x + y, [1, 2, 3, 4]) == 10
    assert lab.reduce_new(lambda x, y: x * y, [1, 2, 3, 4]) == 24
    assert lab.reduce_new(lambda x, y: x * y, [4]) == 4
    assert lab.reduce_new(lambda x, y: x + 2 * y, [1, 2, 3]) == 11


def test_even_weighted():
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 3, 5, 8]
    assert lab.even_weighted(x) == [0, 6, 20]
    assert lab.even_weighted(y) == [24]


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
    assert lab.couple([1, 2, 3], [1, 2, 3]) == [[1, 4], [2, 5], [3, 6]]
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