


def loaddata(file_path):
   
    with open(file_path, 'r') as file:
        # Initialize two empty lists for the columns
        col1, col2 = [], []
        for line in file:
            # Split each line into two parts
            num1, num2 = map(int, line.split())
            col1.append(num1)
            col2.append(num2)
    return col1, col2

def sortlist(list):
    # Convert all elements to integers
    int_list = [int(item) for item in list]
    print(int_list)
    
    # Now, sort the list
    int_list_sort = sorted(int_list)
    #print(type(int_list_sort[0]))
    #print()
    return int_list_sort

def main():
    """
    Main function to execute the program logic.
    """
    col1, col2 = loaddata("day1_short.txt")
    #print(col1)
    sorted_list1 = sortlist(col1)
    sorted_list2= sortlist(col2)
    print(sorted_list1)
    print(sorted_list2)
    print("completed.")


if __name__ == "__main__":
    main()

