#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Error(Exception):
    """Base class for errors."""
    pass


class ExecutionError(Error):
    """Error of program execution."""
    pass


class DefinitionError(Error):
    """Error of program definition."""
    pass