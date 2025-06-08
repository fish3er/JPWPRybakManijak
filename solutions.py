def custom_range(start, end, step):
    """
    Generator that mimics the built-in range() function.
    Yields numbers from start to end with a given step.
    """
    current = start
    while (step > 0 and current < end) or (step < 0 and current > end):
        yield current
        current += step
def infinite_fibonacci():
    """
    Generator that yields Fibonacci numbers infinitely.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
def take_n(iterator, n):
    """
    Takes the first n items from an iterator and returns them as a list.
    """
    result = []
    try:
        for _ in range(n):
            result.append(next(iterator))
    except StopIteration:
        pass
    return result
def read_file_lines(filepath):
    """
    Generator that yields one line at a time from a file.
    """
    with open(filepath, 'r') as f:
        for line in f:
            yield line.rstrip('\n')

class PeekableIterator:
    def __init__(self, iterator):
        """
        Wraps around an iterator and allows peeking at the next value without consuming it.
        """
        self.iterator = iter(iterator)
        self._has_peeked = False
        self._peeked_value = None

    def peek(self):
        """
        Returns the next value without consuming it.
        """
        if not self._has_peeked:
            self._peeked_value = next(self.iterator)
            self._has_peeked = True
        return self._peeked_value

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next value and advances the iterator.
        """
        if self._has_peeked:
            self._has_peeked = False
            return self._peeked_value
        else:
            return next(self.iterator)
