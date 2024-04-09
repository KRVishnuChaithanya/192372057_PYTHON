def addBinary(a, b):
    result = ""
    carry = 0
    
    i = len(a) - 1
    j = len(b) - 1
    
    while i >= 0 or j >= 0:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        
        current_sum = digit_a + digit_b + carry
        
        result_digit = current_sum % 2
        
        carry = current_sum // 2
        
        result = str(result_digit) + result
        
        i -= 1
        j -= 1
    
    if carry:
        result = "1" + result
    
    return result

# Test cases
test_cases = [("11", "1"), ("1010", "1011"), ("1111", "1010"), ("101101", "1100"), ("15", "45")]
for a, b in test_cases:
    print("Input: a =", a, ", b =", b)
    print("Output:", addBinary(a, b))
    print()
