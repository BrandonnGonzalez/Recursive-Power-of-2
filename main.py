def is_power_of_two(n):
  if n <= 0:
      return False
  if n == 1:
      return True
  if n % 2 != 0:
      return False
  return is_power_of_two(n // 2)
print(is_power_of_two(1))    # Output: True (2^0)
print(is_power_of_two(2))    # Output: True (2^1)
print(is_power_of_two(16))   # Output: True (2^4)
print(is_power_of_two(3))    # Output: False
print(is_power_of_two(0))    # Output: False
print(is_power_of_two(-16))  # Output: False

# Time Complexity: O(log n)
# The time complexity of this function is O(log n) because in each recursive call, the size of the problem (in this case, 𝑛
# is halved (or approximately halved in terms of bits shifted), leading to a logarithmic number of steps.

# Space Complexity: O(log n)
## The space complexity is also O(logn) due to the recursion stack. This is because the max depth of the recursion stack is logarithmic in relation to the input size n
