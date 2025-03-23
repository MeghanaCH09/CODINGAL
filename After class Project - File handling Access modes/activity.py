def write_file(filename, content):
    """Write content to a file (overwrites if exists)."""
    with open(filename, 'w') as file:  
        file.write(content)
    print(f"Data written to {filename}")

def append_file(filename, content):
    """Append content to an existing file."""
    with open(filename, 'a') as file: 
        file.write(content)
    print(f"Data appended to {filename}")

def read_file(filename):
    """Read and display the content of a file."""
    try:
        with open(filename, 'r') as file:  
            content = file.read()
            print(f"Contents of {filename}:\n{content}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

def read_write_file(filename, new_content):
    """Read existing data and then overwrite with new content."""
    try:
        with open(filename, 'r+') as file:  
            old_content = file.read()
            file.seek(0)
            file.write(new_content)
            file.truncate()  
        print(f"Updated {filename} from:\n{old_content}\nto:\n{new_content}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")


filename = "students.txt"
write_file(filename, "Alice - Favorite Subject: Math\nBob - Favorite Subject: Science\n")
append_file(filename, "Charlie - Favorite Subject: History\n")
read_file(filename)
read_write_file(filename, "Roy - Favorite Subject: Computer Science\nEmma - Favorite Subject: English\n")
read_file(filename)
