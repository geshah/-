first_ = int(input('Введите число: '))
second_ = int(input('Введите число: '))
third_ = int(input('Введите число: '))
if first_ == second_ == third_:
    print(3)
elif first_ == second_ or second_ == third_ or first_ == third_:
    print(2)
elif first_ != second_ and second_ != third_ and first_ != third_:
    print(0)
