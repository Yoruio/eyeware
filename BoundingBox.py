class BoundingBox:
    def __init__(self, rect, seen):
        self.rect = rect    # rect is an list
        self.seen = seen    # int -> 0: seen, 1: not seen far, 2: not seen close