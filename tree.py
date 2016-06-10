# list of lists way
def binary_tree(r):
	return [r, [], []]

def insert_left(root, new_branch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [new_branch, t, []])
	else:
		root.insert(1, [new_branch, [], []])
	return root

def insert_right(root, new_branch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2, [new_branch, [], t])
	else:
		root.insert(2, [new_branch, [], []])

def get_root_val(root):
	return root[0]

def set_root_val(root, new_val):
	root[0] = new_val

def get_left_child(root):
	return root[1]

def get_right_child(root):
	return root[2]

# r = binary_tree(3)
# print(r)
# insert_left(r, 4)
# print(r)
# print get_left_child(r)
# insert_left(r, 8)
# print(r)
# insert_right(r, 5)
# print(r)
# l = get_left_child(r)
# print(l)

r = binary_tree('a')
insert_left(r, 'b')
insert_right(get_left_child(r), 'd')
insert_right(r, 'c')
insert_left(get_right_child(r), 'e')
insert_right(get_right_child(r), 'f')
print(r)


# set_root_val(l, 9)
# print(r)
# insert_left(l, 11)
# print(r)
# insert_left(l, 18)
# print(r)
# insert_right(l, 12)
# print(r)


# my_tree = ['a', 
# 				['b', 
# 					['d',[],[]],['e', [],[]]],
# 				['c',
# 					['f',[],[]],[]]]

# print my_tree
# print my_tree[0]
# print my_tree[1]
# print my_tree[2]
