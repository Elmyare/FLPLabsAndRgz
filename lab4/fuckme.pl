% Чтение строк из файла и удаление слов максимальной длины
rgz2(InputFile, OutputFile) :-
    see(InputFile),              % Открыть файл для чтения
    read_lines(Lines),           % Прочитать строки из файла
    seeing(_),                   % Узнать, что видим
    seen,                        % Закрыть файл после чтения

    remove_max_length_words_from_list(Lines, FilteredLines),  % Удалить слова максимальной длины
    tell(OutputFile),            % Указать файл для записи
    write_lines(FilteredLines),  % Записать отфильтрованные строки в файл
    told.                        % Закрыть файл после записи

% Прочитать строки из потока ввода
read_lines([]) :- at_end_of_stream, !.
read_lines([Line|Lines]) :-
    read_line_to_codes(current_input, Line),
    read_lines(Lines).

% Удаление всех слов максимальной длины из списка строк
remove_max_length_words_from_list([], []).
remove_max_length_words_from_list([Line|Lines], [FilteredLine|FilteredLines]) :-
    split_string(Line, " ", "", Words),  % Разделить строку на слова
    max_word_length(Words, MaxLength),   % Найти максимальную длину слова
    remove_max_length_words_from_line(Words, MaxLength, FilteredWords),  % Удалить слова максимальной длины
    atomic_list_concat(FilteredWords, " ", FilteredLine),  % Объединить слова обратно в строку
    remove_max_length_words_from_list(Lines, FilteredLines).

% Найти максимальную длину слова в списке
max_word_length(Words, MaxLength) :-
    maplist(atom_length, Words, Lengths),
    max_list(Lengths, MaxLength).

% Удалить слова максимальной длины из списка слов
remove_max_length_words_from_line([], _, []).
remove_max_length_words_from_line([Word|Words], MaxLength, Filtered) :-
    atom_length(Word, Length),
    (   Length < MaxLength
    ->  Filtered = [Word|Rest],
        remove_max_length_words_from_line(Words, MaxLength, Rest)
    ;   remove_max_length_words_from_line(Words, MaxLength, Filtered)
    ).

% Записать список строк в поток вывода
write_lines([]).
write_lines([Line|Lines]) :-
    write(Line), nl,
    write_lines(Lines).
