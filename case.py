#место для твоего кода

import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance.csv')
df.info()
print(df['parental level of education'].value_counts())
print('Кто умнее девочки или мальчики?')
men_math_result = df[df['gender']=='male']['math score'].mean()
women_math_result = df[df['gender']=='female']['math score'].mean()
men_reading_result = df[df['gender']=='male']['reading score'].mean()
women_reading_result = df[df['gender']=='female']['reading score'].mean()
men_writing_result = df[df['gender']=='male']['writing score'].mean()
women_writing_result = df[df['gender']=='female']['writing score'].mean()

female_free = 0
female_standart = 0

def lunch_counter(row):
    global female_free, female_standart
    if row['gender'] =='female' and row['lunch'] == 'standart':
        female_standart+1
    return False 
df.apply(lunch_counter, axis = 1)
print(female_free, female_standart)
print(female_free, female_standart)

print('Результат парней по математике:', round(men_math_result,2))
print('Результат девушек по математике:', round(women_math_result,2))
print('Результат парней по чтению:', round(men_reading_result,2))
print('Результат девушек по чтению:', round(women_reading_result,2))
print('Результат парней по письму:', round(men_writing_result,2))
print('Результат девушек по письму:', round(women_writing_result,2))
print('Девочки сильнее в гуманитарных науках, а мальчики в точных науках')
print('Влияет ли качество питания на результаты тестов?')
standart_math = df[df['lunch']=='standard']['math score'].mean()
free_math = df[df['lunch']=='free/reduced']['math score'].mean()
standart_reading = df[df['lunch']== 'standard']['reading score'].mean()
free_reading = df[df['lunch']=='free/reduced']['reading score'].mean()
standart_write = df[df['lunch']== 'standard']['writing score'].mean()
free_write = df[df['lunch']== 'free/reduced']['writing score'].mean()
print('Реультаты по математике:', 'Стандарт:', round(standart_math,2),'Бесплатное:',round(free_math,2))
print('Реультаты по чтению:', 'Стандарт:', round(standart_reading,2),'Бесплатное:',round(free_reading,2))
print('Реультаты по письму:', 'Стандарт:', round(standart_write,2),'Бесплатное:',round(free_write,2))
print('Гипотеза подтверждена. Питание влияет на качество обучения')


genders = df['gender'].value_counts()
genders.plot(kind = 'pie')
plt.show()
s = pd.Series(data=[men_math_result, women_math_result, men_reading_result, women_reading_result,men_writing_result, women_writing_result])
index = ['Математика парня', 'Математика девушки', 'Чтение парня', 'Чтение девушки', 'Письмо парня', 'Письмо девушки'],
s.plot(kind ='barh')
plt.show()