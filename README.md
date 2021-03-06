# Gampy

Gampy provides experimental constructs to improve your Python programs.

## Pipeline

While functional programming is a great paradigm to create data pipelines, some operations remains hard to express:
- wrap every function of a data pipeline with an external function (e.g. logging, safe exception handling ...)
- concatenate and transform data pipelines with algebra operators (e.g. convert and compare a pipeline ...)
- apply the `compose` and `partial` operators on a data pipeline to create a single callable function

Gampy Pipeline is a data structure created to address these problems.

Here is an example of a simple pipeline:

```python
from gampy.structures import Pipeline

pipeline = Pipeline([
    (map, [lambda x: x + 1], {}),
    (filter, [lambda x: x % 2 == 0]),
    (list,)
])
```

Each **step** of the pipeline is represented as a 3-tuple: `(function, arguments, keyword arguments)`. While `function` is mandatory, `arguments` and `keyword argument` will be replaced by `list()` and `dict()` respectively if they are missing. This structure allows the creation of **unevaluated expression**, that can be further transformed prior to their execution.

The most interesting operations over a pipeline are `()` (call) and `@` (matmul).

`Call` converts the pipeline into a single function. This process is divided in two steps:
- `functools.partial` is applied on each step arguments to create a single function per step
- functions are composed two by two with `functools.reduce` to create a single function per pipeline

```python
>>> f = pipeline()
>>> f(range(10))
30
```

`Matmul` applies **an advice** to each function of the pipeline. This allows the expression of cross concern aspects.

In the snippet below, any exception raised by a pipeline function will return `None`.

```python
from gampy.advices import exceptional

safepipe = pipeline @ exceptional(None)
```

An advice is similar to a **parametrized decorator**, which create a function that takes a function and replaced it by a new function. The purpose is to extend the behavior of the original function.

```python
def exceptional(x: Any = None, on: Type[Exception] = Exception) -> Advice:
    """Return x when f raises an exception."""

    def advice(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except on:
                return x

        return wrapped

    return advice
```
