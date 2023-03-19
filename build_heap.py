def heapify(data, n, i, swaps):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and data[l] < data[smallest]:
        smallest = l

    if r < n and data[r] < data[smallest]:
        smallest = r

    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        swaps.append((i, smallest))
        heapify(data, n, smallest, swaps)

def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        heapify(data, n, i, swaps)
    return swaps

def main():
    ievades_veidas = input()

    if "I" in ievades_veidas:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))

    elif "F" in ievades_veidas:
        nosaukums = input()

        with open("test/" + nosaukums, 'r') as fails:
            n = int(fails.readline())
            data = list(map(int, fails.readline().split()))
            assert len(data) == n
            swaps = build_heap(data)
            print(len(swaps))

    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
