group_1 = ['Иван', 'Мария', 'Петр', 'Сергей', 'Анна']
group_2 = ['Мария', 'Анна', 'Дмитрий', 'Елена', 'Сергей']

myset_1 = set(group_1)
myset_2 = set(group_2)

both_groups = myset_1.intersection(myset_2)
print("Студентов в обеих группах:", both_groups)

only_first = myset_1 - myset_2
print("Студентов только в первой группе:", only_first)

only_second = myset_2 - myset_1
print("Студентов только во второй группе:", only_second)

at_least_one = myset_1.union(myset_2)
print("Студентов хотя бы в одной группе:", at_least_one)

only_one = myset_1.symmetric_difference(myset_2)
print("Студентов только в одной группе:", only_one)