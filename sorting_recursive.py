#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n)
    TODO: Memory usage: O(n)"""
    new_list = []

    while len(items1) > 0 and len(items2) > 0:
        if items1[0] < items2[0]:
            new_list.append(items1[0])
            del items1[0]
        else:
            new_list.append(items2[0])
            del items2[0]

    if len(items1) > 0:
        new_list.extend(items1)

    if len(items2) > 0:
        new_list.extend(items2)

    return new_list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: O(n * m)
    TODO: Memory usage: O(n)"""
    middle = len(items) // 2

    left = items[:middle]
    left.sort()

    right = items[middle:]
    right.sort()

    return merge(left, right)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n * log (n))
    TODO: Memory usage: O(n)"""
    if len(items) in [0, 1]:
        return items

    middle = len(items) // 2
    return split_sort_merge(
        merge_sort(items[:middle]) + merge_sort(items[middle:])
    )


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (by selecting the end of the list) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: (N)
    TODO: Memory usage:  (Log^2N)"""
    i = low
    pivot = items[high]
  
    for j in range(low, high):
      if (items[j] <= pivot):
        items[i], items[j] = items[j], items[i]
        i += 1
      
    items[i], items[high] = items[i], items[i]
    return i


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: (N Log N)
    TODO: Worst case running time: (N^2) - when nearly sorted or sorted
    TODO: Memory usage: (Log^2N)"""
    if (low is None and high is None):
        low = 0
        high = len(items) - 1

    if low < high:
        partition_ind = partition(items, low, high)
        quick_sort(items, low, partition_ind - 1)
        quick_sort(items, partition_ind + 1, high)
