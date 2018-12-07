#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""Errors of the project."""


class Error(Exception):
    """Base class for errors."""


class DefinitionError(Error):
    """Error during definition."""


class CompositionError(Error):
    """Error during composition."""
