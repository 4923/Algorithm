def solution(arr1, arr2):
    for row in range(len(arr1)):
        for col in range(len(arr1[row])):
            arr1[row][col] += arr2[row][col]
    return arr1