import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
random_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
rock_1 = random.choice(random_numbers)
rock_2 = []
summa_list = []
list_for_2 = []
list_for_3 = []
list_for_4 = []
list_for_5 = []
list_for_6 = []
sup_list = []
sup_list_2 = []
sup_list_3 = []
sup_list_4 = []
sup_list_5 = []
sup_list_6 = []


def condition():
    for i in numbers:
        for j in numbers:
            terms_for_2 = 2
            terms_for_3 = 3
            terms_for_4 = 4
            terms_for_5 = 5
            terms_for_6 = 6
            summa = i + j
            div = rock_1 / summa
            if rock_1 == summa and i != j:
                summa_list.extend([i, j])
                break
            if div == terms_for_2 and i != j:
                list_for_2.extend([i, j])
                break
            if div == terms_for_3 and i != j:
                list_for_3.extend([i, j])
                break
            if div == terms_for_4 and i != j:
                list_for_4.extend([i, j])
                break
            if div == terms_for_5 and i != j:
                list_for_5.extend([i, j])
                break
            if div == terms_for_6 and i != j:
                list_for_6.extend([i, j])
                break
    return (summa_list,
            list_for_2,
            list_for_3,
            list_for_4,
            list_for_5,
            list_for_6)

result = condition()
sup_list = list(dict.fromkeys(summa_list))
sup_list_2 = list(dict.fromkeys(list_for_2))
sup_list_3 = list(dict.fromkeys(list_for_3))
sup_list_4 = list(dict.fromkeys(list_for_4))
sup_list_5 = list(dict.fromkeys(list_for_5))
sup_list_6 = list(dict.fromkeys(list_for_6))
rock_2 = (sup_list_6 +
          sup_list_5 +
          sup_list_4[0:2] +
          sup_list_3[0:2] +
          sup_list_2[0:2] +
          sup_list[0:2] +
          sup_list_4[2:] +
          sup_list_3[2:4] +
          sup_list_2[2:4] +
          sup_list[2:4] +
          sup_list_2[4:6] +
          sup_list[4:6] +
          sup_list_2[6:] +
          sup_list[6:])
print("Шифр:", rock_1)
print("Пароль:", ''.join(str(x) for x in rock_2))
