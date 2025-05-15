# Function to count the number of words in a text file
def count_words_in_file(filename):
    try:
        # Open the file in read mode with UTF-8 encoding
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()          # Read the entire content of the file
            words = content.split()        # Split the content into words using whitespace
            word_count = len(words)        # Count the number of words
            print(f"✅ The file '{filename}' has {word_count} words.")
    except FileNotFoundError:
        # Handle case when the file doesn't exist
        print(f"❌ Error: The file '{filename}' was not found.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"⚠️ An unexpected error occurred: {e}")

# Main function to get the filename from the user
def main():
    filename = input("Enter the filename (with .txt extension): ")  # Ask the user for the filename
    count_words_in_file(filename)  # Call the function to count words

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
