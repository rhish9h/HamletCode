# from file_parser import File_parser
import re

class Tokenizer:
    tokens = []
    keywords = ["act", "scene", "end", "numeral", "verse", "bool", "sayeth", "if", "then",
                "otherwise", "forsooth", "doth", "whilst", "to", "by", "step", "size", "of", "let"]
    operators = ["+", "-", "*", "/", "<", ">", "<=", ">=", "=="]
    delimiters = [",", ".", "(", ")", ":", "?"]
    program = ""

    def __init__(self, ip_program):
        # parser = File_parser(ip_program)
        # self.program = parser.parse()
        self.program = ip_program

    def tokenize(self):
        # Split the input code by whitespace, new lines, digits, identifiers, strings, and new lines
        tokens = re.findall(r'"[^"]*"|\b(?:act|scene|end|numeral|verse|bool|sayeth|if|then|otherwise|forsooth|doth|whilst|to|by|step|size|of|let|aye|nay)\b|[-+*/<>=]+|\w+|[.,():?]|[\n\r]+', self.program)

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
                self.tokens.append(("DELIMITER", word))
            # Check for bool literals
            elif word == "aye" or word == "nay":
                self.tokens.append(("BOOL_LITERAL", word))
            # Check for numbers
            elif re.match(r"^\d+$", word):
                self.tokens.append(("NUMBER", word))
            # Check for identifiers
            elif re.match(r"^[a-zA-Z][a-zA-Z0-9]*$", word):
                self.tokens.append(("IDENTIFIER", word))
            # Check for strings
            elif re.match(r'^\"[a-zA-Z0-9\s]+\"$', word):
                self.tokens.append(("STRING", word))
            # Check for new lines
            elif word == "\n":
                self.tokens.append(("NEWLINE", word))
            # If none of the above, it's an invalid token
            else:
                raise ValueError(f"Invalid token: {word}")

        return self.tokens


# Example usage
program = '''
act
  scene
    let numeral a be 10.
    let verse b be "Hello world".
    let bool c be a > 5.
    sayeth a.
    sayeth b.
    sayeth c.
    if it be c then thee shall
      sayeth "The condition is true".
    otherwise
      sayeth "The condition is false".
  end scene
  scene
    forsooth, let i be 1 to 5 by step size of 1. doth
      sayeth i.
  end scene
  scene
    whilst it be i <= 5 doth
      sayeth i.
      let i be i + 1.
  end scene
end act
'''

tokenizer = Tokenizer(program)
tokens = tokenizer.tokenize()


[print (f'({token[0]}, {token[1]})') for token in tokens]