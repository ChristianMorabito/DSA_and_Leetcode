# Use a STACK data structure.
# Validate closed brackets with a dictionary
# Only opening brackets will be placed onto the STACK.

def valid_par(string):
	stack = []
	closed_check = {')': '(', '}': '{', ']': '['}
	for i in string:
		if i in closed_check:

			# STEP 2) Now stack won't be empty.

			if stack and closed_check[i] == stack[-1]:
				stack.pop()  # Pop (remove) last 'open bracket' from stack
			else:
				return False  # If closed bracket
		else:
			#  STEP 1) Because stack will initially be empty

			stack.append(i)  # Push (add) 'open bracket' onto the stack.
	return True if not stack else False  # Return False if there is a stray open bracket, as last item.


print(valid_par('({{}}([]))'))