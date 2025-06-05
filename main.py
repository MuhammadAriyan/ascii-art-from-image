from ascii_magic import AsciiArt

def main():
    my_art = AsciiArt.from_image('image.jpg')
    my_art.to_terminal()
    prompt = input("Do you want to save the ASCII art to a file? (yes/no): ")
    if prompt.lower() == 'yes':
        while True:
            prompt = input("Enter the filename (with .txt extension): ")
            if prompt.endswith('.txt'):
                my_art.to_file(prompt)
                break
            else:
                print("Invalid filename. Please use a .txt extension.")
    # Add more functionality here as needed


if __name__ == "__main__":
    main()
