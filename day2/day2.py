


def load_data(file_path):
   
    with open(file_path, 'r') as file:
        # Initialize two empty lists for the columns
        col1, col2 = [], []
        for line in file:
            # Split each line into two parts
            num1, num2 = map(int, line.split())
            col1.append(num1)
            col2.append(num2)
    return col1, col2

def load_reports(file_path):
    with open(file_path, 'r') as file:
    # Read lines and process each line into a list of integers
        data = [list(map(int, line.split())) for line in file]
    return data

def check_order_validity(list):
    
    is_valid_increase = False
    is_valid_decrease = False

    is_stricly_increasing = all(list[i] < list[i+1] for i in range(len(list) - 1))
    is_stricly_decreasing = all(list[i] > list[i+1] for i in range(len(list) - 1))

    if is_stricly_increasing:
        is_valid_increase = all(1 <= list[i+1] - list[i] <=3 for i in range(len(list) - 1))

    if is_stricly_decreasing:
        is_valid_decrease = all(1 <= list[i] - list[i+1] <=3 for i in range(len(list) - 1))


    return is_valid_increase, is_valid_decrease

def check_order_validity_with_fault_tolerance(list):
    
    fault_tolerance = 1
    valid_sequence  = 0
    index = 0

    while index <= len(list) - 1:
        if list[index] < list[index+1] and 1 <= abs(list[index] - list[index+1]) <=3:
            valid_sequence += 1
        if list[index] > list[index+1] and 1 <= abs(list[index] - list[index+1]) <=3:
            valid_sequence -= 1
        index += 1


    for i in range(len(list) - 1):
        if list[i] < list[i+1] and 1 <= abs(list[i] - list[i+1]) <=3:
            valid_sequence += 1
        if list[i] > list[i+1] and 1 <= abs(list[i] - list[i+1]) <=3:
            valid_sequence -= 1
    
    if abs(valid_sequence - fault_tolerance) <= len(list)-1:
        print(valid_sequence)
        return True
    else:
        print(valid_sequence)
        return False



def main():
    """
    Main function to execute the program logic.
    """
    file_path= "day2/day2_test.txt"
    reports = load_reports(file_path)
    #print(reports)
    safe_count = 0
    for r in range(len(reports)):
        is_valid_increase, is_valid_decrease = check_order_validity(reports[r])
        if is_valid_increase or is_valid_decrease:
            safe_count += 1
    print(safe_count)
    print("completed step 1")

    safe_count_with_tolerance = 0

    for r in range(len(reports)):
        is_valid_with_tolerance = check_order_validity_with_fault_tolerance(reports[r])
        if is_valid_with_tolerance:
            safe_count_with_tolerance += 1
    print(safe_count_with_tolerance)

    print("completed step 2")


if __name__ == "__main__":
    main()

