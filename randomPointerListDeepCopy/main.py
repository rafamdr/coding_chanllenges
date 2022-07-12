# Given a linked list, such that each node contains an additional random pointer which could point to any node in the
# list, or null, make a deep copy of the list and return the head node of the new copy.
# ----------------------------------------------------------------------------------------------------------------------


class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next: Node = None
        self.random: Node = None

    def skip(self, length: int):
        temp = self
        while temp.next and length > 0:
            temp = temp.next
            length -= 1
        return temp

    def __str__(self):
        result = ''
        temp = self
        while temp.next:
            random_value = temp.random.value if temp.random else ''
            result += '[v=%d, r=%s], ' % (temp.value, random_value)
            temp = temp.next
        return result

    def deep_copy(self):
        dict_nodes = {}
        new_start = Node(self.value)
        new_temp = new_start
        temp = self
        while temp.next:
            dict_nodes[temp] = new_temp
            temp = temp.next
            new_temp.next = Node(temp.value)
            new_temp = new_temp.next

        temp = self
        new_temp = new_start
        while temp.next:
            new_temp.random = dict_nodes.get(temp.random, None)
            temp = temp.next
            new_temp = new_temp.next

        return new_start
# ----------------------------------------------------------------------------------------------------------------------


max_items = 10
initial = 1
head = Node(initial)
temp = head

for i in range(initial + 1, max_items + 1):
    temp.next = Node(i)
    temp = temp.next


temp = head

temp.random = head.skip(2)
temp = temp.next
temp = temp.next

temp.random = head.skip(4)
temp = temp.next
temp = temp.next

temp.random = head.skip(6)
temp = temp.next
temp = temp.next

temp.random = head.skip(8)
temp = temp.next
temp = temp.next

result = head.deep_copy()

print(head)
print(result)
# ----------------------------------------------------------------------------------------------------------------------
