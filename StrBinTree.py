from Node import Node
from Direction import Direction


class StrBinTree:
    '''
    Класс бинарного дерева с функциями поиска и выдачи ближайших строк
    '''

    def __init__(self):
        self.root: Node = Node()

    def add(self, value: any):
        '''
        добавляет строку в дерево
        '''
        self.root.add(value)

    def __add__(self, item):
        '''
        операция "+" объединения для двух деревьев
        '''
        if isinstance(item, StrBinTree):
            res = StrBinTree()
            for x in self.to_list():
                res.add(x)
            for x in item.to_list():
                res.add(x)
            return res
        else:
            raise ValueError('item is not StrBinTree')

    def __contains__(self, value: any):
        '''
        возвращает True, если есть точно такая же строка, или False, если её нет
        '''
        self.root.contains(value)

    def remove(self, value):
        '''
        удаляет строку. Удаление производится только в случае точного совпадения
        строки с указанной. Возвращает 0, если удаление выполнено, и 1 в остальных случаях
        '''
        found_node, parent = StrBinTree.__search(self.root, None, value)

        if found_node is None:
            return 1

        if parent is None:
            self.root = StrBinTree.__merge_to_first(self.root.left, self.root.right)
            if self.root is None:
                self.root = Node()
        else:
            merged = StrBinTree.__merge_to_first(found_node.left, found_node.right)
            if parent.left == found_node:
                parent.left = merged
            else:
                parent.right = merged
        return 0

    @staticmethod
    def __search(node: Node, parent: Node or None, value) -> (Node or None, Node or None):
        if node.value is None:
            return None, parent
        if node.value == value:
            return node, parent
        if value < node.value:
            return StrBinTree.__search(node.left, node, value)
        return StrBinTree.__search(node.right, node, value)

    @staticmethod
    def __merge_to_first(first: Node or None, second: Node or None) -> Node or None:
        if first is None and second is None:
            return None
        if first is None:
            return second
        if second is None:
            return first

        for x in second:
            first.add(x)
        return first

    def get(self, value):
        '''
        Возвращает две ближайшие строки, между которыми находится value
        Возвращаемые значения:
            (None, None) - дерево пусто
            (a, None) - value > a, при этом a - наибольший элемент в дереве
            (None, b) - value < b, при этом b - наименьший элемент в дереве
            (a, b) - a < value < b
            (a, a) - a == value
        '''
        return StrBinTree.__approx_get(self.root, None, None, Direction.Left, value)

    @staticmethod
    def __approx_get(node: Node or None, parent: Node or None, other_bound: Node or None,
                     direction: Direction, value):
        if node is None or node.value is None:
            return StrBinTree.__make_approx_result(parent, other_bound, direction)

        if value == node.value:
            return value, value

        next_direction = Direction.Left if value < node.value else Direction.Right
        next_node = node.left if value < node.value else node.right

        if direction == next_direction:
            return StrBinTree.__approx_get(next_node, node, other_bound, direction, value)
        return StrBinTree.__approx_get(next_node, node, parent, next_direction, value)

    @staticmethod
    def __make_approx_result(parent: Node or None, other_bound: Node or None,
                             direction: Direction):
        bound_value = None if other_bound is None else other_bound.value
        parent_value = None if parent is None else parent.value
        if direction == Direction.Left:
            return bound_value, parent_value
        return parent_value, bound_value

    def __len__(self):
        '''
        возвращает количество строк в дереве
        '''
        return len(self.root)

    def to_list(self):
        '''
        возвращает все строки в виде упорядоченного списка
        '''
        return list(iter(self.root))

    def __iter__(self):
        return iter(self.root)

    def __str__(self):
        return str(self.root)

