# O(n) time; O(h) space
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binaryTreeDiameter(tree):
	return get_tree_info(tree).diameter

def get_tree_info(tree):
	if tree is None:
		return TreeInfo(0, 0)
	else:
		left_tree_info = get_tree_info(tree.left)
		right_tree_info = get_tree_info(tree.right)
		height = max(left_tree_info.height, right_tree_info.height) + 1
		root_longest_diameter = left_tree_info.height + right_tree_info.height
		diameter = max(left_tree_info.diameter, right_tree_info.diameter, root_longest_diameter)
		return TreeInfo(height, diameter)

class TreeInfo:
	def __init__(self, height, diameter):
		self.height = eight
		self.diameter = diameterh
