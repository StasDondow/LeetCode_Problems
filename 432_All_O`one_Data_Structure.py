# https://leetcode.com/problems/all-oone-data-structure

class ListNode:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = ListNode(float('-inf'))
        self.tail = ListNode(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_count = {}
        self.count_node = {}

    def _add_node_after(self, new_node, prev_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_node[node.count]

    def inc(self, key: str) -> None:
        if key in self.key_count:
            count = self.key_count[key]
            self.key_count[key] += 1
            node = self.count_node[count]
            next_node = node.next
            if next_node.count != count + 1:
                new_node = ListNode(count + 1)
                self._add_node_after(new_node, node)
                self.count_node[count + 1] = new_node
            next_node = node.next
            next_node.keys.add(key)
            node.keys.remove(key)
            if not node.keys:
                self._remove_node(node)
        else:
            self.key_count[key] = 1
            if self.head.next.count != 1:
                new_node = ListNode(1)
                self._add_node_after(new_node, self.head)
                self.count_node[1] = new_node
            self.head.next.keys.add(key)

    def dec(self, key: str) -> None:
        if key in self.key_count:
            count = self.key_count[key]
            node = self.count_node[count]
            if count == 1:
                del self.key_count[key]
            else:
                self.key_count[key] -= 1
                prev_node = node.prev
                if prev_node.count != count - 1:
                    new_node = ListNode(count - 1)
                    self._add_node_after(new_node, prev_node)
                    self.count_node[count - 1] = new_node
                prev_node = node.prev
                prev_node.keys.add(key)
            node.keys.remove(key)
            if not node.keys:
                self._remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
