def min_length_after_removals(s):
    stack = []
    
    for char in s:
        if stack and (stack[-1] + char in ["AB", "CD"]):
            stack.pop()
        else:
            stack.append(char)

    return len(stack)

s = "ABACDCDAB"
result = min_length_after_removals(s)
print(result)
