def combine_files(input_files, output_file):
    # Read the contents of each file
    contents = []
    for filename in input_files:
        with open(filename, 'r') as file:
            contents.append(file.read())

    # Combine the contents into a single string
    combined_content = '\n'.join(contents)

    # Open a new file for writing
    with open(output_file, 'w') as combined_file:
        # Write the combined content to the new file
        combined_file.write(combined_content)


def rearrange_code(original_file, output_file):
    code_lines = []
    imported_modules = set()

    # Read the original file into code_lines
    with open(original_file, 'r') as file:
        code_lines = file.readlines()

    # Identify and remove duplicate import statements
    code_lines_copy = code_lines.copy()  # Avoid modifying the list while iterating
    for line in code_lines_copy:
        if line.startswith(('import', 'from')):
            imported_modules.add(line.strip())
            code_lines.remove(line)

    # Sort the imported modules in alphabetical order
    imported_modules = sorted(imported_modules)

    # Rearrange the code
    organized_code = []
    for line in code_lines:
        if line.startswith('def'):
            organized_code.append(line)
            indent = line.split(':')[0]
            for inner_line in code_lines[code_lines.index(line) + 1:]:
                if inner_line.strip().startswith(indent):
                    organized_code.append(inner_line)
                else:
                    break
        else:
            organized_code.append(line)

    # Generate the rearranged code
    rearranged_code = '\n'.join(imported_modules) + '\n\n' + ''.join(organized_code)

    # Write the rearranged code to the output file
    with open(output_file, 'w') as file:
        file.write(rearranged_code)


if __name__ == '__main__':
    input_files = ['file1.py', 'file2.py', 'file3.py']
    output_file = 'combined.py'

    # Combine the code from input_files and write it to 'combined.py'
    combine_files(input_files, output_file)

    # Rearrange the code from 'combined.py' and write it to 'rearranged_code.py'
    rearrange_code(output_file, 'rearranged_code.py')

