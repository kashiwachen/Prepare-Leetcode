def isValidSubsequence(array, sequence):
    pointer = 0
    for i in range(len(array)):
        if array[i] == sequence[pointer]:
            pointer += 1
        if pointer == len(sequence):
            break
    return pointer == len(sequence)


if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    res = isValidSubsequence(array, sequence)
