# -*- coding: utf-8 -*-
# Created by restran on 2018/6/21
from __future__ import unicode_literals, absolute_import

from collections import Counter

from mountains.utils import PrintCollector

"""
字符频率统计
"""


def decode(data, verbose=False):
    p = PrintCollector()
    r = Counter(data)
    length = len(data)
    for k, v in r.items():
        p.print('{}: {:.1f}%, {}'.format(k, v / length * 100, v))

    return p.smart_output(verbose=verbose)