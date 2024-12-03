


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

def sort_list(list):
    # Convert all elements to integers
    int_list = [int(item) for item in list]
    
    # Now, sort the list
    int_list_sort = sorted(int_list)
 
    return int_list_sort

def compute_distance(list1, list2):
    distance_list = []
    for a, b in zip(list1,list2):
        if a > b:
            distance_list.append(a-b)
        else:
            distance_list.append(b-a)
    print(f"the full distance is: {sum(distance_list)}")

def main():
    """
    Main function to execute the program logic.
    """
    col1, col2 = load_data("day1.txt")

    sorted_list1 = sort_list(col1)
    sorted_list2= sort_list(col2)
    compute_distance(sorted_list1, sorted_list2)
    print("completed.")


if __name__ == "__main__":
    main()

