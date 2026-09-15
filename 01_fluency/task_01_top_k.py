def top_k(items, k, key=None):
    if k <= 0:
        return []

    if key is None:
        key = lambda x: x

    heap = []

    def sift_up(i):
        while i > 0:
            parent = (i - 1) // 2

            if heap[parent][0] <= heap[i][0]:
                break

            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent

    def sift_down(i):
        n = len(heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and heap[left][0] < heap[smallest][0]:
                smallest = left

            if right < n and heap[right][0] < heap[smallest][0]:
                smallest = right

            if smallest == i:
                break

            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest

    for item in items:
        value = key(item)

        if len(heap) < k:
            heap.append((value, item))
            sift_up(len(heap) - 1)

        elif value > heap[0][0]:
            heap[0] = (value, item)
            sift_down(0)

    return [item for _, item in sorted(heap, reverse=True)]


if __name__ == "__main__":
    print(top_k([5, 1, 9, 3, 7], 3))

    people = [
        {"name": "Luca", "score": 81},
        {"name": "Anna", "score": 95},
        {"name": "Marco", "score": 87},
        {"name": "Giulia", "score": 91},
    ]

    print(top_k(people, 2, key=lambda x: x["score"]))

    print(top_k((x for x in range(100)), 5))