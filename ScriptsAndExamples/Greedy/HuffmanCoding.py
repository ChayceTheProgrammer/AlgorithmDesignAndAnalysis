"""
Huffman coding is a greedy algorithm used for lossless data compression.

The idea behind Huffman coding is to assign variable-length codes to input characters,
    where the lengths of the assigned codes are based on the frequencies of the corresponding characters.
The variable-length codes assigned to input characters are prefix codes,
    meaning that the code of any character is not the prefix of the code of any other character.

The Huffman coding algorithm works by building a binary tree,
    where the leaf nodes represent the input characters,
    and the weight of each leaf node is the frequency of the corresponding character.

The algorithm then assigns codes to the characters by traversing the binary tree
    from the root to the leaf nodes, assigning a 0 for left branches and a 1 for right branches.

Explanation:
The huffman_coding function takes the input text as a string and returns
    the Huffman codes for each character and the compressed text.

In the first step,
    the function counts the frequency of each character in the input text using the
    Counter class from the collections module.

In the second step, the function builds the Huffman tree by
    repeatedly taking the two nodes with the lowest frequencies,
    creating a new node with the combined frequency, and adding it back to the queue.
    The queue is sorted by frequency to ensure that the nodes
    with the lowest frequencies are processed first.

In the third step, the function assigns Huffman codes to each character by traversing
    the Huffman tree and assigning a 0 for left branches and a 1 for right branches.

In the fourth step,
    the function compresses the input text by replacing each character
    with its corresponding Huffman code.

The key points are:
Huffman coding is a greedy algorithm that assigns variable-length codes to input
    characters based on their frequencies.
The algorithm builds a binary tree where the
    leaf nodes represent the input characters,
    and the weight of each leaf node is the
    frequency of the corresponding character.
The Huffman codes are assigned by traversing the binary tree
    from the root to the leaf nodes, assigning a 0 for left branches and a 1 for right branches.
The compressed text is generated by replacing each character in the
    input text with its corresponding Huffman code.
"""
#implementationfrom collections import Counter, deque
from collections import Counter,deque

def huffman_coding(text):
    """
    Performs Huffman coding on the given text.

    Args:
        text (str): The input text to be compressed.

    Returns:
        dict: A dictionary mapping characters to their Huffman codes.
        str: The compressed text.
    """
    # Step 1: Count the frequency of each character in the text
    char_freq = Counter(text)

    # Step 2: Build the Huffman tree
    queue = deque(sorted([(freq, char) for char, freq in char_freq.items()], key=lambda x: x[0]))
    while len(queue) > 1:
        # Take the two nodes with the lowest frequencies
        freq1, char1 = queue.popleft()
        freq2, char2 = queue.popleft()

        # Create a new node with the combined frequency
        new_freq = freq1 + freq2
        queue.append((new_freq, (char1, char2)))

        # Sort the queue by frequency
        queue = deque(sorted(queue, key=lambda x: x[0]))

    # Step 3: Assign Huffman codes to each character
    huffman_codes = {}
    def traverse_tree(node, code=''):
        if isinstance(node, tuple):
            traverse_tree(node[0], code + '0')
            traverse_tree(node[1], code + '1')
        else:
            huffman_codes[node] = code
    traverse_tree(queue[0][1])

    # Step 4: Compress the text
    compressed_text = ''.join(huffman_codes[char] for char in text)

    return huffman_codes, compressed_text

if __name__ == "__main__":
    # Test the Huffman coding algorithm
    text = "Hello, World!"
    huffman_codes, compressed_text = huffman_coding(text)
    print("Original text:", text)
    print("Huffman codes:", huffman_codes)
    print("Compressed text:", compressed_text)