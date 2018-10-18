#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytest
import ipytest

from functools import reduce

from gampy.structures import Pipeline
from gampy.errors import DefinitionError, CompositionError


# In[2]:


def inc(x):
    return x + 1


def add(a, b):
    return a + b


def iseven(x):
    return x % 2 == 0


# In[3]:


P00 = Pipeline([(map, [inc])])

P01 = Pipeline([(filter, [iseven])])

P02 = Pipeline([list])

P0 = Pipeline([(map, [inc], {}), (filter, [iseven]), (list,)])

P1 = Pipeline([(reduce, [add])])


# In[4]:


def test_init():
    assert Pipeline([map])
    assert Pipeline([(map,)])
    assert Pipeline([(map, [])])
    assert Pipeline([(map, [], {})])

    with pytest.raises(DefinitionError) as err:
        Pipeline([0])
    assert str(err.value) == "A step should be Callable or Iterable. Not: int."

    with pytest.raises(DefinitionError) as err:
        Pipeline([()])
    assert str(err.value) == "A tuple step should contain 1, 2 or 3 items. Not: 0."

    with pytest.raises(DefinitionError) as err:
        Pipeline([(map, [], {}, 0)])
    assert str(err.value) == "A tuple step should contain 1, 2 or 3 items. Not: 4."

    with pytest.raises(DefinitionError) as err:
        Pipeline([(0, [], {})])
    assert str(err.value) == "The first step argument should be Callable. Not: int."

    with pytest.raises(DefinitionError) as err:
        Pipeline([(map, 0, {})])
    assert str(err.value) == "The second step argument should be Iterable. Not: int."

    with pytest.raises(DefinitionError) as err:
        Pipeline([(map, [], 0)])
    assert str(err.value) == "The third step argument should be Mapping. Not: int."


# In[5]:


def test_hash():
    assert hash(P0) != hash(P1)


# In[6]:


def test_getter():
    assert P0.steps == [(map, [inc], {}), (filter, [iseven], {}), (list, [], {})]


# In[7]:


def test_setter():
    p = Pipeline([])
    p.steps = [(map, [inc])]

    assert p == P00


# In[8]:


def test_context():
    pipeline = Pipeline([(range, [10])])

    with pipeline as p:
        p.append((map, [inc]))
        p.append((reduce, [add]))

    assert pipeline.steps == [(range, [10], {}), (map, [inc], {}), (reduce, [add], {})]


# In[9]:


def test_or():
    assert (P1 | list | set) == Pipeline(
        [(reduce, [add], {}), (list, [], {}), (set, [], {})]
    )


test_or()


# In[10]:


def test_and():
    assert P0 & P01 == P01


# In[11]:


def test_xor():
    assert (P0 ^ P01) == (P00 + P02)


# In[12]:


def test_add():
    assert P00 + P01 + P02 == P0


# In[13]:


def test_sub():
    assert P0 - P01 == P00 + P02


# In[14]:


def test_mul():
    assert P0 * 2 == Pipeline(
        [
            (map, [inc], {}),
            (filter, [iseven], {}),
            (list, [], {}),
            (map, [inc], {}),
            (filter, [iseven], {}),
            (list, [], {}),
        ]
    )


# In[15]:


def test_matmul():
    def advice(f):
        def wrapped(*args, **kwargs):
            return 10

        return wrapped

    p = P0 @ advice
    f = p()

    assert f(0, k=1) == 10


# In[16]:


def test_truediv():
    assert P0 / 2 == [P00 + P01, P02]


# In[17]:


def test_floordiv():
    assert P0 // 2 == [P00 + P01]


# In[18]:


def test_mod():
    assert P0 % P1 == P00 + P1 + P01 + P02


# In[19]:


def test_str():
    assert str(P0) == "map -> filter -> list"


# In[20]:


def test_repr():
    assert repr(P02) == "[(<class 'list'>, [], {})]"


# In[21]:


def test_bool():
    assert P0 and P1
    assert not Pipeline([])


# In[22]:


def test_call():
    with pytest.raises(CompositionError) as err:
        Pipeline([])()
    assert str(err.value) == "Cannot compose from an empty pipeline."

    assert P1()(range(10)) == 45
    assert P0()(range(10)) == [2, 4, 6, 8, 10]


# In[23]:


def test_len():
    assert len(P1) == 1
    assert len(P0) == 3


# In[24]:


def test_iter():
    assert list(iter(P0)) == P0.steps


# In[25]:


def test_getitem():
    assert P0[0] == (map, [inc], {})
    assert P0[1] == (filter, [iseven], {})
    assert P0[2] == (list, [], {})

    with pytest.raises(IndexError):
        P0[3]


# In[26]:


def test_contains():
    assert (list, [], {}) in P0
    assert (map, [inc], {}) in P0
    assert (filter, [iseven], {}) in P0

    assert (reduce, [add]) not in P0


# In[27]:


def test_reversed():
    assert reversed(P0).steps == [
        (list, [], {}),
        (filter, [iseven], {}),
        (map, [inc], {}),
    ]


# In[28]:


def test_lt():
    assert not P0 < P1
    assert P1 < P0
    assert not P0 < P0


# In[29]:


def test_gt():
    assert P0 > P1
    assert not P1 > P0
    assert not P0 > P0


# In[30]:


def test_le():
    assert not P0 <= P1
    assert P1 <= P0
    assert P0 <= P0


# In[31]:


def test_ge():
    assert P0 >= P1
    assert not P1 >= P0
    assert P0 >= P0


# In[32]:


def test_eq():
    assert not P0 == P1
    assert P0 == P0


# In[33]:


def test_ne():
    assert P0 != P1
    assert not P0 != P0


# In[34]:


def test_pow():
    assert P0 ** P0
    assert not P0 ** P1
    assert P0 == Pipeline([map, filter, list])


# In[35]:


def test_lshift():
    assert not P0 << P1
    assert not P1 << P0
    assert not P0 << P00
    assert P00 << P0
    assert P0 << P0


# In[36]:


def test_rshift():
    assert not P0 >> P1
    assert not P1 >> P0
    assert P0 >> P00
    assert not P00 >> P0
    assert P0 >> P0


# In[37]:


ipytest.run_tests()
