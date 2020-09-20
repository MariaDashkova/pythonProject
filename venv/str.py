# 1.
# Входящие параметры: int <count> ,
# Результат: string в форме
# "Number of: <count>", где <count> число из вход.парам.
#  Если число равно 10 или более, напечатать "many"
#  вместо <count>
#  Пример: (5) -> "Number of: 5"
#  (23) -> 'Number of: many'
def num_of_items(count):
    if count > 9:
        return "Number of: many"

    return "Number of: " + str(count)



# 2.
# Входящие параметры: string s,
# Результат: string из 2х первых и 2х последних символов s
# Пример 'welcome' -> 'weme'.
def start_end_symbols(s):
    lenth = len(s)
    if (lenth > 1):
        return s[0] + s[1] + s[lenth - 2] + s[lenth - 1]
    return ""



# 3.
# Входящие параметры: string s,
# Результат: string где все вхождения 1го символа заменяются на '*'
# (кроме самого 1го символа)
# Пример: 'bibble' -> 'bi**le'
# s.replace(stra, strb)
def replace_char(my_str):
    my_str = my_str[0] + my_str[1:].replace(my_str[0], '*')  # 'murmurian'
    return (my_str)



# 4
# Входящие параметры: string a и b,
# Результат: string где <a> и <b> разделены пробелом
# а превые 2 симв обоих строк заменены друг на друга
# Т.е. 'max', pid' -> 'pix mad'
# 'dog', 'dinner' -> 'dig donner'
def str_mix(a, b):
    if (len(a) > 1) & (len(b) > 1):
        return b[0:2] + a[2:] + " " + a[0:2] + b[2:]
    return ""



# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.

def test(res, expt):
   print('returns: ' + str(res)+'\n' + 'supposed to return: '+str(expt))
   if str(str(res)) == expt:
       print('ОК' + '\n')
   else:
       print('FAIL' + '\n')

def main():
    test(num_of_items(5),'Number of: 5')
    test(start_end_symbols('welcome'), 'weme')
    test(replace_char('bibble'), 'bi**le')
    test(str_mix('max', 'pid'),'pix mad')

if __name__ == '__main__':
    main()
    print("Everything passed")

