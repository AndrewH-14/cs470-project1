import sys
import csv
import random

def quickselect(arr, left, right, k_val, arr_len):
    if (k_val > 0 and k_val <= right - left + 1):
        part_pos = partition(arr, left, right)
        # print(f'part_pos = {part_pos}, arr = {arr}')
        if (part_pos - left == k_val - 1):
            return partition(arr, left, right)
        if (part_pos - left > k_val - 1):
            # print(f'partition positition was higher than the k_val - 1: {part_pos}')
            return quickselect(arr, left, part_pos - 1, k_val, arr_len)
        else:
            # print(f'partition positition was lower than the k_val - 1: {part_pos}')
            return quickselect(arr, part_pos + 1, right, k_val - part_pos + left - 1, arr_len)

def partition(arr, left, right):
    pivot_val = arr[right]
    i = left
    for j in range(left, right):
        if (arr[j] <= pivot_val):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
    temp = arr[i]
    arr[i] = arr[right]
    arr[right] = temp
    return i
    

def main():
    all_input_nums = list()
    file_name = input('Enter File Name:\n')
    file = open(f'{file_name}')
    csv_reader = csv.reader(file)
    data = list()
    for line in csv_reader:
        data = line
    for num in data:
        all_input_nums.append(int(num))
    k_val = int(input('Type the k_value\n'))
    list_len = len(all_input_nums)
    quickselect(all_input_nums, 0, list_len - 1, list_len - k_val - 1, list_len)
    if (k_val >= 1 and k_val <= list_len):
        print(f'The top {k_val} elements:')
        for i in range(list_len - k_val, list_len):
            print(all_input_nums[i], end=' ')

if __name__ == "__main__":
    main()