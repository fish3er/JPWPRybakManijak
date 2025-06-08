class PeekableIterator:
    def __init__(self, iterator):
        """
        Wraps around an iterator and allows peeking at the next value without consuming it.
        """
        # TODO: Store the iterator and prepare to buffer the next value
        pass

    def peek(self):
        """
        Returns the next value without consuming it.
        """
        # TODO: Return the next value without advancing the iterator
        pass

    def __iter__(self):
        # TODO: Return self as an iterator
        pass

    def __next__(self):
        """
        Returns the next value and advances the iterator.
        """
        # TODO: Return the buffered value if available; otherwise, pull from iterator
        pass
