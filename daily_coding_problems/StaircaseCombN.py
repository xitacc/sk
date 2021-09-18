import math
import sys
import os
from typing import List, Tuple

import numpy as np
import math
import itertools
from itertools import *
from typing import *
from operator import itemgetter

class Person():
    def __init__(self):
        self.id = 0
STR = TypeVar('', int, str)
def stairs_climb_fewest(allowed_steps: set[int], n_stairs: int):
    li_allowed_steps = list(allowed_steps)
    li_allowed_steps.sort(reverse=True)  # von groß zu klein sortiert
    rest_stairs = n_stairs
    fewest_steps = list()
    for index, step in enumerate(li_allowed_steps):
        n_step = rest_stairs // step  # n_step ist schon abgerundet
        rest_stairs = rest_stairs - (n_step * step)
        if rest_stairs == 0:
            [fewest_steps.append(step) for i in range(n_step)]
            return fewest_steps
        if rest_stairs > 0:
            if index == len(li_allowed_steps) - 1:
                fewest_steps.pop()
            [fewest_steps.append(step) for i in range(n_step)]

def stairs_climb_fewest(allowed_steps: set[int], n_stairs: int):
    li_allowed_steps = list(allowed_steps)
    li_allowed_steps.sort(reverse=True)  # von groß zu klein sortiert
    rest_stairs = n_stairs
    fewest_steps = list()
    for index, step in enumerate(li_allowed_steps):
        n_step = rest_stairs // step  # n_step ist schon abgerundet
        rest_stairs = rest_stairs - (n_step * step)
        if rest_stairs == 0:
            [fewest_steps.append(step) for i in range(n_step)]
            return fewest_steps
        if rest_stairs > 0:
            if index == len(li_allowed_steps) - 1:
                fewest_steps.pop()
            [fewest_steps.append(step) for i in range(n_step)]


def stairs_climb_perm(all_combn: set[tuple], n_stairs: int, allowed_steps: set[int]):
    if n_stairs < 1:
        return 0
    if n_stairs == 1:
        return 1
    fewest_steps = stairs_climb_fewest(allowed_steps, n_stairs)
    if len(fewest_steps) == 0:
        return 0
    unique_perm = set()
    for perm in permutations(fewest_steps):
        unique_perm.add(perm)

def stairs_climb_number(n: int, allowed_steps: set):
    pass




stairset = {()}
stairs_climb_perm(stairset, 33, {1, 2, 3, 7, 9})

def biggest_two(int_list: list[int]):
    max_li = list()
    try:
        assert len(int_list) > 0
    except AssertionError:
        return
    for idx, val in enumerate(int_list):
        ridx = idx + 2
        lidx = idx - 2
        right = int_list[ridx:]
        if lidx < 0:
            left = []
        else:
            left = int_list[:lidx + 1]
        leftadded = [(idx, idx_, item + val) for idx_, item in enumerate(left)]
        rightadded = [(idx, idx + 2 + idx_, item + val) for idx_, item in enumerate(right)]
        max_li.append(max(leftadded + rightadded, key=itemgetter(2), default=None))
    return max(max_li, key=itemgetter(2), default=None)
max_li = biggest_two([3,4,5,6,7,8,9,88,888])
print(biggest_two([]))
# print(max_li)
int_li=[33,45,66,77,88]


int_li2=[2,22,123,124,125,25]
int_li3=[5,20,2,5,2,5]
int_li3=[100,1,1,100]
def max_nonadjacent(int_list: list[int]):
    selected_ints = []
    sub_int_list = int_list[1:-1]
    for idx, val in enumerate(sub_int_list):
        last_val = int_list[idx]
        next_val = int_list[idx + 2]


        lpr_val = next_val + last_val
        if lpr_val > val:
            selected_ints.append((idx, last_val))
            selected_ints.append((idx + 2, next_val))
        else:
            selected_ints.append((idx, val))
    return selected_ints
print(max_nonadjacent(int_list=int_li3))

print(stairs_climb_fewest({99, 2}, 300))

from functools import reduce


# The Data
s = {1, 2, 3, 4, 5}


# The One-Liner
ps = lambda s: reduce(lambda P, x: P + [subset | {x} for subset in P], s, [set()])


# The Result
print(ps(s))

def all_subsets(in_set: set):
    ret_set = set()
    ret_set.add(frozenset())
    for item in in_set:
        ret_set.add(item)

    return ret_set
print(all_subsets({1,2,3}))