


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


def compute_similarity(list1, list2):
    similarity_list =[]
    for a in list1:
        count = 0
        for b in list2:
            if a == b:
                count += 1
        similarity_list.append(a*count)
    print(similarity_list)
    print(f"the similarity score is: {sum(similarity_list)}")


def main():
    """
    Main function to execute the program logic.
    """
    col1, col2 = load_data("day1/day1.txt")

    sorted_list1 = sort_list(col1)
    sorted_list2= sort_list(col2)
    compute_distance(sorted_list1, sorted_list2)
    print("completed step 1")

    compute_similarity(sorted_list1, sorted_list2)


if __name__ == "__main__":
    main()

