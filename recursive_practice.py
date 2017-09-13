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

