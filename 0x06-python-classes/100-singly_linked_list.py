#!/usr/bin/python3
""" includes a class Node that defines a node of a singly linked list """


class Node:
    """ class Node with atributes data, next_node """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                value > current.next_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

        def __str__(self):
            result = ""
            current = self.head
            while (current is not None):
                result += str(current.data) + "\n"
                current = current.next_node
            return (result.rstrip())
