with open('file1.py', 'r') as f1, open('file2.py', 'r') as f2, open('file3.py', 'r') as f3:
    # Read the contents of each file
    content1 = f1.read()
    content2 = f2.read()
    content3 = f3.read()

# Combine the contents into a single string
combined_content = content1 + '\n' + content2 + '\n' + content3

# Open a new file for writing
with open('combined.py', 'w') as combined_file:
    # Write the combined content to the new file
    combined_file.write(combined_content)


def rearrange_code(original_file, output_file):
    code_lines = []
    imported_modules = set()

    # Read the original file into code_lines
    with open(original_file, 'r') as file:
        code_lines = file.readlines()

    # Identify and remove duplicate import statements
    for line in code_lines[:]:
        if line.startswith('import') or line.startswith('from'):
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


# Rearrange the code and write it to a new file
rearrange_code('combined.py', 'rearranged_code.py')


