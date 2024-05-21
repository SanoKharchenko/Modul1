grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
a = grades[0]
sum_a = sum(a)
res_a = str(a)
kol_a = len(res_a[1:-1:3])
print(kol_a)  # проверяем правильное отбражение количество оценок у первого студента
print(sum_a)  # проверяем правильно подсчитаную сумму баллов первого студента
sred_ball_a = float(sum_a/kol_a)
print(sred_ball_a)  # проверяем правильно ли подсчитан средний балл первого студента
b = grades[1]
sum_b = sum(b)
res_b = str(b)
kol_b = len(res_b[1:-1:3])
print(kol_b)  # проверяем правильное отбражение количество оценок второго студента
print(sum_b)  # проверяем правильно подсчитаную сумму баллов второго студента
sred_ball_b = float(sum_b/kol_b)
print(sred_ball_b)  # проверяем правильно ли подсчитан средний балл второго студента
c = grades[2]
sum_c = sum(c)
res_c = str(c)
kol_c = len(res_c[1:-1:3])
sred_ball_c = float(sum_c/kol_c)
print(kol_c)  # проверяем правильное отбражение количество оценок третьего студента
print(sum_c)  # проверяем правильно подсчитаную сумму баллов третьего студента
print(sred_ball_c)  # проверяем правильно ли подсчитан средний балл третьего студента
d = grades[3]
sum_d = sum(d)
res_d = str(d)
kol_d = len(res_d[1:-1:3])
sred_ball_d = float(sum_d/kol_d)
print(kol_d)  # проверяем правильное отбражение количество оценок четвертого студента
print(sum_d)  # проверяем правильно подсчитаную сумму баллов четвертого студента
print(sred_ball_d)  # проверяем правильно ли подсчитан средний балл  студента
e = grades[4]
sum_e = sum(e)
res_e = str(e)
kol_e = len(res_e[1:-1:3])
sred_ball_e = float(sum_e/kol_e)
print(kol_e)  # проверяем правильное отбражение количество оценок пятого
print(sum_e)  # проверяем правильно подсчитаную сумму баллов пятого студента
print(sred_ball_e)  # проверяем правильно ли подсчитан средний балл пятого
new_grades = [sred_ball_a,sred_ball_b,sred_ball_c,sred_ball_d,sred_ball_e]
print(new_grades)  # проверяем как записаны оценки
stud_po_alph = sorted(students)
print(stud_po_alph)  # проверяем правильно ли отсортирован список
print(type(stud_po_alph), type(new_grades))  # узнаем тип данных
jornal = {'Aaron': new_grades[0], 'Bilbo': new_grades[1], 'Johnny': new_grades[2], 'Khendrik': new_grades[3], 'Steve':
    new_grades[4]}
print(jornal)
print(type(jornal))
