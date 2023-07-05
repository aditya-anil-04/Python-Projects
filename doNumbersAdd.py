def two_sum(nums, k):

  seen = set()
  for num in nums:
    if k - num in seen:
      return True
    seen.add(num)
  return False


if __name__ == "__main__":
  nums = [int(input("Enter first value of set: ")),
          int(input("Enter second value of set: ")),
          int(input("Enter third value of set: ")),
          int(input("Enter fourth value of set: "))]
  k = int(input("Enter sum value: "))
  print(two_sum(nums, k))