file_names = ['first.py', 'second.py', 'third.py' , 'fourth.py', 'fifth.py']


output_file = 'merged_files.txt'

# Function to merge files
def merge_files(file_names, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in file_names:
            with open(file_name, 'r') as infile:
                content = infile.read()
                outfile.write(f'# Content of file: {file_name}\n\n')
                outfile.write(content)
                outfile.write('\n\n')


merge_files(file_names, output_file)

print(f'Merged files into {output_file}')