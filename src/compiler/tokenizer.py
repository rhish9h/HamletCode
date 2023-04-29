from file_parser import File_parser
import re
import sys

class Tokenizer:
    tokens = []
    keywords = ["act", "scene", "end", "numeral", "verse", "bool", "sayeth", "if", "then", "for", "it",
                "otherwise", "forsooth", "doth", "whilst", "to", "by", "step", "size", "of", "let", "be"]
    operators = ["+", "-", "*", "/", "<", ">", "<=", ">=", "=="]
    delimiters = [",", ".", "(", ")", ":", "?"]
    program = ""

    def __init__(self, ip_program):
        self.program = ip_program

    def tokenize(self):
        # Split the input code by whitespace, new lines, digits, identifiers, strings, and new lines
        tokens = re.findall(r'~.*?~|\b(?:act|scene|end|numeral|verse|bool|sayeth|if|then|otherwise|forsooth|doth|whilst|to|by|step|size|of|let|aye|nay)\b|[-+*/<>=]+|\w+|[.,():?]|[\n\r]+', self.program)

        # Iterate through each word in the program
        for word in tokens:
            if word == '':
                continue
            # Check for keywords
            elif word in self.keywords:
                self.tokens.append(("KEYWORD", word))
            # Check for operators
            elif word in self.operators:
                self.tokens.append(("OPERATOR", word))
            # Check for delimiters
            elif word in self.delimiters:
                self.tokens.append(("DELIMITER", f"'{word}'"))
            # Check for bool literals
            elif word == "aye" or word == "nay":
                self.tokens.append(("BOOL_LITERAL", word))
            # Check for numbers
            elif re.match(r"^\d+$", word):
                for ch in word:
                    self.tokens.append(("NUMBER", ch))
            # Check for strings
            elif re.match(r'^\~[a-zA-Z0-9\s]+\~$', word):
                for ch in word:
                    self.tokens.append(("STRING", ch))
            # Check for identifiers
            elif re.match(r"^[a-zA-Z][a-zA-Z0-9]*$", word):
                for ch in word:
                    self.tokens.append(("IDENTIFIER", ch))
            # Check for new lines
            elif word == "\n":
                # self.tokens.append(("NEWLINE", word))
                pass
            # If none of the above, it's an invalid token
            else:
                raise ValueError(f"Invalid token: {word}")

        return self.tokens


# Example usage
program = ''''''
parser = File_parser (sys.argv[1])
# data/example.hamlet
tokenizer = Tokenizer(parser.parse())

tokens = tokenizer.tokenize()

# Print below for debugging
# [print ('(', type, token, ')') if (token != '') else print('', end='') for type, token in tokens]

token_out = []

for type, token in tokens:
    if token != '':
        token_out.append(token)

print(','.join(token_out))