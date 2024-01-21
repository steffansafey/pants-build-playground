# Pants Build Playground

A repo with the sole purpose of mucking around with [Pants Build](https://www.pantsbuild.org/). 

`server` is a basic web server running on `:8000` that does very little.

# How to

### Run fmt, lint, mypy, tests
``` bash
pants fmt :: && pants lint :: && pants check :: && pants test ::
```

Despite the `::` globs, Pants is smart about what it'll actually execute, e.g. only running tests dependent on files that have changed.

### Package a `.pex` executable

``` bash
pants package server
```