# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from GF2 import one, zero




## 1: (Problem 3.8.1) Vector Comprehension and Sum
def vec_select(veclist, k):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    '''
    return [v for v in veclist if v[k] == 0]


def vec_sum(veclist, D):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    '''
    
    # why is this incorrect ???? return sum([Vec(D, v.f) for v in veclist]) and  return sum([v for v in veclist]) 
    vs = Vec(D,{})
    for v in veclist:
        vs += v
    return vs



def vec_select_sum(veclist, k, D):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    '''
    return vec_sum(vec_select(veclist, k), D)



## 2: (Problem 3.8.2) Vector Dictionary
def scale_vecs(vecdict):
    '''
    >>> v1 = Vec({1,2,4}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> result = scale_vecs({3: v1, 5: v2})
    >>> len(result)
    2
    >>> [v in [Vec({1,2,4},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})] for v in result]
    [True, True]
    '''
    return [zero_vec(v.D) if k == 0 else (1/k) * v for k, v in vecdict.items()]



## 3: (Problem 3.8.3) Constructing a Span over GF(2)
def GF2_span(D, L):
    '''
    >>> from GF2 import one
    >>> D = {'a', 'b', 'c'}
    >>> result = GF2_span(D, [Vec(D, {'a': one, 'c': one}), Vec(D, {'c': one})])
    >>> len(result)
    4
    >>> [v in result for v in [Vec(D, {}),Vec(D, {'a': one, 'c': one}),Vec(D, {'c': one}),Vec(D, {'a':one})]
    [True, True, True, True]
    '''
    import itertools
    if not L: return zero_vec(D)
    coefficient_combinations = list(itertools.product([zero, one], repeat=len(L))) #product(A, B) returns the same as ((x,y) for x in A for y in B).
    return [sum(coefficient * l for coefficient, l in zip(coefficient_combination, L)) for coefficient_combination in coefficient_combinations]
    



## 4: (Problem 3.8.7) Is it a vector space 1
# Answer with a boolean, please.
is_a_vector_space_1 = False



## 5: (Problem 3.8.8) Is it a vector space 2
# Answer with a boolean, please.
is_a_vector_space_2 = True



## 6: (Problem 3.8.9) Is it a vector space 3
# Answer with a boolean, please.
is_a_vector_space_3 = False



## 7: (Problem 3.8.10) Is it a vector space 4
# Answer with a boolean, please.
is_a_vector_space_4a = True
is_a_vector_space_4b = False

