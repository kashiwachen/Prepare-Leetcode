def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    coins = [0 for _ in range(len(denoms))]
    denoms = sort_denoms(denoms)
    for idx in range(len(denoms)):
        coins[idx] = n // denoms[idx]
        rest  = n % denoms[idx]
        n = rest
    if rest != 0:
        return -1
    result = 0
    for num in coins:
        result += num
    return result

def sort_denoms(array):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(array)-1):
            if array[i] < array[i+1]:
                swap(i, i+1, array)
                is_sorted = False
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

minNumberOfCoinsForChange(9, [3, 5])
