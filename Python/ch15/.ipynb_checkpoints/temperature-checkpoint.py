def above_freezing(celsius: float) -> bool:
    """Return True iff temperature celsius degrees is above freezing.
    >>> above_freezing(5.2)
    True
    >>> above_freezing(-2)
    False
    """
    return celsius > 0

def above_freezing_v2(celsius: float) -> bool:
    """Return True iff temperature celsius degrees is above freezing.
    >>> above_freezing_v2(5.2)
    True
    >>> above_freezing_v2(-2)
    False
    """
    return celsius >= 0
