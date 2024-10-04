def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.readlines()
            if content:
                print("\nContents of the file:")
                for line in content:
                    print(line.strip())
            else:
                print("The file is empty.")
    except FileNotFoundError:
        print("The file does not exist.")

def main():
    filename = 'user_data.txt'

    while True:
        print("\nMenu:")
        print("1. Write to file")
        print("2. Read from file")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            user_input = input("Enter the data you want to save: ")
            write_to_file(filename, user_input)
            print("Data saved successfully!")
        elif choice == '2':
            read_from_file(filename)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
