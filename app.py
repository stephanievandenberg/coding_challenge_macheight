
def find_pairs(input_array, target_sum):

    input_array.sort()
    index_min, index_max = 0, len(input_array)-1

    pairs = []
    while index_min < index_max:
        if input_array[index_min] + input_array[index_max] == target_sum:
            pairs.append((input_array[index_min], input_array[index_max]))
        
        if input_array[index_min] + input_array[index_max] < target_sum:
            index_min += 1
        else: 
            index_max -= 1
    return pairs


def validate_input(input_array):
    try:
        input_array = [int(i) for i in input_array]
        return input_array
    except ValueError: 
        print('The received input is not a list of integers, please try again.')
        return False

def validate_target_sum(target_sum):
    try:
        target_sum = int(target_sum_string)
        return target_sum
    except ValueError: 
        print('The received target sum is not an integer, please try again.')
        return False
    

if __name__ == '__main__':

    print('Please enter a comma separated list of integers and press enter: ')
    while True:
        input_string = input()
        input_array = input_string.split(",")
        validated_input = validate_input(input_array)
        if validated_input != False:
            break

    print('Please enter the target sum: ')
    while True:
        target_sum_string = input()
        validated_sum = validate_target_sum(target_sum_string)
        if validated_sum != False:
            break
        
    pairs = find_pairs(validated_input, validated_sum)

    if len(pairs) == 0:
        print('There are no pairs of numbers in the input that sum ', validated_sum)
    else:
        print('Pairs found that sum ' + str(validated_sum) + ': ' , pairs)

