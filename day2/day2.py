


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



def main():
    """
    Main function to execute the program logic.
    """
    file_path= "day2/day2.txt"
    reports = load_reports(file_path)
    print(reports)
    safe_count = 0
    for r in range(len(reports)):
        is_valid_increase, is_valid_decrease = check_order_validity(reports[r])
        if is_valid_increase or is_valid_decrease:
            safe_count += 1
    print(safe_count)
    print("completed step 1")

 
    print("completed step 2")


if __name__ == "__main__":
    main()

