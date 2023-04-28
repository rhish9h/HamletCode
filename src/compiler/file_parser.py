class File_parser:
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        try:
            with open(self.filename, 'r') as file:
                data = file.read()
                parsed_string = str(data)
            return parsed_string
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        except IOError:
            print(f"Error: Unable to read file '{self.filename}'.")