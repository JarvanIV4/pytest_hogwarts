table_comment = 'abc'
table_name = 'tr_teacher_training_and_further_education'
table_comment = ' ' if table_comment == '' else table_name
print(table_comment)

if len(table_name)>32:
    table_name = table_name.split('_')
    print(table_name)
    tabel_name_list = []
    for name in table_name:
        tabel_name_list.append(name[0])
    print(str(tabel_name_list))
    print('_'.join(tabel_name_list))