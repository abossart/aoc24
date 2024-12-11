import re



def clean_file_for_digits(lines,pattern):
        # Find all matches of 1 to 3 digit numbers in the entire string
    matches = re.findall(pattern, lines)
    print(matches)
    # Join matches into a single string with spaces
    cleaned_content = ' '.join(matches)
    return matches


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

def clean_dont(content, pattern):
    # Use re.sub to replace all matches of the pattern in the string
    cleaned_content = re.sub(pattern, "", content)
    return cleaned_content

        

def main():
    """
    Main function to execute the program logic.
    """
    # Define the pattern for 1 to 3 digit numbers
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    pattern2= r'\d+,\d+'
    pattern3 = r"don't\([^)]*\).*?do\([^)]*\)"

    #file_path= "day3/day3_step2_test.txt"
    file_path= "day3/day3.txt"

    with open(file_path, 'r', encoding='utf-8') as infile:
        lines = infile.read().replace("\n","")
    #print(all_lines)
   
    print(lines)

    #file_path= "day3/day3_testfile.txt"
    
    # Usage
    #cleaned_file = clean_file_for_digits(lines,pattern)  
    cleaned_file = clean_file_for_digits(lines,pattern)  
    
    multiply_and_add(cleaned_file,pattern2) 
    
    cleaned_file_step2_with_do = clean_dont(lines,pattern3)
    
    cleaned_file_step2 = clean_file_for_digits(cleaned_file_step2_with_do,pattern) 
    multiply_and_add(cleaned_file_step2,pattern2) 
    


if __name__ == "__main__":
    main()
