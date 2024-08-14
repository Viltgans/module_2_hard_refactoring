import random

numbers = list(range(1,21))
random_numbers = list(range(3,21))
rock_1 = random.choice(random_numbers)
summa_list = []
list_for_2 = []
list_for_3 = []
list_for_4 = []
list_for_5 = []
list_for_6 = []


def condition():
    for i in numbers:
        for j in numbers:
            if rock_1 == (i + j) and i != j:
                summa_list.extend([i, j])
                continue
            if (rock_1 / (i + j)) == 2 and i != j:
                list_for_2.extend([i, j])
                continue
            if (rock_1 / (i + j)) == 3 and i != j:
                list_for_3.extend([i, j])
                continue
            if (rock_1 / (i + j)) == 4 and i != j:
                list_for_4.extend([i, j])
                continue
            if (rock_1 / (i + j)) == 5 and i != j:
                list_for_5.extend([i, j])
                continue
            if (rock_1 / (i + j)) == 6 and i != j:
                list_for_6.extend([i, j])
                continue
    return (summa_list,
            list_for_2,
            list_for_3,
            list_for_4,
            list_for_5,
            list_for_6)


def duplicate(old_list):
    for item in old_list:
        if item in old_list:
            old_list.remove(item)
    old_list.reverse()
    return old_list


condition()
duplicate(summa_list)
duplicate(list_for_2)
duplicate(list_for_3)
duplicate(list_for_4)
duplicate(list_for_5)
duplicate(list_for_6)

rock_2 = (list_for_6 +
          list_for_5 +
          list_for_4[0:2] +
          list_for_3[0:2] +
          list_for_2[0:2] +
          summa_list[0:2] +
          list_for_4[2:] +
          list_for_3[2:4] +
          list_for_2[2:4] +
          summa_list[2:4] +
          list_for_2[4:6] +
          summa_list[4:6] +
          list_for_2[6:] +
          summa_list[6:])
print("Шифр:", rock_1)
print("Пароль:", ''.join(str(x) for x in rock_2))
