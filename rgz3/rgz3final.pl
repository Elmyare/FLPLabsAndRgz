:- dynamic toy/2. % Определяем динамический предикат для хранения игрушек в базе данных

% Предикат удаления непечатаемых символов из списка кодов символов
delete_nonprintable([], []).
delete_nonprintable([Code|Rest], CleanList) :-
    (   Code >= 32, Code =< 126
    ->  CleanList = [Code|CleanRest]
    ;   delete_nonprintable(Rest, CleanList)
    ).

% Предикат чтения строки с учетом удаления непечатаемых символов
read_clean_string(String) :-
    read_line_to_codes(user_input, InputCodes),
    delete_nonprintable(InputCodes, CleanInputCodes),
    atom_codes(String, CleanInputCodes).

% Меню программы
menu :-
    writeln('Меню:'),
    writeln('1. Просмотр содержимого базы данных'),
    writeln('2. Добавление записи'),
    writeln('3. Удаление записи'),
    writeln('4. Выполнение запроса'),
    writeln('5. Выход из программы'),
    write('Выберите действие: '),
    read_clean_string(Choice),
    process_choice(Choice).

% Обработка выбора пользователя
process_choice("1") :- view_database, menu.
process_choice("2") :- add_record, menu.
process_choice("3") :- delete_record, menu.
process_choice("4") :- query_database, menu.
process_choice("5") :- save_and_exit.
process_choice(_) :- writeln('Некорректный ввод. Попробуйте снова.'), menu.

% Просмотр содержимого базы данных
view_database :-
    findall(Toy, toy(Toy), Toys),
    writeln('Содержимое базы данных:'),
    print_toys(Toys).

% Добавление записи
add_record :-
    writeln('Введите название игрушки: '),
    read_clean_string(N),
    writeln('Введите стоимость игрушки: '),
    read(C),
    assertz(toy(N, C)),
    writeln('Запись добавлена успешно!').

% Удаление записи
delete_record :-
    writeln('Введите название игрушки для удаления: '),
    read_clean_string(N),
    retract(toy(N, _)),
    writeln('Запись удалена успешно!').

% Выполнение запроса
query_database :-
    findall(Price, toy(_, Price), Prices),
    min_list(Prices, MinPrice),
    findall(Name, (toy(Name, Price), Price =< MinPrice + 100), Toys),
    writeln('Наиболее дешевые игрушки:'),
    print_toys(Toys).

% Сохранение и выход из программы
save_and_exit :-
    tell(), % Открываем файл базы данных для записи
    listing(toy), % Записываем содержимое базы данных в файл
    told, % Закрываем файл базы данных
    writeln('Содержимое базы данных сохранено в файле database.txt'),
    halt. % Завершаем выполнение программы

% Печать списка игрушек
print_toys([]) :-
    writeln('').
print_toys([Toy|Toys]) :-
    writeln(Toy),
    print_toys(Toys).

% Главный предикат
mainp :-
    retractall(toy(_, _)), % Очищаем базу данных перед началом работы
    consult('C:/VUZ/FLP/rgz3/database.txt'), % Загружаем начальное состояние базы данных из файла
    menu.

:- mainp. % Запускаем программу
