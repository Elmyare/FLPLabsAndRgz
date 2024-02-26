read_file_lines(File, Lines) :-
    open(File, read, Stream),
    read_lines(Stream, Lines),
    close(Stream).

% Предикат для рекурсивного чтения
% строк из потока
read_lines(Stream, []) :-
    at_end_of_stream(Stream).

read_lines(Stream, [Line | Rest]) :-
    \+ at_end_of_stream(Stream),
    read_line_to_string(Stream, Line),
    read_lines(Stream, Rest).

% Предикат для записи строк в файл в обратном порядке
write_reverse_lines(File, Lines) :-
    reverse(Lines, ReversedLines),
    open(File, write, Stream),
    write_lines(Stream, ReversedLines),
    close(Stream).

% Предикат для рекурсивной записи строк в поток
write_lines(_, []).

write_lines(Stream, [Line | Rest]) :-
    write(Stream, Line), nl(Stream),
    write_lines(Stream, Rest).

% Предикат для перестановки строк в обратном порядке
reverse_file(InputFile, OutputFile) :-
    read_file_lines(InputFile, Lines),
    write_reverse_lines(OutputFile, Lines).

task2 :- writeln('Enter input file:'), read(A), writeln('Enter output file:'), read(B), reverse_file(A, B).
