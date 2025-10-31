#!/usr/bin/env python3

# Read the file
with open('typescript-learning-path.md', 'r') as file:
    lines = file.readlines()

# Process the lines to remove empty code blocks
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    
    # Check if this line is a code block start
    if line.strip() == '```':
        # Count how many consecutive lines are just ```
        count = 0
        j = i
        while j < len(lines) and lines[j].strip() == '```':
            count += 1
            j += 1
        
        # If we have exactly 2 consecutive ``` lines, this is an empty code block
        if count == 2:
            # Skip these two lines
            i += 2
            # Also skip any trailing newlines that might be left
            while i < len(lines) and lines[i].strip() == '':
                i += 1
            continue
        # If we have more than 2 consecutive ``` lines, keep just one
        elif count > 2:
            new_lines.append('```\n')
            i += count
            # Also skip any trailing newlines that might be left
            while i < len(lines) and lines[i].strip() == '':
                i += 1
            continue
    
    # Add the line to our new content
    new_lines.append(line)
    i += 1

# Write the cleaned content back to the file
with open('typescript-learning-path.md', 'w') as file:
    file.writelines(new_lines)

print("Empty code blocks removed successfully!")