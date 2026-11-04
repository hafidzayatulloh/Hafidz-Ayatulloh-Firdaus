car = 'subaru'
age = 20
foods = ['nasi', 'tempe', 'tahu']

print("Kesamaan string")
print(car == 'subaru')
print(car == 'audi')

print("\nKetidaksamaan string")
print(car != 'audi')
print(car != 'subaru')

print("\nMetode lower()")
print('SUBARU'.lower() == car)
print('Audi'.lower() == car)

print("\nTes angka: sama dengan dan tidak sama dengan")
print(age == 20)
print(age == 25)
print(age != 25)
print(age != 20)

print("\nTes angka: lebih dari dan kurang dari")
print(age > 18)
print(age > 20)
print(age < 30)
print(age < 20)

print("\nTes angka: lebih dari atau sama dengan, kurang dari atau sama dengan")
print(age >= 20)
print(age >= 21)
print(age <= 20)
print(age <= 19)

print("\nKata kunci and")
print(age > 15 and age < 30)
print(age > 15 and age < 18)

print("\nKata kunci or")
print(age < 10 or age > 18)
print(age < 10 or age > 50)

print("\nItem ada di dalam list")
print('tempe' in foods)
print('bakso' in foods)

print("\nItem tidak ada di dalam list")
print('bakso' not in foods)
print('tempe' not in foods)