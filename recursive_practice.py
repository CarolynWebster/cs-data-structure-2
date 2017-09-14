# reverse a string recrusively
def recur_str(s):
    if len(s) > 1:
        return s[-1] + recur_str(s[:-1])
    else:
        return s


# given a list of numers and a max num - find missing num
# no using the set to list method

def find_missing_num(lst, max_val):
    #nums = set(lst)
    nums = set()
    for num in lst:
        nums.add(num)
    for i in range(1, max_val+1):
        if i not in nums:
            return i

def is_matched(expression):
    # get the expression length
    exp_len = len(expression)
    # make a dict of the bracket pairs
    punct = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    # make sure there are at least 2 characters
    if exp_len % 2 == 0:
        # make a 'stack' using a list
        bracket_stack = []
        
        # loop through the chars in the expression
        for i in range(exp_len):
            b = expression[i]
            # if it's an opening bracket - add to stack
            if b not in punct:
                bracket_stack.append(b)
            else:
                # if it's a closing bracket pop the last bracket off the stack
                if bracket_stack:
                    pair = bracket_stack.pop()
                    # check the punct dict to see if the matching bracket is popped
                    if b in punct:
                        if punct[b] != pair:
                            print "NO"
                            return False
                else:
                    print "NO"
                    return False
        # if there are no brackets remaining in the stack
        if not bracket_stack:
            print "YES"
            return True
        print "NO"
        return False
    # if we don't have at least 2 brackets or an odd number of brackets
    print "NO"
    return False
            
brack_txt = open("brackets.txt").readlines()
for line in brack_txt:
    # print line.strip()
    is_matched(line.strip()) 

# t = int(raw_input().strip())
# for a0 in xrange(t):
#     expression = raw_input().strip()
#     if is_matched(expression) == True:
#         print "YES"
#     else:
#         print "NO"