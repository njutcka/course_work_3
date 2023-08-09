from utils import load_operations, sort_operations_by_date, \
    filter_operations_by_status, format_operation_output

all_operations = load_operations('operations.json')

sorted_operations = sort_operations_by_date(all_operations)

n = input("Какое количество последних операций распечатать? ")
filtered_operations = filter_operations_by_status(sorted_operations, int(n))

for filtered_operation in filtered_operations:
    print(format_operation_output(filtered_operation))
