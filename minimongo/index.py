# -*- coding: utf-8 -*-


class Index(object):
    """A simple wrapper for arguments to
    :meth:`pymongo.collection.Collection.ensure_index`."""

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def __eq__(self, other):
        """Two indices are equal, when the have equal arguments.

        >>> Index(42, foo='bar') == Index(42, foo='bar')
        True
        >>> Index(foo='bar') == Index(42, foo='bar')
        False
        """
        return self.__dict__ == other.__dict__

    def ensure(self, collection):
        """Calls :meth:`pymongo.collection.Collection.create_index`
        on the given `collection` with the stored arguments.
        """
        return collection.create_index(*self._args, **self._kwargs)
