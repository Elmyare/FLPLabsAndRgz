:- dynamic toy/2. % ���������� ������������ �������� ��� �������� ������� � ���� ������

% �������� �������� ������������ �������� �� ������ ����� ��������
delete_nonprintable([], []).
delete_nonprintable([Code|Rest], CleanList) :-
    (   Code >= 32, Code =< 126
    ->  CleanList = [Code|CleanRest]
    ;   delete_nonprintable(Rest, CleanList)
    ).

% �������� ������ ������ � ������ �������� ������������ ��������
read_clean_string(String) :-
    read_line_to_codes(user_input, InputCodes),
    delete_nonprintable(InputCodes, CleanInputCodes),
    atom_codes(String, CleanInputCodes).

% ���� ���������
menu :-
    writeln('����:'),
    writeln('1. �������� ����������� ���� ������'),
    writeln('2. ���������� ������'),
    writeln('3. �������� ������'),
    writeln('4. ���������� �������'),
    writeln('5. ����� �� ���������'),
    write('�������� ��������: '),
    read_clean_string(Choice),
    process_choice(Choice).

% ��������� ������ ������������
process_choice("1") :- view_database, menu.
process_choice("2") :- add_record, menu.
process_choice("3") :- delete_record, menu.
process_choice("4") :- query_database, menu.
process_choice("5") :- save_and_exit.
process_choice(_) :- writeln('������������ ����. ���������� �����.'), menu.

% �������� ����������� ���� ������
view_database :-
    findall(Toy, toy(Toy), Toys),
    writeln('���������� ���� ������:'),
    print_toys(Toys).

% ���������� ������
add_record :-
    writeln('������� �������� �������: '),
    read_clean_string(N),
    writeln('������� ��������� �������: '),
    read(C),
    assertz(toy(N, C)),
    writeln('������ ��������� �������!').

% �������� ������
delete_record :-
    writeln('������� �������� ������� ��� ��������: '),
    read_clean_string(N),
    retract(toy(N, _)),
    writeln('������ ������� �������!').

% ���������� �������
query_database :-
    findall(Price, toy(_, Price), Prices),
    min_list(Prices, MinPrice),
    findall(Name, (toy(Name, Price), Price =< MinPrice + 100), Toys),
    writeln('�������� ������� �������:'),
    print_toys(Toys).

% ���������� � ����� �� ���������
save_and_exit :-
    tell(), % ��������� ���� ���� ������ ��� ������
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

% ������� ��������
mainp :-
    retractall(toy(_, _)), % ������� ���� ������ ����� ������� ������
    consult('C:/VUZ/FLP/rgz3/database.txt'), % ��������� ��������� ��������� ���� ������ �� �����
    menu.

:- mainp. % ��������� ���������
