from stackADT import Stack
from binaryTreeClass import Binary_tree
import operator

def build_parse_tree(parse_exp):
	p_list = parse_exp.split()
	p_stack = Stack()
	r = Binary_tree('')
	p_stack.push(r)
	current_tree = r

	for i in p_list:
		if i == '(':
			current_tree.insert_left('')
			p_stack.push(current_tree)
			current_tree = current_tree.get_left_child()
		elif i not in ['+','-','*','/',')']:
			current_tree.set_root_val(int(i))
			parent = p_stack.pop()
			current_tree = parent
		elif i in ['+','-','*','/']:
			current_tree.set_root_val(i)
			current_tree.insert_right('')
			p_stack.push(current_tree)
			current_tree = current_tree.get_right_child()
		elif i == ')':
			current_tree = p_stack.pop()
		else:
			raise ValueError
	return r


def evaluate(parse_tree):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
	
	left = parse_tree.get_left_child()
	right = parse_tree.get_right_child()

	if left and right:
		fn = opers[parse_tree.get_root_val()]
		return fn(evaluate(left), evaluate(right))
	else:
		return parse_tree.get_root_val()

# external method of preorder - better because we may want traversal and use it to do other things

def preorder(tree):
	if tree:
		print(tree.get_root_val())
		preorder(tree.get_left_child())
		preorder(tree.get_right_child())

# internal method of preorder

def preorder_internal(self):
	print(self.key)
	if self.left_child:
		self.left.preorder()
	else: 
		self.right_child:
		self.right.preorder()

def postorder(tree):
	if tree != None:
		postorder(tree.get_left_child())
		postorder(tree.get_right_child())
		print(tree.get_root_val())

def inorder(tree):
	if tree != None:
		inorder(tree.get_left_child())
		print(tree.get_root_val())
		inorder(tree.get_right_child())

def print_exp_inorder(tree):
	str_val = ""
	if tree:
		str_val = '(' + print_exp_inorder(tree.get_left_child())
		str_val = str_val + str(tree.get_root_val())
		str_val = str_val + print_exp_inorder(tree.get_right_child()) + ')'

	return str_val
	
def postorder_eval(tree):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

	res1 = None
	res2 = None

	if tree:
		res1 = postorder_eval(tree.get_left_child())
		res2 = postorder_eval(tree.get_right_child)
		if res1 and res2:
			return opers[tree.get_root_val()](res1, res2)
		else:
			return tree.get_root_val




pt = build_parse_tree("((3+5)*2")
pt.postorder()



