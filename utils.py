import json

def load_operations(file):
    '''считывает json файл
    возвращает список словарей
    '''

    with open(file, 'r', encoding='utf-8') as f:
        operations = json.load(f)

    return operations

def sort_operations_by_date(operations):
    '''сортирует по дате, от более поздней к более ранней
    возвращает отсортированный список словарей
    '''
    valid_operations = []
    for operation in operations:
        if operation:
            valid_operations.append(operation)

    sorted_by_date = sorted(valid_operations, key=lambda k:'date', reverse=True)
    return sorted_by_date

def filter_operations_by_status(sorted_date, quantity):
    '''принимает список словарей и количество
    выбирает только выполнненные операции
    возвращает список из заданного количества словарей
    '''
    executed_operations = []
    for item in sorted_date:
        if item['state'] == "EXECUTED":
            executed_operations.append(item)
            if len(executed_operations) == quantity:
                break
    return executed_operations

def convert_date(date):
    '''преобразует формат даты до ДД.ММ.ГГГГ
    возвращает строку'''
    date1 = date[0:10]
    date1_lst = date1.split('-')
    convert_date = '.'.join(reversed(date1_lst))

    return convert_date

def mask_requisites(requisites):
    '''заменяет часть номера карты или счета *
    возвращает строку
    '''
    splited_req = requisites.split()
    number = splited_req[-1]
    if requisites.startswith("Счет"):
        hided_number = f"**{number[-4:]}"

    else:
        hided_number = f"{number[0:4]} {number[4:6]}** **** {number[-4:]}"

    splited_req[-1] = hided_number
    return ' '.join(splited_req)


def format_operation_output(executed_operation):
    '''подго авливает данные из словаря для печати
    возвращает f-строку'''
    str1 = f"{convert_date(executed_operation['date'])} {executed_operation['description']}"
    if executed_operation.get('from'):
        str2 = f"{mask_requisites(executed_operation['from'])} '->' {mask_requisites(executed_operation['to'])}"

    else:
        str2 = f"'->' {mask_requisites(executed_operation['to'])}"

    str3 = f"{executed_operation['operationAmount']['amount']} {executed_operation['operationAmount']['currency']['name']}"

    return f"{str1}\n{str2}\n{str3}\n"
