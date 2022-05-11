#!python


class BinaryMinHeap(object):
    """BinaryMinHeap: a partially ordered collection with efficient methods to
    insert new items in partial order and to access and remove its minimum item.
    Items are stored in a dynamic array that implicitly represents a complete
    binary tree with root node at index 0 and last leaf node at index n-1."""

    def __init__(self, items=None):
        """Initialize this heap and insert the given items, if any."""
        # Initialize an empty list to store the items
        self._items = []
        if items:
            for item in items:
                if type(item) is tuple and len(item) == 2:
                    self.insert(item)
                else:
                    self.insert((item, 0))

    def __repr__(self):
        """Return a string representation of this heap."""
        return 'BinaryMinHeap({})'.format(self._items)
    
    @property
    def items(self):
        item_values = []
        for item in self._items:
            item_values.append(item[0])
        return item_values
    
    @items.setter
    def items(self, items):
        item_tuples = []
        for item in items:
            if type(item) is tuple and len(item) == 2:
                item_tuples.append(item)
            else:
                item_tuples.append((item, 0))
        self._items = item_tuples

    def is_empty(self):
        """Return True if this heap is empty, or False otherwise."""
        return not bool(self.size())

    def size(self):
        """Return the number of items in this heap."""
        return len(self._items)

    def insert(self, item, priority = 0):
        """Insert the given item into this heap.
        TODO: Best case running time: O(1) under what conditions?
        TODO: Worst case running time: O(log n) under what conditions?"""
        # Insert the item at the end and bubble up to the root
        if type(item) is tuple and len(item) == 2:
            self._items.append(item)
        else:
            self._items.append((item, priority))

        if self.size() > 1:
            self._bubble_up(self._last_index())

    def get_min(self):
        """Return the minimum item at the root of this heap.
        Best and worst case running time: O(1) because min item is the root."""
        if self.size() == 0:
            raise ValueError('Heap is empty and has no minimum item')
        assert self.size() > 0
        return self._items[0][0]

    def delete_min(self):
        """Remove and return the minimum item at the root of this heap.
        TODO: Best case running time: O(1) under what conditions?
        TODO: Worst case running time: O(log n) under what conditions?"""
        if self.size() == 0:
            raise ValueError('Heap is empty and has no minimum item')
        elif self.size() == 1:
            # Remove and return the only item
            return self._items.pop()[0]
        assert self.size() > 1
        min_item = self._items[0]
        # Move the last item to the root and bubble down to the leaves
        last_item = self._items.pop()
        self._items[0] = last_item
        if self.size() > 1:
            self._bubble_down(0)
        return min_item[0]

    def replace_min(self, item, priority = 0):
        """Remove and return the minimum item at the root of this heap,
        and insert the given item into this heap.
        This method is more efficient than calling delete_min and then insert.
        TODO: Best case running time: O(1) under what conditions?
        TODO: Worst case running time: O(log n) under what conditions?"""
        if self.size() == 0:
            raise ValueError('Heap is empty and has no minimum item')
        assert self.size() > 0
        min_item = self._items[0]
        # Replace the root and bubble down to the leaves
        if type(item) is tuple and len(item) == 2:
            self._items[0] = item
        else:
            self._items[0] = (item, priority)

        if self.size() > 1:
            self._bubble_down(0)
        return min_item[0]

    def swap(self, index1, index2):
        """Swap the items at the given indices."""
        self._items[index1], self._items[index2] = self._items[index2], self._items[index1]
    
    def heapify(self, i, max):
        """Heapify the subtree with the given root index until the heap is
        valid."""
        index = None
        left_child = None
        right_child = None

        while i < max:
            index = i
            left_child_index = self._left_child_index(i)
            right_child_index = self._right_child_index(i)

            if left_child_index < max and self._items[left_child_index] < self._items[index]:
                index = left_child_index
            
            if right_child_index < max and self._items[right_child_index] < self._items[index]:
                index = right_child_index
            
            if index == i:
                return
            
            self.swap(i, index)
            i = index
    
    def build_min_heap(self):
        """Build a min heap."""
        i = floor(self.size() / 2 - 1)

        while i >= 0:
            self.heapify(i, self.size())
            i -= 1

    def _bubble_up(self, index):
        """Ensure the heap ordering property is true above the given index,
        swapping out of order items, or until the root node is reached.
        Best case running time: O(1) if parent item is smaller than this item.
        Worst case running time: O(log n) if items on path up to root node are
        out of order. Maximum path length in complete binary tree is log n."""
        if index == 0:
            return  # This index is the root node (does not have a parent)
        if not (0 <= index <= self._last_index()):
            raise IndexError('Invalid index: {}'.format(index))
        # Get the item's value
        item = self._items[index]
        # Get the parent's index and value
        parent_index = self._parent_index(index)
        parent_item = self._items[parent_index]
        
        if  parent_item[1] > item[1] or parent_item[0] > item[0]:
            # TODO: Swap this item with parent item if values are out of order
            self.swap(index, parent_index)
            # TODO: Recursively bubble up again if necessary
            self._bubble_up(parent_index)

    def _bubble_down(self, index):
        """Ensure the heap ordering property is true below the given index,
        swapping out of order items, or until a leaf node is reached.
        Best case running time: O(1) if item is smaller than both child items.
        Worst case running time: O(log n) if items on path down to a leaf are
        out of order. Maximum path length in complete binary tree is log n."""
        if not (0 <= index <= self._last_index()):
            raise IndexError('Invalid index: {}'.format(index))
        # Get the index of the item's left and right children
        left_index = self._left_child_index(index)
        right_index = self._right_child_index(index)
        if left_index > self._last_index():
            return  # This index is a leaf node (does not have any children)
        # Get the item's value
        item = self._items[index]

        # TODO: Determine which child item to compare this node's item to
        child_index = left_index
        if right_index <= self._last_index() and (self._items[right_index][1] < self._items[left_index][1] or self._items[right_index][0] < self._items[left_index][0]):
            child_index = right_index

        child_item = self._items[child_index]
        if child_item[1] < item[1] or child_item[0] < item[0]:
            # TODO: Swap this item with a child item if values are out of order
            self.swap(index, child_index)
            # TODO: Recursively bubble down again if necessary
            self._bubble_down(child_index)

    def _last_index(self):
        """Return the last valid index in the underlying array of items."""
        return len(self._items) - 1

    def _parent_index(self, index):
        """Return the parent index of the item at the given index."""
        if index <= 0:
            raise IndexError('Heap index {} has no parent index'.format(index))
        return (index - 1) >> 1  # Shift right to divide by 2

    def _left_child_index(self, index):
        """Return the left child index of the item at the given index."""
        return (index << 1) + 1  # Shift left to multiply by 2

    def _right_child_index(self, index):
        """Return the right child index of the item at the given index."""
        return (index << 1) + 2  # Shift left to multiply by 2


def test_binary_min_heap():
    # Create a binary min heap of 7 items
    items = [9, 25, 86, 3, 29, 5, 55]
    heap = BinaryMinHeap()
    print('heap: {}'.format(heap))

    print('\nInserting items:')
    for index, item in enumerate(items):
        heap.insert(item)
        print('insert({})'.format(item))
        print('heap: {}'.format(heap))
        print('size: {}'.format(heap.size()))
        heap_min = heap.get_min()
        real_min = min(items[: index + 1])
        correct = heap_min == real_min
        print('get_min: {}, correct: {}'.format(heap_min, correct))

    print('\nDeleting items:')
    for item in sorted(items):
        heap_min = heap.delete_min()
        print('delete_min: {}'.format(heap_min))
        print('heap: {}'.format(heap))
        print('size: {}'.format(heap.size()))


if __name__ == '__main__':
    test_binary_min_heap()