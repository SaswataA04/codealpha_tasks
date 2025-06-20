import re

input_file = 'input.txt'     # The file with raw text
output_file = 'emails.txt'   # File to save extracted emails

with open(input_file, 'r') as file:
    content = file.read()

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

with open(output_file, 'w') as out_file:
    for email in sorted(set(emails)):
        out_file.write(email + '\n')

print(f"{len(set(emails))} unique emails extracted and saved to '{output_file}'")
