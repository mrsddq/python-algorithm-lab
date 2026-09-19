def merge_sort(values):
    """Return a stable sorted copy; O(n log n) time and O(n) auxiliary space."""
    if len(values) <= 1:
        return list(values)

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    return _merge(left, right)


def _merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if not right[j] < left[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
