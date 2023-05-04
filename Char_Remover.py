import os

print("\n Getting Started: Welcome to the Character Remover! \n")

# Function to remove a specific character/number from file names
def remove_char_from_filename(dir_path, char, pos=None, direction=None):
    # List all files in the directory
    files = os.listdir(dir_path)

    # Loop through all files in the directory
    for filename in files:
        # Check if the file name contains the specified character/number
        if char in filename:
            # Remove the character/number from the file name
            new_filename = filename.replace(char, "")
            # If a character position is specified, remove characters based on the position
            if pos:
                pos = int(pos)
                if direction == "left":
                    new_filename = new_filename[pos:]
                elif direction == "right":
                    new_filename = new_filename[:-pos]
            # Rename the file with the new file name
            os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))

# Take input from the user for the directory path(s) and the character/number to remove
dir_paths = input("Enter the directory path(s) separated by commas: ").split(",")
char_to_remove = input("Enter the character/number to remove: ")
pos = input("Enter the character position to remove (optional): ")
direction = input("Enter the direction (left or right) to remove characters from the specified position (optional): ")

# Loop through all directory paths and remove the character/number from file names
for dir_path in dir_paths:
    remove_char_from_filename(dir_path.strip(), char_to_remove, pos, direction)

# Print a success message
print("Character/Number removed successfully from file names!")

input("\n Press Enter to Close The Program!! \n")