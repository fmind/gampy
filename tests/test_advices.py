#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pytest
import ipytest

from gampy import advices


# In[4]:


div10 = lambda x: 10 / x


# In[5]:


def test_identical():
    advice = advices.identical()
    f = advice(div10)

    assert f(5) == 2
    assert f(10) == 1


# In[ ]:


# def test_preable(capsys):
#     advice = advices.preable(lambda: print("pre"))
#     f = advice(div10)

#     assert (capsys)
#     assert f(5) == 2
#     assert f(10) == 1


# In[6]:


ipytest.run_tests()


# In[ ]:
