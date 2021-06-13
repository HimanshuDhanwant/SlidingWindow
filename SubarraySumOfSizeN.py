# Given an array, we need to find all subarray sum of given size n

arr = [1,2,3,4,5,6,7,8]
# arr = [1,2,3]
n = 3

def subArraySum():
    if n <= len(arr):
        sum = 0
        sum_list = []

        for j in range(n):
            sum += arr[j]
        sum_list.append(sum)

        for j in range(1, len(arr)-n+1):
            sum = sum - arr[j-1] + arr[j+2]
            sum_list.append(sum)

        return sum_list
    else:
        return "Invalid input given"

print(subArraySum())

    