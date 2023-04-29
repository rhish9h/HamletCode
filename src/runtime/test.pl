:- include(evaluator).
:- include('../compiler/parse_tree').

test_case(1, [begin, var, x,;, var, y,;, var, z,;, z,:=,x,+,y, end, .], 2, 3, 5).

% Command to run the tests
% swipl -f .\test.pl -g run

run(Case) :-
    test_case(Case, Tokens, X, Y, Expected_Z),
    write('\nTest case '), write(Case), write(':\n\n'),
    (current_predicate(program/3), current_predicate(program_eval/4) ->
        findall((Z), (program(P, Tokens, []), program_eval(P, X, Y, Z)), Ans_Set), forall(member(Ans, Ans_Set), (write(Ans=Expected_Z),nl)) ;
        write('\n***** Missing either program/3 or program_eval/4 *****\n\n')).

run :- findall((Case), run(Case), _), halt.
