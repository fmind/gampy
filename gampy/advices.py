#!/usr/bin/env python
# coding: utf-8

# In[5]:


"""Advices of the project."""

# import logging

# from functools import wraps, lru_cache


# In[ ]:


def identical():
    """Return f as is."""

    def advice(f):
        return f

    return advice


# In[ ]:


# def preable(do):
#     """Call do before f."""

#     def advice(f):
#         @wraps(f)
#         def wrapped(*args, **kwargs):
#             do()

#             return f(*args, **kwargs)

#         return wrapped

#     return advice


# In[ ]:


# def postable(do):
#     """Call do after f."""

#     def advice(f):
#         @wraps(f)
#         def wrapped(*args, **kwargs):
#             state = f(*args, **kwargs)
#             do()

#             return state

#         return wrapped

#     return advice


# In[4]:


# In[5]:


# def optional(x=None):
#     """Return x when f return None."""

#     def advice(f):
#         @wraps(f)
#         def wrapped(*args, **kwargs):
#             state = f(*args, **kwargs)

#             if state is None:
#                 return x

#             return state

#         return wrapped

#     return advice


# In[7]:


# def exceptional(x=None, on=Exception):
#     """Return x when f raises an exception."""

#     def advice(f):
#         @wraps(f)
#         def wrapped(*args, **kwargs):
#             try:
#                 return f(*args, **kwargs)
#             except on:
#                 return x

#         return wrapped

#     return advice


# In[15]:


# def loggable(pre=True, post=False, level=logging.DEBUG):
#     """Log f before and/or after call."""

#     def advice(f):
#         @wraps(f)
#         def wrapped(*args, **kwargs):
#             strf = f.__name__

#             if pre:
#                 logging.log(level, "enter: %s", strf)

#             state = f(*args, **kwargs)

#             if post:
#                 logging.log(level, "exit: %s", strf)

#             return state

#         return wrapped

#     return advice


# In[9]:


# def traceable(pre=True, post=False):
#     """Print f trace before and/or after call."""

#     def advice(f):
#         @wraps(f)
#         def wrapped(*args, **kwargs):
#             strf = f.__name__
#             strargs = [str(x) for x in args]
#             strkwargs = ["{0}={1}".format(k, v) for k, v in kwargs.items()]
#             inittrace = "{0}({1})".format(strf, ",".join(strargs + strkwargs))

#             if pre:
#                 print("[PRE] {}".format(inittrace))

#             state = f(*args, **kwargs)

#             if post:
#                 exittrace = str(state)
#                 print("[POST] {} -> {}".format(inittrace, exittrace))

#             return state

#         return wrapped

#     return advice


# In[16]:


# def cacheable(maxsize=128, typed=False):
#     """Cache the most recent function results."""
#     return lru_cache(maxsize, typed)


# In[2]:


# def flippable():
#     """Flip f arguments."""

#     def advice(f):
#         @wraps(f)
#         def wrapped(*args, **kwargs):
#             return f(*reversed(args), **kwargs)

#         return wrapped

#     return advice


# In[3]:


# def constable(x=None):
#     """Return x constantly."""

#     def advice(f):
#         @wraps(f)
#         def wrapped(*args, **kwargs):
#             f(*args, **kwargs)

#             return x

#         return wrapped

#     return advice


# In[4]:


# def fluentable(n=1):
#     """Return the n argument after f."""

#     def advice(f):
#         @wraps(f)
#         def wrapped(*args, **kwargs):
#             f(*args, **kwargs)

#             if len(args) >= n:
#                 return args[n]

#             return None

#         return wrapped

#     return advice
