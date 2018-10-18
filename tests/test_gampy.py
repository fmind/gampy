#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pytest
import ipytest

from gampy import Pipeline, advices


# In[11]:


def test_pipeline():
    p = Pipeline(
        [(map, [lambda x: x ** 2], {}), (filter, [lambda x: x > 2]), (list,), max]
    )

    assert p()(range(10)) == 81


# In[20]:


def test_advices():
    p = Pipeline(
        [(map, [lambda x: x ** 2], {}), (filter, [lambda x: x > 2]), lambda x: None]
    )

    p = p @ advices.optional([1, 2, 3])

    return p()(range(10)) == [1, 2, 3]


# In[21]:


ipytest.run_tests()
