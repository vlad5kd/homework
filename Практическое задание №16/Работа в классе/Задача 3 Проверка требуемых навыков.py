needed_skills = {'Python', 'SQL', 'Git', 'Docker'}

candidate1 = {'Python', 'SQL', 'Git', 'Docker', 'Kubernetes'}
candidate2 = {'Python', 'SQL', 'JavaScript'}
candidate3 = {'Python', 'SQL', 'Git', 'HTML/CSS'}

print("Кандидат 1:")
print("Наличие требуемых навыков: " , needed_skills.issubset(candidate1))
print("Отсутствуют требуемые навыки: ", needed_skills.difference(candidate1))
print("Дополнительные навыки: ", candidate1.difference(needed_skills))

print()

print("Кандидат 2:")
print("Наличие требуемых навыков: " , needed_skills.issubset(candidate2))
print("Отсутствуют требуемые навыки: ", needed_skills.difference(candidate2))
print("Дополнительные навыки: ", candidate2.difference(needed_skills))

print()

print("Кандидат 3:")
print("Наличие требуемых навыков: " , needed_skills.issubset(candidate3))
print("Отсутствуют требуемые навыки: ", needed_skills.difference(candidate3))
print("Дополнительные навыки: ", candidate3.difference(needed_skills))