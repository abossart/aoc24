def split_digits(number):
    # Get the total number of digits
    num_digits = len(str(number))
    
    # Ensure the number has an even number of digits
    if num_digits % 2 != 0:
        raise ValueError("The number must have an even number of digits.")
    
    # Calculate the divisor to split the number into two halves
    divisor = 10 ** (num_digits // 2)
    
    # First half (integer division)
    first_half = number // divisor
    
    # Second half (modulo)
    second_half = number % divisor
    
    return first_half, second_half




def main():
    """
    Main function to execute the program logic.
    """
    print()
    list = [0, 4, 4979, 24, 4356119, 914, 85734, 698829]
    #list =[125,17]

    count = 0
    blink = 75
    
    while count < blink:
        index = 0
        while index <= len(list)-1:
            if list[index] == 0:
                list[index] = 1
                index += 1
            elif len(str(list[index])) % 2 == 0:
                first_half, second_half = split_digits(list[index])
                list.insert(index+1, second_half)
                list[index] = first_half
                index += 2
            else:
                list[index] = list[index]*2024
                index += 1
        count += 1
        list_size = len(list)
        print(f"blink count={count}, nb of stones = {list_size}")#  and list = {list} ")
        

    print("end")


if __name__ == "__main__":
    main()
