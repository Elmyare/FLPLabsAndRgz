odd(X) :- X mod 2 =\= 0. % if x is odd
odd(X, Y) :- Y >= X, odd(Y), write(Y), write('  '), fail. % if still in loop and Y is odd
odd(X, Y) :- Y > X, Y1 is Y - 1, odd(X, Y1). % if Y > X, continue with (X, Y - 1)
odd(X, Y) :- Y == X. % if Y = X, end
print_odd() :-
    writeln('start:'), read(X),
    writeln('End:'), read(Y), nl, writeln('The result is:'), odd(X, Y).
num1() :- print_odd().

fibonacci(X, Y) :- X < 2, Y is 1, !. % if X < 2 (0 or 1), Y = 1
fibonacci(X, Y) :-
	X2 is X - 2,
	X1 is X - 1,
	fibonacci(X2, Y2), % (N-2)th number
	fibonacci(X1, Y1), % (N-1)th number
	Y is Y2 + Y1. % Nth Fibonacci number = (N-2)th + (N-1)th numbers
fibonacci() :-
	repeat, % cycle
        writeln('enter number'),
	writeln('-----------------'),
        read(X),
	% if x < 0 - fail, else - print Nth Fibonacci number and \n\n
	(X < 0, !; (fibonacci(X, RES), write('The result is: '), writeln(RES), nl, nl, fail)).
num2() :- fibonacci().

split(N1, N2, [H | T], [H | T1], L2, L3) :- % first - always
	H < min(N1, N2), !,                 % if head is less than min(N1,N2)
	split(N1, N2, T, T1, L2, L3).       % put it in L1 and continue recursively
split(N1, N2, [H | T], L1, [H | T2], L3) :- % second - if first failed
	H =< max(N1, N2), !,                % if head is less than max(N1,N2)
	split(N1, N2, T, L1, T2, L3).       % put it in L2 and continue recurs.
split(N1, N2, [H | T], L1, L2, [H | T3]) :- % third - if second failed
	split(N1, N2, T, L1, L2, T3).       % put in L3 and continue
split(_, _, [], [], [], []).
print_split() :-
	writeln('Enter list '), read(L),
	writeln('Enter first num: '), read(N1),
	writeln('Enter second num: '), read(N2),
	split(N1, N2, L, L1, L2, L3),
	writeln('The result is: '), writeln(L1), writeln(L2), writeln(L3).
num3 :- print_split().

% 4.
% L - input list, L_new / L_res - result list, Max - maximum occurencies of element in list, H - head, T - tail
most—ommon([], [], 0) :- !. % empty - finish
most—ommon([H | T], L_res, Max) :-
	delete(T, H, L_temp), % delete H from list
	length([H | T], LenL), % count list items with H
	length(L_temp, LenL_temp), % count list items without all Hs
	Max_temp is LenL - LenL_temp, % occurencies of element H - Max_temp to compare with other elements
	most—ommon(L_temp, L_new, Max_maybe), % recursive call of mostCommon()
	(Max_temp > Max_maybe -> % is previous Max (Max_temp) > Max_maybe from recursive call  ?
		(L_res = [H], Max is Max_temp); % true - Max is Max_temp
		(Max is Max_maybe, % false - Max is Max_maybe
		(Max_temp =:= Max_maybe -> % and is Max_temp = Max_maybe
			L_res = [H | L_new]; % true - L_res = H + L_new
			L_res = L_new)) % false - L_res = L_new
	).
most—ommon(L, L_new) :-	most—ommon(L, L_new, _). % if calling mostCommon/2, call mostCommon/3 (L, L_new, _)
print_most—ommon() :-
        writeln('Enter list: '), read(L),
	most—ommon(L, L_new),
	writeln('The result is: '), writeln(L_new).
num4 :- print_most—ommon().
