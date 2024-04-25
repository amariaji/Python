# Define the file name
file_name = "my_file.txt"

try:
    # Step 1: Write initial content to the file
    with open(file_name, 'w') as file:
        file.write("Hello, this is line 1\n")
        file.write("12345\n")
        file.write("This is line 3 with some special characters: !@#$%^&*\n")

    print(f"File '{file_name}' has been created with initial content.")

    # Step 2: Read and display the initial contents of the file
    with open(file_name, 'r') as file:
        file_contents = file.read()

    print(f"Contents of '{file_name}':")
    print(file_contents)

    # Step 3: Append additional content to the file
    with open(file_name, 'a') as file:
        file.write("This is line 4 appended to the existing content\n")
        file.write("Appending numbers: 67890\n")
        file.write("Final line with some more special characters: <>?{}\n")

    print(f"Additional content has been appended to '{file_name}'.")

    # Step 4: Read and display the updated contents of the file
    with open(file_name, 'r') as file:
        updated_contents = file.read()

    print(f"Updated contents of '{file_name}':")
    print(updated_contents)

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")

except PermissionError:
    print(f"Error: Permission denied to access the file '{file_name}'.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Script execution complete.")

