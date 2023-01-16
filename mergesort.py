import turtle

data_string = input()
data = data_string.split(',')
data = [int(x) for x in data]

def Merge(lower_idx, middle_idx, upper_idx):
    sorted_data     = []
    left_iter       = lower_idx
    right_iter      = middle_idx + 1

    # Compare elements from either side of the array and add the smaller one to the
    # sorted array
    while left_iter <= middle_idx and right_iter <= upper_idx:
        if data[left_iter] <= data[right_iter]:
            sorted_data.append(data[left_iter])
            left_iter += 1
        else:
            sorted_data.append(data[right_iter])
            right_iter += 1

    # Add any leftover values from the left side of the array to the sorted array
    while left_iter <= middle_idx:
        sorted_data.append(data[left_iter])
        left_iter += 1
    # Add any leftover values from the right side of the array to the sorted array
    while right_iter <= upper_idx:
        sorted_data.append(data[right_iter])
        right_iter += 1

    # Copy the sorted integers back into the data array
    for idx in range(len(sorted_data)):
        data[lower_idx + idx] = sorted_data[idx]

def MergeSort(lower_idx, upper_idx):
    if lower_idx >= upper_idx:
        return
    middle_idx = (lower_idx + upper_idx) // 2
    MergeSort(lower_idx, middle_idx)
    MergeSort(middle_idx + 1, upper_idx)
    Merge(lower_idx, middle_idx, upper_idx)

MergeSort(0, len(data) - 1)
print(data)