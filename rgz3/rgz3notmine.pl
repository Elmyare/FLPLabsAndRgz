%������� 3
:- dynamic(bag/2).

% �������� ����������� ���� ������
view_database :-
bag(Name, Weight),
write(Name), write(' - '), writeln(Weight),
fail.

% ���������� ������
add_record :-
write('������� ��� ���������: '), read(Name),
write('������� ��� ������: '),
read(Weight),
assertz(bag(Name, Weight)),
writeln('������ ���������.').

% �������� ������
delete_record :-
write('������� ��� ��������� ��� ��������: '),
read(Name),
retract(bag(Name, _)),
writeln('������ �������.'),
fail.

% ���������� ������� � ���� ������
query :-
findall(Weight, bag(_, Weight), List),
max_list(List, MaxWeight),
writeln('����� � ������������ �����:'),
bag(Name, MaxWeight), writeln(Name),
fail.

% ������� ���� ���������
menu:-
repeat,
writeln('1. ����������� ���������� ���� ������.'),
writeln('2. �������� ������.'),
writeln('3. ������� ������.'),
writeln('4. ��������� ������ � ���� ������.'), writeln('5. �����.'),
writeln('�������� ����� ����: '), read(Choice),
(Choice = 1 -> view_database;
Choice = 2 -> add_record; Choice
= 3 -> delete_record; Choice = 4 -> query;
Choice = 5 -> halt;
write('������������ �����. ���������� �����.'), nl), fail.
