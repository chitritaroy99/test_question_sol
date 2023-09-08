def mySqrt(x):
    if x == 0:
        return 0

    left, right = 1, x
    result = 0

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the midpoint
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
            result = mid  # Store the possible result
        else:
            right = mid - 1

    return result  # Return the result rounded down to the nearest integer

# Driver code to test the mySqrt function
x1 = 4
x2 = 8

result1 = mySqrt(x1)
result2 = mySqrt(x2)

print(f"Square root of {x1} is {result1}")  # Output: Square root of 4 is 2
print(f"Square root of {x2} is {result2}")  # Output: Square root of 8 is 2
