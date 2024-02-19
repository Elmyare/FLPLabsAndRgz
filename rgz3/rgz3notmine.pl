%Задание 3
:- dynamic(bag/2).

% просмотр содержимого базы данных
view_database :-
bag(Name, Weight),
write(Name), write(' - '), writeln(Weight),
fail.

% добавление записи
add_record :-
write('Введите имя пассажира: '), read(Name),
write('Введите вес багажа: '),
read(Weight),
assertz(bag(Name, Weight)),
writeln('Запись добавлена.').

% удаление записи
delete_record :-
write('Введите имя пассажира для удаления: '),
read(Name),
retract(bag(Name, _)),
writeln('Запись удалена.'),
fail.

% выполнение запроса к базе данных
query :-
findall(Weight, bag(_, Weight), List),
max_list(List, MaxWeight),
writeln('Багаж с максимальным весом:'),
bag(Name, MaxWeight), writeln(Name),
fail.

% главное меню программы
menu:-
repeat,
writeln('1. Просмотреть содержимое базы данных.'),
writeln('2. Добавить запись.'),
writeln('3. Удалить запись.'),
writeln('4. Выполнить запрос к базе данных.'), writeln('5. Выйти.'),
writeln('Выберите пункт меню: '), read(Choice),
(Choice = 1 -> view_database;
Choice = 2 -> add_record; Choice
= 3 -> delete_record; Choice = 4 -> query;
Choice = 5 -> halt;
write('Некорректный выбор. Попробуйте снова.'), nl), fail.
