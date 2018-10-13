#!/usr/bin/env python
# coding: utf-8

# In[8]:


"""Definition of Program class."""

from typing import Mapping, Iterable, Callable

from gampy.errors import DefinitionError


class Program(object):
    """A Program is a sequence of steps."""

    def __init__(self, steps):
        """Initialize the program steps."""
        self.steps = steps  # trigger setter

    # PROPERTY

    @property
    def steps(self):
        """Return the program steps."""
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Assign the program steps."""
        self._steps = []

        for s in steps:
            # fill blanks
            if len(s) == 1:
                step = (s[0], list(), dict())
            elif len(s) == 2:
                step = (s[0], s[1], dict())
            elif len(s) == 3:
                step = (s[0], s[1], s[2])
            else:
                raise DefinitionError("A step should contain 1, 2 or 3 arguments, not {} arguments.".format(
                    len(steps)))

            # validate steps
            if not isinstance(step[0], Callable):
                raise DefinitionError("The 1st step argument should be a Callable, not a {}.".format(
                    type(step[0]).__name__))
            elif not isinstance(step[1], Iterable):
                raise DefinitionError("The 2nd step argument should be an Iterable, not a {}".format(
                    type(step[1]).__name__))
            elif not isinstance(step[2], Mapping):
                raise DefinitionError("The 3rd step argument should be Mapping, not a {}".format(
                    type(step[2]).__name__))

            self._steps.append(step)

    # FORMAT

    def __str__(self):
        """Return a string from the program steps."""

        def fmt(step):
            f, args, kwargs = step

            strf = f.__name__
            strargs = [str(x) for x in args]
            strkwargs = ["{0}={1}".format(k, v) for k, v in kwargs.items()]

            return "{0}({1})".format(strf, ",".join(strargs + strkwargs))

        return "\n".join(map(fmt, self.steps))

    def __repr__(self):
        """Return a representation of the program steps."""
        return str(self.steps)

    # OPERATION

    def __add__(self, other):
        """Concatenate program steps."""
        return self.__class__(self.steps + other.steps)

    def __sub__(self, other):
        """Filter common program steps."""
        return self.__class__(s for s in self.steps if s not in other.steps)

#     def __mul__(self, n):
#         """Duplicate program steps."""
#         return self.__class__(self._steps * 2)

#     def __matmul__(self, g):
#         """Compose program functions."""
#         return self.__class__((g(f), args, kwargs) for f, args, kwargs in self.steps)

#     def __truediv__(self, n):
#         """Chunk steps in smaller programs."""
#         chunk = []

#         for i, s in enumerate(self.steps, 1):
#             chunk.append(s)

#             if i % n == 0:
#                 yield self.__class__(*chunk)
#                 chunk.clear()

#     def __floordiv__(self, n):
#         """Chunk all steps in smaller programs."""
#         chunk = []

#         for i, x in enumerate(self.steps, 1):
#             chunk.append(x)

#             if i % n == 0:
#                 yield self.__class__(*chunk)
#                 chunk.clear()

#         if chunk:
#             yield self.__class__(*chunk)

#     def __mod__(self, other):
#         """Alternate program steps."""
#         gen = it.chain.from_iterable(it.zip_longest(self.steps, other.steps))

#         steps = [s for s in gen if s is not None]

#         return self.__class__(steps)

#     def __pow__(self, other):
#         pass

#     def __lshift__(self, n):
#         """Shift program steps to the left."""
#         return self.__class__(self.steps[n:] + self.steps[:n])

#     def __rshift__(self, n):
#         """Shift program steps to the right."""
#         return self.__class__(self.steps[-n:] + self.steps[:-n])

#     def __and__(self, other):
#         """Intersect program steps."""
#         steps = []

#         for s in self.steps:
#             if s in other:
#                 steps.append(s)

#         return self.__class__(steps)

#     def __xor__(self, other):
#         """Symmetric program steps."""
#         return (self + other) - (self & other)

#     def __or__(self, other):
#         pass

    # INPLACE

    def __iadd__(self, other):
        """Concatenante program steps."""
        self._steps += other.steps

    def __isub__(self, other):
        """Filter common program steps."""
        self._steps = [s for s in self.steps if s not in other.steps]

#     def __imul__(self, n):
#         """Duplicate program steps"""
#         self._steps = self.steps * n

#     def __imatmul__(self, g):
#         """Combine program functions."""
#         self._steps = [(g(f), args, kwargs) for f, args, kwargs in self.steps]

#     def __imod__(self, other):
#         """Alternate program steps."""
#         gen = it.chain.from_iterable(it.zip_longest(self.steps, other.steps))

#         self._steps = [s for s in gen if s is not None]

#     def __ipow__(self, other):
#         pass

#     def __ilshift__(self, n):
#         """Shift program steps to the left."""
#         self._steps = self.steps[n:] + self.steps[:n]

#     def __irshift__(self, n):
#         """Shift program steps to the right."""
#         self.steps = self.steps[-n:] + self.steps[:-n]

#     def __iand__(self, other):
#         """Intersect program steps."""
#         steps = []

#         for s in self.steps:
#             if s in other:
#                 steps.append(s)

#         self._steps = steps

#     def __ixor__(self, other):
#         """Symmetric program steps."""
#         self._steps = (self ^ other).steps

#     def __ior__(self, other):
#         pass

#     # CONTEXT

    def __enter__(self):
        """Return the program steps."""
        return self.steps

    def __exit__(self, exc_type, exc_value, traceback):
        """Update the program steps."""
        self.steps = self._steps  # trigger setter

#     # CALLABLE
#     def __call__(self, state, control=None):
#         """Execute program steps."""
#         try:
#             for step in self.steps:
#                 if control is not None:
#                     step, state = control(step, state)

#                 f, args, kwargs = step
#                 state = f(*args, **kwargs)

#             return state
#         except Exception as err:
#             raise ExecutionError() from err

    # CONVERTION
    
    def __int__(self)
        """Return the number of steps in the program."""
        return len(self)

    def __bool__(self):
        """Return True if program is not empty."""
        return len(self.steps) > 0
    
    def __list__(self):
        """Return the steps of the programs."""
        return self.steps

    # COLLECTION

    def __len__(self):
        """Return the number of steps."""
        return len(self.steps)

    def __iter__(self):
        """Iterate over the program steps."""
        return iter(self.steps)

    def __reversed__(self):
        """Reverse the steps of the program."""
        return self.__init__(*reversed(self.steps))

    def __getitem__(self, n):
        """Return the nth step of the program."""
        return self.steps[n]

    def __delitem__(self, n):
        """Delete the nth step of the program."""
        del self.steps[n]

    def __setitem__(self, n, step):
        """Change the nth step of the program."""
        self.steps[n] = step

    def __contains__(self, step):
        """Return True if step exists in the program."""
        return step in self.steps

    # COMPARISON

    def __lt__(self, other):
        """Compare the program lengths with <."""
        return len(self) < len(other)

    def __le__(self, other):
        """Compare the program lengths with <=."""
        return len(self) <= len(other)

    def __eq__(self, other):
        """Compare the program lengths with ==."""
        return len(self) == len(other)

    def __ne__(self, other):
        """Compare the program lengths with !=."""
        return len(self) != len(other)

    def __ge__(self, other):
        """Compare the program lengths with >=."""
        return len(self) >= len(other)

    def __gt__(self, other):
        """Compare the program lengths with >."""
        return len(self) > len(other)

