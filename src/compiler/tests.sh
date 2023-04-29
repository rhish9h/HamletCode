#!/bin/bash

cwd="$(dirname "$0")"

echo "Count char"
"${cwd}/hamlet" "${cwd}/../../data/count_char.hamlet"

echo $'\n'
echo "Example"
"${cwd}/hamlet" "${cwd}/../../data/example.hamlet"

echo $'\n'
echo "Factorial"
"${cwd}/hamlet" "${cwd}/../../data/factorial.hamlet"

echo $'\n'
echo "Fibonacci"
"${cwd}/hamlet" "${cwd}/../../data/fibonacci.hamlet"

echo $'\n'
echo "Hello world"
"${cwd}/hamlet" "${cwd}/../../data/hello_world.hamlet"

echo $'\n'
echo "Sum of squares"
"${cwd}/hamlet" "${cwd}/../../data/sum_of_squares.hamlet"