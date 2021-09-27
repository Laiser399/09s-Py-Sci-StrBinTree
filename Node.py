class Node:
    def __init__(self, value: any or None = None):
        self.value: any or None = value
        self.left: Node or None = None
        self.right: Node or None = None

    def __iter__(self):
        if self.left is not None:
            for value in self.left:
                yield value
        if self.value is not None:
            yield self.value
        if self.right is not None:
            for value in self.right:
                yield value

    def __str__(self):
        if self.value is None:
            return ''

        if self.left is None and self.right is None:
            return self.value

        left_str = str(self.left) if self.left is not None else ''
        right_str = str(self.right) if self.right is not None else ''
        return f'{self.value}[{left_str},{right_str}]'

    def __len__(self):
        if self.value is None:
            return 0
        left_count = len(self.left) if self.left is not None else 0
        right_count = len(self.right) if self.right is not None else 0
        return 1 + left_count + right_count

    def add(self, value: any):
        if self.value == value:
            raise ValueError('Multi value')

        if self.value is None:
            self.value = value
        elif value < self.value:
            if self.left is None:
                self.left = Node()
            self.left.add(value)
        else:
            if self.right is None:
                self.right = Node()
            self.right.add(value)

    def __contains__(self, item):
        return self.contains(item)

    def contains(self, value: any):
        if self.value is None:
            return False
        if value == self.value:
            return True
        if value < self.value:
            if self.left is None:
                return False
            return self.left.contains(value)
        if self.right is None:
            return False
        return self.right.contains(value)
