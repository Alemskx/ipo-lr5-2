str1 = str(input("Введите первую строку: ")).lower()
str2 = str(input("Введите вторую строку: ")).lower()
if str1 == str2:
    print("Строки не являются анаграммами.")
    
if len(str1)!=len(str2):
    print("Строки не являются анаграммами.")

if sorted(str1) == sorted(str2):
    print("Строки являются анаграммами.")
else:
    print("Строки не являются анаграммами.")