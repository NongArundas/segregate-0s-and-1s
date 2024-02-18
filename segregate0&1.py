def segregate_zeros_and_ones(arr):
    # Add Validation
    for num in arr:
        if num != 0 and num != 1:
            print("You are stuck in the part!")
            return arr
    
    # Count the number of zeros
    count_zeros = arr.count(0)
    
    # Fill the array with zeros
    arr[:count_zeros] = [0] * count_zeros
    
    # Fill the remaining part of the array with ones
    arr[count_zeros:] = [1] * (len(arr) - count_zeros)

    return arr

# Insert the input any integer size and enter "ENTER" to stop the array
input_array = [int(item) for item in input("Please enter only 0s and 1s in your list: \n").split()]
output_array = segregate_zeros_and_ones(input_array)
print(output_array)
