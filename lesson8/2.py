from collections import Counter, deque


def huffman_tree(string):
    frequency = Counter(string)
    sorted_deque = deque(sorted(frequency.items(), key=lambda item: item[1]))

    if len(sorted_deque) != 1:
        while len(sorted_deque) > 1:
            accumulated_frequency = sorted_deque[0][1] + sorted_deque[1][1]
            combined_el = {0: sorted_deque.popleft()[0], 1: sorted_deque.popleft()[0]}
            for j, count in enumerate(sorted_deque):
                if accumulated_frequency > count[1]:
                    continue
                else:
                    sorted_deque.insert(j, (combined_el, accumulated_frequency))
                    break
            else:
                sorted_deque.append((combined_el, accumulated_frequency))
    else:
        accumulated_frequency = sorted_deque[0][1]
        combined_el = {0: sorted_deque.popleft()[0], 1: None}
        sorted_deque.append((combined_el, accumulated_frequency))
    return sorted_deque[0][0]


table = {}


def huffman_coding(huff_tree, path=''):
    if not isinstance(huff_tree, dict):
        table[huff_tree] = path
    else:
        huffman_coding(huff_tree[0], path=f"{path}0")
        huffman_coding(huff_tree[1], path=f"{path}1")


s = input("Введите строку: ")

huffman_coding(huffman_tree(s))

for i in s:
    print(table[i], end=" ")
print()
print(table)
