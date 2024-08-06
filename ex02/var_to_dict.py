#!/usr/bin/python3

def convert_and_display_musicians(musicians_list):
    # Convert list to dictionary with year as key and musician name as value
    musicians_dict = {name: year for name, year in musicians_list}

    # Display dictionary in the specified format
    for name, year in musicians_list:
        print(f"{year} : {name}")

def main():
    # Example list of musicians with name and birth year
    musicians_list = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939'),
    ]

    # Call the function to convert and display musicians
    convert_and_display_musicians(musicians_list)

if __name__ == "__main__":
    main()
