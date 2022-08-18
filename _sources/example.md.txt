---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Example

In this page, we demonstrate using some components

```{code-cell} ipython3
import todobricks
```


For this toy example, we'll write the todo file out from there first and then read it back in.
```{code-cell} ipython3
toy_list = ['x post example +todobricks @code due:2022-08-18',
            'x document bricks +todobricks @code due:2022-08-17',
            'write sample function doc strings @prismia +todobricks',
            'write up answers to questions +tdadmin @prismia']
```

Then we can write it out

```{code-cell} ipython3
todobricks.write_file(toy_list,'todo.txt')
```

and we can read it in

```{code-cell} ipython3
todobricks.read_txt_file('todo.txt')
```

To save it to a variable to use it, we use assignment

```{code-cell} ipython3
todo_list_read = todobricks.read_txt_file('todo.txt')
```

Then we can split it to be able to work with it

```{code-cell} ipython3
todo_list = todobricks.split_txt_file(todo_list_read)
```
