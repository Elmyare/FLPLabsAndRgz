delete(_, [], []).
delete(X, [X|T], Res) :-
    delete(X, T, Res).
delete(X, [H|T], [H|Res]) :-
    X \= H,
    delete(X, T, Res).
