#!/bin/bash

cwd="$(dirname "$0")"

echo "Count char"
"${cwd}/hamlet" "${cwd}/../../data/count_char.hamlet"

# echo $'\n'
# echo "Example"
# ./hamlet ../../data/example.hamlet

# echo $'\n'
# echo "Factorial"
# ./hamlet ../../data/factorial.hamlet

# echo $'\n'
# echo "Fibonacci"
# ./hamlet ../../data/fibonacci.hamlet

# echo $'\n'
# echo "Hello world"
# ./hamlet ../../data/hello_world.hamlet

# echo $'\n'
# echo "Sum of squares"
# ./hamlet ../../data/sum_of_squares.hamlet