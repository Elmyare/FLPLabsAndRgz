% ������ ����� �� ����� � �������� ���� ������������ �����
rgz2(InputFile, OutputFile) :-
    see(InputFile),              % ������� ���� ��� ������
    read_lines(Lines),           % ��������� ������ �� �����
    seeing(_),                   % ������, ��� �����
    seen,                        % ������� ���� ����� ������

    remove_max_length_words_from_list(Lines, FilteredLines),  % ������� ����� ������������ �����
    tell(OutputFile),            % ������� ���� ��� ������
    write_lines(FilteredLines),  % �������� ��������������� ������ � ����
    told.                        % ������� ���� ����� ������

% ��������� ������ �� ������ �����
read_lines([]) :- at_end_of_stream, !.
read_lines([Line|Lines]) :-
    read_line_to_codes(current_input, Line),
    read_lines(Lines).

% �������� ���� ���� ������������ ����� �� ������ �����
remove_max_length_words_from_list([], []).
remove_max_length_words_from_list([Line|Lines], [FilteredLine|FilteredLines]) :-
    split_string(Line, " ", "", Words),  % ��������� ������ �� �����
    max_word_length(Words, MaxLength),   % ����� ������������ ����� �����
    remove_max_length_words_from_line(Words, MaxLength, FilteredWords),  % ������� ����� ������������ �����
    atomic_list_concat(FilteredWords, " ", FilteredLine),  % ���������� ����� ������� � ������
    remove_max_length_words_from_list(Lines, FilteredLines).

% ����� ������������ ����� ����� � ������
max_word_length(Words, MaxLength) :-
    maplist(atom_length, Words, Lengths),
    max_list(Lengths, MaxLength).

% ������� ����� ������������ ����� �� ������ ����
remove_max_length_words_from_line([], _, []).
remove_max_length_words_from_line([Word|Words], MaxLength, Filtered) :-
    atom_length(Word, Length),
    (   Length < MaxLength
    ->  Filtered = [Word|Rest],
        remove_max_length_words_from_line(Words, MaxLength, Rest)
    ;   remove_max_length_words_from_line(Words, MaxLength, Filtered)
    ).

% �������� ������ ����� � ����� ������
write_lines([]).
write_lines([Line|Lines]) :-
    write(Line), nl,
    write_lines(Lines).
