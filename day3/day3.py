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
    # Write the cleaned lines to the output file
    #with open(output_file, 'w', encoding='utf-8') as outfile:
    #    outfile.writelines(cleaned_lines)





def main():
    """
    Main function to execute the program logic.
    """
    # Define the pattern for 1 to 3 digit numbers
    pattern = r'mul\(\d{1,3},\d{1,3}\)'

    #file_path= "day3/day3_testfile.txt"
    file_path= "day3/day3.txt"
    # Usage
    cleaned_file = clean_file_for_digits(file_path,pattern, 'output.txt')   


if __name__ == "__main__":
    main()
