#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division

class SegmentTreeNode(object):
    def __init__(self, nodeRange, default=None):
        self.nodeRange = nodeRange
        self.value = default
        self.children = []
        self.parent = None

class SegmentTree(object):
    def __init__(self, keys, func, default=None, maxChildNum=2):
        self.func = func

        l = [SegmentTreeNode((k, k)) for k in sorted(keys)]
        self.mapping = {n.nodeRange[0]: n for n in l}

        while len(l) > 1:
            nl = []

            for i in xrange(0, len(l), maxChildNum):
                c = l[i:i+maxChildNum]
                n = SegmentTreeNode((c[0].nodeRange[0], c[-1].nodeRange[1]), default)
                n.children = c
                for x in c:
                    x.parent = n

                nl.append(n)

            l = nl

        self.root = l[0]

    def __covers__(self, a, b):
        return a[0] <= b[0] and b[1] <= a[1]

    def __intersects__(self, a, b):
        return not (a[1] < b[0] or a[0] > b[1])

    def update(self, keyValueDict):
        ul = set()

        for (k, v) in keyValueDict.iteritems():
            node = self.mapping[k]

            if node.value != v:
                node.value = v
                if node.parent != None:
                    ul.add(node.parent)

        while len(ul) > 0:
            newUL = set()

            for node in ul:
                pv = self.func(x.value for x in node.children)
                if pv != node.value:
                    node.value = pv
                    if node.parent != None:
                        newUL.add(node.parent)

            ul = newUL

    def query(self, queryRange):
        def query_aux(node):
            if self.__covers__(queryRange, node.nodeRange):
                return node.value
            else:
                return self.func(
                    query_aux(cNode)
                    for cNode in node.children
                    if self.__intersects__(queryRange, cNode.nodeRange)
                )

        if queryRange[0] > queryRange[1]:
            raise

        if not self.__intersects__(queryRange, self.root.nodeRange):
            raise

        return query_aux(self.root)

