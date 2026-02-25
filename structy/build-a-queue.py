import unittest


class Node[T]:
    def __init__(self, val: T) -> None:
        self.val: T = val
        self.next: Node[T] | None = None


# space: O(n)
# where: n = number of nodes
class Queue[T]:
    def __init__(self) -> None:
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None
        self.size: int = 0

    # time:  O(1)
    # space: O(1)
    def enqueue(self, val: T) -> None:
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            assert self.tail  # For ty.
            self.tail.next = Node(val)
            self.tail = self.tail.next
        self.size += 1

    # time:  O(1)
    # space: O(1)
    def dequeue(self) -> T | None:
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return val


class TestSolution(unittest.TestCase):
    def values_of[T](self, head: Node[T] | None) -> list[T]:
        values: list[T] = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def test_00(self) -> None:
        queue: Queue[str] = Queue()
        queue.enqueue("a")
        self.assertEqual(queue.size, 1)
        self.assertEqual(queue.dequeue(), "a")
        queue.enqueue("b")
        queue.enqueue("c")
        self.assertEqual(queue.size, 2)
        self.assertEqual(queue.dequeue(), "b")
        self.assertEqual(queue.dequeue(), "c")
        self.assertEqual(queue.size, 0)

    def test_01(self) -> None:
        queue: Queue[str] = Queue()
        queue.enqueue("a")
        queue.enqueue("b")
        queue.enqueue("c")
        self.assertEqual(queue.dequeue(), "a")
        queue.enqueue("d")
        queue.enqueue("e")
        self.assertEqual(queue.size, 4)
        self.assertEqual(queue.dequeue(), "b")
        self.assertEqual(queue.dequeue(), "c")
        self.assertEqual(queue.dequeue(), "d")
        self.assertEqual(queue.dequeue(), "e")
        queue.enqueue("x")
        queue.enqueue("y")
        self.assertEqual(queue.size, 2)
        self.assertEqual(queue.dequeue(), "x")
        self.assertEqual(queue.dequeue(), "y")

    def test_02(self) -> None:
        queue: Queue[int] = Queue()
        for i in range(1, 150001):
            queue.enqueue(i)
        for _ in range(1, 150000):
            queue.dequeue()
        self.assertEqual(queue.size, 1)
        self.assertEqual(queue.dequeue(), 150000)


if __name__ == "__main__":
    unittest.main()
