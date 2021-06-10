"""
AlgoExpert/Permutations.py:4:23: W0621: Redefining name 'arr' from outer scope
(line 18) (redefined-outer-name)
AlgoExpert/Permutations.py:4:0: C0116: Missing function or method docstring
(missing-function-docstring)
AlgoExpert/Permutations.py:5:7: C1801: Do not use `len(SEQUENCE)` without
comparison to determine if a sequence is empty (len-as-condition)
AlgoExpert/Permutations.py:9:8: C0200: Consider using enumerate instead of
iterating with range and len (consider-using-enumerate)
"""
import pdb


def permutation_helper(arr, cur_permutation, permutations):
    """permutation_helper.

    Args:
        arr:
        cur_permutation:
        permutations:
    """
    if len(arr) == 0 and len(cur_permutation):
        pdb.set_trace()
        permutations.append(cur_permutation)
    else:
        for i, _ in enumerate(arr):
            new_permutation = cur_permutation + [arr[i]]
            new_arr = arr[:i] + arr[i+1:]
            permutations = permutation_helper(
                new_arr, new_permutation, permutations
            )
            pdb.set_trace()
    return permutations

array = permutation_helper([1,2,3], [], [])
print(array)
