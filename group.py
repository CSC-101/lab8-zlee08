def groups_of_3(arr: list[int]) -> list[list[int]]:
    result = []
    for i in range (0, len(arr), 3):
        result.append(arr[i:i+3])
    return result
