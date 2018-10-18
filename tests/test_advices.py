#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytest
import ipytest

from unittest.mock import Mock

from gampy import advices


# In[2]:


div10 = lambda x: 10 / x

gdict = lambda x: {0: 0, 1: 1}.get(x)


# In[3]:


def test_identical():
    f = advices.identical()(div10)

    assert f(5) == 2
    assert f(10) == 1
    assert f == div10

    with pytest.raises(ZeroDivisionError):
        f(0)


# In[4]:


def test_cacheable():
    mock = Mock(return_value=10)
    f = advices.cacheable()(mock)

    assert f(5) == 10
    assert f(5) == 10
    assert f(10) == 10
    assert f(10) == 10

    assert mock.call_count == 2


# In[5]:


def test_constable():
    f = advices.constable(9)(div10)

    assert f(0) == 9
    assert f(5) == 9
    assert f(10) == 9


# In[6]:


def test_flippable():
    f = advices.flippable()(pow)

    assert f(2, 3) == 9
    assert f(3, 2) == 8


# In[7]:


def test_fluentable():
    f = advices.fluentable()(list.append)
    l = list()

    f(f(f(l, 0), 1), 2)

    assert l == [0, 1, 2]


# In[8]:


def test_preable():
    mock = Mock()
    f = advices.preable(mock)(div10)

    assert mock.call_count == 0
    assert f(5) == 2
    assert f(10) == 1
    assert mock.call_count == 2


# In[9]:


def test_postable():
    mock = Mock()
    f = advices.postable(mock)(div10)

    assert mock.call_count == 0
    assert f(5) == 2
    assert f(10) == 1
    assert mock.call_count == 2


# In[10]:


def test_optional():
    f = advices.optional(9)(gdict)

    assert f(0) == 0
    assert f(5) == 9


# In[18]:


def test_retryable():
    mock = Mock(side_effect=IndexError)
    advice = advices.retryable()
    f = advice(div10)
    g = advice(mock)

    assert f(0) == None
    assert f(5) == 2

    assert g(0) == None
    assert g(5) == None

    assert mock.call_count == 6


# In[12]:


def test_exceptional():
    f = advices.exceptional(9)(div10)

    assert f(0) == 9
    assert f(5) == 2


# In[13]:


def test_loggable():
    mock = Mock()
    f = advices.loggable(mock)(int)

    assert f(0) == 0
    assert f(1) == 1

    assert mock.call_args_list == [
        (("enter: int",), {}),
        (("exit: int",), {}),
        (("enter: int",), {}),
        (("exit: int",), {}),
    ]


# In[14]:


def test_traceable():
    mock = Mock()
    f = advices.traceable(mock, True, True)(int)

    assert f(0) == 0
    assert f(1) == 1

    assert mock.call_args_list == [
        (("[PRE] int(0)",), {}),
        (("[POST] int(0) -> 0",), {}),
        (("[PRE] int(1)",), {}),
        (("[POST] int(1) -> 1",), {}),
    ]


test_traceable()


# In[20]:


ipytest.run_tests()
