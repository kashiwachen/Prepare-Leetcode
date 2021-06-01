import pdb
def permutation_helper(arr, cur_permutation, permutations):
    if not len(arr) and len(cur_permutation):
        pdb.set_trace()
        permutations.append(cur_permutation)
    else:
        for i in range(len(arr)):
            new_permutation = cur_permutation + [arr[i]]
            new_arr = arr[:i] + arr[i+1:]
            permutations = permutation_helper(
                new_arr, new_permutation, permutations
            )
            pdb.set_trace()
    return permutations

arr = permutation_helper([1,2,3], [], [])
print(arr)
