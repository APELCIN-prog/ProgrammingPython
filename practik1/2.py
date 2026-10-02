n = int(input())
def chet(num):
    if num % 2 == 0:
        print(f'число {num} чётное')
    else:
        print(f'число {num} нечётное')
def razmer(num):
    if num > 0:
        print(f'число {num} положительное')
    elif num < 0:
        print(f'число {num} отрицательное')
    else:
        print(f'число {num} это 0')
def in_range(num):
    if 10 <= num <= 50:
        print(f'число {num} принадлежит диапазону [10; 50]')
    else:
        print(f'число {num} не принадлежит диапазону [10; 50]')

chet(n)
razmer(n)
in_range(n)