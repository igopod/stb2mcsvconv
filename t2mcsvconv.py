import csv
import sys
import os

def make_output_file(input_file):
    tmp_file_name = os.path.splitext(os.path.basename(input_file))
    if (tmp_file_name[1]):
        output_file = '{0}.out{1}'.format(tmp_file_name[0], tmp_file_name[1])
        return output_file
    
    output_file = '{0}.out.csv'.format(tmp_file_name[0])
    return output_file

cmd_args = sys.argv

if len(cmd_args) <= 1:
    input_file = input("Введите путь к файлу для конвертации")
    output_file = make_output_file(input_file)
if len(cmd_args) == 2:
    input_file = cmd_args[1]
    output_file = make_output_file(input_file)
if len(cmd_args) == 3:
    input_file = cmd_args[1]
    output_file = cmd_args[2]
else:
    print('Синтаксис: "python t2mcsvconv.py [input_file.csv] [output_file.csv]"')

with open(output_file, 'w', newline='') as csv_output:
    fieldnames = ['Обращение',
        'Имя',
        'Отчество',
        'Фамилия',
        'Организация',
        'Улица (дом. адрес)',
        'Основной телефон',
        'Web-страница',
        'Адрес эл. почты',
        'Адрес 2 эл. почты',
        'Адрес 3 эл. почты',
        'День рождения',
        'Заметки']
    writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
    writer.writeheader()

    with open(input_file, 'r') as csv_input:
        reader = csv.DictReader(csv_input)
        for row in reader:
            writer.writerow({'Имя': row['Отображаемое имя'],
                'Адрес эл. почты': row['Адрес электронной почты']})
            print(row['Отображаемое имя'], row['Адрес электронной почты'])