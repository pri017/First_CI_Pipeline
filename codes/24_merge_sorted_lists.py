"""Program 24: merge sorted lists."""

def merge_sorted_lists(list1, list2):
    """Merge two sorted lists with two indices, preserving duplicates."""
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result


if __name__ == "__main__":
    print(merge_sorted_lists([int(x) for x in input("First sorted list: ").split()], [int(x) for x in input("Second sorted list: ").split()]))
