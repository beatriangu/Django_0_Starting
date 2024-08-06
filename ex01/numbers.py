def numbers():
    try:
        with open('numbers.txt', 'r') as file:
            content = file.read()
            numbers_list = content.split(',')
            for number in numbers_list:
                print(number)
    except FileNotFoundError:
        print("numbers.txt doesn't exist")

if __name__ == "__main__":
    numbers()
