import re


def clean_file_for_digits(input_file,pattern, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    cleaned_lines = []
    for line in lines:
        # Find all matches of 1 to 3 digit numbers
        matches = re.findall(pattern, line)
        # Join matches into a cleaned line
        cleaned_line = ' '.join(matches)
        cleaned_lines.append(cleaned_line)
    
    return cleaned_lines


def multiply_and_add(input_lines,pattern):
    results = []
    for line in input_lines:
        # Find all matches of 1 to 3 digit numbers
        matches = re.findall(pattern, line)
        for match in matches:
            # Extract numbers as strings
            num1_str, num2_str = match.split(",")
            # Multiply the numbers
            result = int(num1_str) * int(num2_str)
            # Format the result as "mul(x,y) = result"
            results.append(result)
            #print(results)

    print(sum(results))
        

def main():
    """
    Main function to execute the program logic.
    """
    # Define the pattern for 1 to 3 digit numbers
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    pattern2= r'\d+,\d+'

    #file_path= "day3/day3_testfile.txt"
    file_path= "day3/day3.txt"
    # Usage
    cleaned_file = clean_file_for_digits(file_path,pattern, 'output.txt')  
    multiply_and_add(cleaned_file,pattern2) 


if __name__ == "__main__":
    main()
