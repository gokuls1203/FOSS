def maxArea(height):
    result = 0
    l, r = 0, len(height) - 1
    while l < r:
        area = (r - l) * min(height[l], height[r])
        result = max(result, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return result
x=int(input("Enter the number of heights You want to add in the list"))
for i in range of (x):
  h=int(input("Enter the Height"))
  height.append(h)
print(maxArea(height))