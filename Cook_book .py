from collections import Counter
file = open("recipes.txt")
onlist = file.read().split("\n")
some_list3 = []

for line in onlist:
    some_list2 = []
    if line != '':
        some_list2.append(line)
    some_list3.append(some_list2)

some_list4 = []
some_list5 = []
for line in some_list3:
    if line:
        some_list4 = some_list4 + line
    else:
        some_list5.append(some_list4)
        some_list4 = []


Cook_dict = {}
Key_list = []

for element in some_list5:
    if element[0]:
        key = element[0]
        Key_list.append(key)
        number = int(element[1])
        lis = []
        for i in range(2, number+2, 1):
            lis.append(element[i])
        Cook_dict[key] = Cook_dict.get(key, []) + [lis]

request_list = list()
request_list2 = list()
request_list3 = list()

for element in Cook_dict.values():
    for el in element:
        for e in el:
            request_list = e.split("|")
            request_list2.append(request_list)
        request_list3.append(request_list2)
        request_list = []
        request_list2 = []

someone_list = list()
sl = list()
for element in request_list3:
    for el in element:
        half_dict = {}
        half_dict['ingredient_name'] = el[0]
        half_dict['quantity'] = el[1]
        half_dict['measure'] = el[2]
        sl.append(half_dict)
    someone_list.append(sl)
    sl = []

finally_Dict = {}

for k,v in zip(Key_list, someone_list):
        finally_Dict[k] = v

# Конечный словарь __________________________________________________________________________
print(finally_Dict)

#----------------------------------------------------------------------------------------------------------
def get_shop_list_by_dishes(dishes, person_count):
    dishes = ['Омлет','Запеченный картофель']
    person = 2
    second_dict = {}
    dish_name = []
    dish_ingr = []
    dish_ingr2 = []
    for i in dishes:
        for j,k in finally_Dict.items():
            if i == j:
                print("----------------------------------------")
                for ingr in k:
                    dish_name.append(ingr["ingredient_name"])
    for i in dishes:
        for j,k in finally_Dict.items():
            if i == j:
                for ingr in k:
                    dish_ingr.append(ingr['measure'])
                    dish_ingr.append(int(ingr['quantity']) * person)




    function_dict = {}
    list_for_dish = []
    list_for_dish2 = []
    i = 1
    j = 0
    for element in dish_ingr:
        dish_dict = {}
        if i % 2 != 0:
            dish_dict['quantity'] = element
            i = i + 1
            j = j + 1
            list_for_dish.append(dish_dict)
        else:
            dish_dict['measure'] = element
            i = i + 1
            j = j + 1
            list_for_dish.append(dish_dict)
        if j % 2 == 0:
            list_for_dish2.append(list_for_dish)
            list_for_dish = []

    function_dict = {}

    for k,v in zip(dish_name, list_for_dish2):
            function_dict[k] = v

    #print(dish_name)
    #print(dish_ingr)
    print(function_dict)
                    
get_shop_list_by_dishes(['Омлет','Запеченный картофель'], 2)


