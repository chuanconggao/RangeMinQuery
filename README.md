# Implementation in Python for Range Minimum Query Problem

This data structure solves the [range minimum query problem](https://en.wikipedia.org/wiki/Range_minimum_query) of finding the minimal value in a sub-array of an array of comparable objects.

Use `SegmentTree()` to initialize the tree with a list of keys, in **comparable and hashable** type. `func` specifies how the best value is computed for any range of keys. `default` specifies the default value for each key. `maxChildNum` specifies the maximum number of children for each node.
```Python
tree = SegmentTree(
  [1, 2, 3, 4, 5],
  func=min, default=0, maxChildNum=3
)
```

Use `update()` to update the values, if necessary, by specifying a dictionary of key/value pairs. Currently, adding new keys is not supported yet. You need to use `update()` to initialize the values.
```Python
tree.update({1: 3, 4: 6})
```

Use `query()` to to find the best value of a range of keys. The range is denoted by a tuple `(a, b)`, presenting each key `x` such that `a <= x <= b`. The range here is closed on both sides, as we may deal with keys other than `int` type.
```Python
tree.query((1, 3))
```
