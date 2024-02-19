:- dynamic toy/2. % ���������� ������������ �������� ��� �������� ������� � ���� ������

% ���� ���������
menu :-
    writeln('����:'),
    writeln('1. �������� ����������� ���� ������'),
    writeln('2. ���������� ������'),
    writeln('3. �������� ������'),
    writeln('4. ���������� �������'),
    writeln('5. ����� �� ���������'),
    flush_output,
    write('�������� ��������: '),
    flush_output,
    read(Choice),
    choice(Choice).

% ��������� ������ ������������
choice(1) :- view_database, menu.
choice(2) :- add_record, menu.
choice(3) :- delete_record, menu.
choice(4) :- query_database, menu.
choice(5) :- save_and_exit.

% �������� ����������� ���� ������
view_database :-
    findall(Toy, toy(Toy), Toys),
    writeln('���������� ���� ������:'),
    print_toys(Toys).

% ���������� ������
add_record :-
    writeln('������� �������� �������: '),
    flush_output,
    read_string(N),
    writeln('������� ��������� �������: '),
    flush_output,
    read(C),
    assertz(toy(N, C)),
    writeln('������ ��������� �������!'),
    flush_output.

% �������� ������
delete_record :-
    writeln('������� �������� ������� ��� ��������: '),
    flush_output,
    read_string(N),
    retract(toy(N, _)),
    writeln('������ ������� �������!'),
    flush_output.

% ���������� �������
query_database :-
    findall(Price, toy(_, Price), Prices),
    min_list(Prices, MinPrice),
    findall(Name, (toy(Name, Price), Price =< MinPrice + 100), Toys),
    writeln('�������� ������� �������:'),
    flush_output,
    print_toys(Toys).

% ���������� � ����� �� ���������
save_and_exit :-
    tell('C:/VUZ/FLP/rgz3/database.txt'), % ��������� ���� ���� ������ ��� ������
    listing(toy), % ���������� ���������� ���� ������ � ����
    told, % ��������� ���� ���� ������
    writeln('���������� ���� ������ ��������� � ����� database.txt'),
    halt. % ��������� ���������� ���������

% ������ ������ �������
print_toys([]) :-
    writeln('').
print_toys([Toy|Toys]) :-
    writeln(Toy),
    print_toys(Toys).

% ��������������� �������� ��� ������ ����� � ���������
read_string(String) :-
    read_line_to_string(user_input, String).

% ������� ��������
mainp :-
    retractall(toy(_, _)), % ������� ���� ������ ����� ������� ������
    consult('C:/VUZ/FLP/rgz3/database.txt'), % ��������� ��������� ��������� ���� ������ �� �����
    menu.
