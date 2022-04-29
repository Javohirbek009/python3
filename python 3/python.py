# def funksiya
#  while qachonki
# for
# .lower kickich harflar
# .upper katta harflar

# def nomi():






# boshlash = input('boshlash uchun 1 raqamini kiriting: ').lower()
# # for x in range(100):
# #     print('hello')

# while boshlash == '1':
#     print('o`yin boshlandi')
#     print('o`yin tugadi')
#     boshlash = input('boshlash uchun 1 raqamini kiriting: ')



num1 = int(input('sonni kiriting: '))
num2 = int(input('ikkichi sonni kiriting: '))
value = input('Amalni kiriting: ')

# if cont == 'ha':

if value == '+':
    print("Natija: " + str(num1 + num2))
    

cont = input('Davom etishni hohlaysizmi: ').lower()
while cont == 'ha':
    num1 = int(input('sonni kiriting: '))
    num2 = int(input('ikkinchi sonni kiriting: '))
    value = input('Amalni kiriting: ')
    print("Natija: " + str(num1 + num2))