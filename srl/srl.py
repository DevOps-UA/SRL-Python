# -*- coding: utf-8 -*-
"""
srl
~~~

This module implements Simple Regex Language object.

:copyright: (c) 2016 by Simple Regex Language.
:license: MIT, see LICENSE for more details.
"""

from .builder import Builder

class SRL(object):
    """The SRL object implements Simple Regex Language and acts as
    central object. It is passed the string represented for
    Simple Regex Language. Once it is created it will act almost
    exactly same behavior as `re.RegexObject`.

    Usually you create a :class:`SRL` instance like this::

        from srl import SRL
        srl = SRL('letter from a to f')

    :param srl: the string of Simple Regex Language
    """

    def __init__(self, srl=None):
        self.srl = srl
        self.compiled = Builder.parse(srl)

    def __str__(self):
        return self.compiled.pattern

    def __getattr__(self, method):
        return getattr(self.compiled, method)
