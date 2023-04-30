# HamletCode

## SER502-project-group-3
<br>

```
The grand design, forsooth, to marry the realms of yon computer programming and literature hath led to the birth of a wondrous programming tongue, HamletCode. 'Tis a valiant quest to entwine the boundless muse of language with the steadfast logic of the code, that programming might becometh more delightful and captivating to the masses. Perchance, 'tis to be employ'd for the study and instruction of programming tenets in a manner both intriguing and pleasurable.
```

## Design
<br>

```
Design Tools : DCG, Prolog, Python (for tokenization), bash/executable to run the program
Data Structures: List

Flow : 
Bash code that takes program file as cli argument (eg. hamlet program.hamlet)
Internally it will run the following programs

- Python code to read the program file and generate tokens
- Prolog code that takes these tokens to create parse tree
- Prolog code that takes the parse tree to evaluate the output

```

## Project Structure
<br>

```
├── data
│   ├── basic_addition.hamlet
│   ├── basic_arith_with_brackets.hamlet
│   ├── basic_assignment.hamlet
│   ├── basic_bool_var_expression.hamlet
│   ├── basic_bool_with_bracket.hamlet
│   ├── basic_comparison.hamlet
│   ├── basic_multiplication.hamlet
│   ├── basic_print.hamlet
│   ├── basic_scene_and_scene.hamlet
│   ├── basic_traditional_forloop_test.hamlet
│   ├── basic_variable_decl.hamlet
│   ├── basic_while_test.hamlet
│   ├── count_char.hamlet
│   ├── example.hamlet
│   ├── factorial.hamlet
│   ├── fibonacci.hamlet
│   ├── hello_world.hamlet
│   └── sum_of_squares.hamlet
├── doc
│   ├── Milestone 1.pdf
│   └── contribution.txt
└── src
    ├── compiler
    │   ├── __pycache__
    │   ├── dcg
    │   ├── file_parser.py
    │   ├── parse_tree
    │   ├── parser
    │   └── tokenizer.py
    └── runtime
        ├── evaluator
        ├── hamlet
        └── tests

```


- data -> directory for all example program files
- doc -> directory for all docs
- src -> directory for all source files
- compiler -> directory for all compilation related files
- runtime -> directory for all runtime related files
- dcg -> grammar
- file_parser.py -> to read the program file
- tokenizer.py -> read program file and generate tokens
- parse_tree -> to generate parse_tree from program tokens
- evaluator -> to evaluate the program from the parse_tree
- parser -> script to generate parse tree
- hamlet -> to run the parser then pass the parse tree to evaluator, main driver of the program evaluator
- tests -> tests for different program files

<br>

## Important commands to run programs
Note: It is recommended to use Git Bash for Windows
<br>

### Compile and run the hamlet program code
```
./src/runtime/hamlet <program_name>
```

eg.

```
./src/runtime/hamlet data/factorial.hamlet
```
<br>

### Compile program and create parse tree
```
./src/compiler/parser <program_name>
```

eg.

```
./src/compiler/parser data/factorial.hamlet
```
<br>

### Create tokens for the program
```
python src/compiler/tokenizer.py <program_name>
```

eg.

```
python src/compiler/tokenizer.py data/factorial.hamlet
```
<br>

### Run tests
```
./src/runtime/tests
```

<br>

> Note: The tokenizer is a python program. If your machine uses python3 to run python, please change parser as follows (After section):

Before
```
# Run tokenizer, get tokens
tokens=$(python ${cwd}/tokenizer.py $file_name)
```
After
```
# Run tokenizer, get tokens
tokens=$(python3 ${cwd}/tokenizer.py $file_name)
```