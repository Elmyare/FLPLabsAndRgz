:- dynamic(toy/2).

% Загрузка базы данных из файла
load_database(File) :-
    consult(File).

% Сохранение базы данных в файл
save_database(File) :-
    tell(File),
    listing(toy/2),
    told.

% просмотр содержимого базы данных
view_database :-
    toy(Name, Price),
    format('~w: ~w руб.~n', [Name, Price]),
    fail.
view_database.

% добавление записи
add_toy :-
    write('Введите название игрушки: '),
    read_line_to_string(user_input, Name),
    write('Введите стоимость игрушки: '),
    read_line_to_codes(user_input, PriceCodes),
    number_codes(Price, PriceCodes),
    assertz(toy(Name, Price)),
    writeln('Запись добавлена в базу данных.').

% удаление записи
delete_toy :-
    write('Введите название игрушки для удаления: '),
    read_line_to_string(user_input, Name),
    retract(toy(Name, _)),
    writeln('Запись удалена из базы данных.').

% выполнение запроса к базе данных
query :-
    findall(Price, toy(_, Price), Prices),
    min_list(Prices, MinPrice),
    MaxDiff is 100,
    findall(Name, (toy(Name, Price), Price =< MinPrice + MaxDiff), CheapestToys),
    write('Наиболее дешевые игрушки: '), nl,
    print_list(CheapestToys).

% главное меню программы
menu :-
    repeat,
    writeln('1. Просмотреть содержимое базы данных.'),
    writeln('2. Добавить запись.'),
    writeln('3. Удалить запись.'),
    writeln('4. Выполнить запрос к базе данных.'),
    writeln('5. Выйти.'),
    writeln('Выберите пункт меню: '),
    read_number(Choice),
    process_choice(Choice).

% чтение числа из входного потока
read_number(Number) :-
    read_line_to_codes(user_input, Codes),
    number_codes(Number, Codes).

% обработка выбора пользователя
process_choice(1) :- view_database, menu.
process_choice(2) :- add_toy, menu.
process_choice(3) :- delete_toy, menu.
process_choice(4) :- query, menu.
process_choice(5) :- writeln('Программа завершена.'), save_database('C:/VUZ/FLP/rgz3/toys_db.pl').
process_choice(_) :- writeln('Некорректный выбор. Попробуйте снова.'), menu.

% Печать списка
print_list([]).
print_list([X|Xs]) :-
    write(X), nl,
    print_list(Xs).


% Загрузка базы данных и запуск главного меню
mainp :-
    load_database('C:/VUZ/FLP/rgz3/toys_db.pl'),
    menu.

% Выполнить сохранение базы данных при завершении работы программы
:- at_halt(save_database('C:/VUZ/FLP/rgz3/toys_db.pl')).
