#!python

def is_sorted(items):
  """Return a boolean indicating whether given items are in sorted order.
  Running time: O(n)
  Memory usage: O(n)"""
  if len(items) in [0, 1]:
    return True
  
  for i in range(len(items) - 1):
    if items[i] > items[i + 1]:
      return False

  return True

def bubble_sort(items):
  """Sort given items by swapping adjacent items that are out of order, and
  repeating until all items are in sorted order.
  TODO: Running time: O(n ^ 2)
  TODO: Memory usage: O(1)"""
  for i in range(len(items) - 1):
    for j in range(0, len(items) - i - 1):
      if items[j] > items[j + 1]:
        items[j], items[j + 1] = items[j + 1], items[j]
      
def selection_sort(items):
  """Sort given items by finding minimum item, swapping it with first
  unsorted item, and repeating until all items are in sorted order.
  TODO: Running time: O(n ^ 2)
  TODO: Memory usage: O(1)"""
  for i in range(len(items)):
    min_ind = i
    for j in range(i + 1, len(items)):
      if items[min_ind] > items[j]:
        min_ind = j
    items[i], items[min_ind] = items[min_ind], items[i]
  
def insertion_sort(items):
  """Sort given items by taking first unsorted item, inserting it in sorted
  order in front of items, and repeating until all items are in order.
  TODO: Running time: O(n ^ 2)
  TODO: Memory usage: O(1)"""
  for i in range(len(items)):
    j = i - 1;
    while j >= 0 and items[i] < items[j]:
      items[j + 1] = items[j]
      j -= 1
    items[j + 1] = items[i]