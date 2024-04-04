ПРОЕКТ


# # Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# # Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
#
#
# binarx=list()
# binary=list()
#
# def binar_r(n,m):
#     if n<1 and m <1:
#         return 1
#
#     x = n%2
#     y=m%2
#     #print('m=',m)
#     binarx.append(x)
#     binary.append(y)
#
#
#     #print('binarm',binarm)
#     n= n//2
#     m=m//2
#     #print('n=',n)
#
#     return binar_r(n,m)
#
# n=5
# m=6
# binar = binar_r(n,m)
# binarx.reverse()
# binary.reverse()
# print(f'число {n} в довичной системе: {binarx} , число {m} в довичной системе: {binary}')
#
# AND=[]
# for i in range(0,3):
#     x=binarx[i]&binary[i]
#     AND.append(x)
# print(f' результат операции Побитовое И (поразрядная конъюнкция) над числами {m} и {n} равен {AND}')
#
# XOR=[]
# for i in range(0,3):
#     z=binarx[i]^binary[i]
#     XOR.append(z)
# print(f' результат операции Побитовое исключающее ИЛИ (поразрядная дизъюнкция) над числами {m} и {n} равен {XOR}')
#
# OR=[]
# for i in range(0,3):
#     z=binarx[i]| binary[i]
#     OR.append(z)
# print(f' результат операции Побитовое НЕ над числами {m} и {n} равен {OR}')
#
#
# shift_left=binarx.copy()
# shift_right=binarx.copy()
# #x=0
# for i in range(2,0,-1):
#
#     shift_left.append(0)
#     del shift_right[i]
# print(f'побитовый сдвиг  на два  числа 5 вправо равен {shift_right}  и влево  равен {shift_left}')
#
#

# #Посчитать четные и нечетные цифры введенного натурального числа.
# # Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
#
#
# n = input('Введите натуральное число: ')
# num=[]
#
# sum_even =[]
# sum_odd =[]
#
# for i in n:
#  num.append(i)
#
# for x in range(0,len(num)):
#     a= num[x]
#     #print(a)
#     if int(a) % 2 !=0:
#         sum_odd.append(num[x])
#     else:
#      sum_even.append(num[x])
# #
# print(f' в числе {n}  количество нечетных цифр {len(sum_odd)}  эти числа {sum_odd}, количество четных цифр {len(sum_even)}  эти числа {sum_even} ' )


# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# import random
# n=20
#
# arr=list()
#
# for x in range(n):
#     number =random.randint(1,100)
#     arr.append(number)
# # #
#
# a = min(arr)
# b=max(arr)
#
# x= arr.index(a)
# y=arr.index(b)
#
# print(f'массив: {arr}')
# print(f' минимальный элемент: {a}  индекс: {x} , максимальный элемент: {b} индекс: {y}')
#
#
#
# #print(x,y)
#
# arr.remove(a)
# arr.remove(b)
#
# arr.insert(x,b)
# arr.insert(y,a)
#
# #del arr[y]
# print('массив с поменяными местами минимальный и максимальный элементам: ')
# print(arr)


# Отсортируйте по убыванию методом пузырька одномерный
# целочисленный массив, заданный случайными числами на
# промежутке [-100; 100]. Выведите на экран исходный и
# отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая
# принимает на вход массив данных;
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас
# должна остаться сортировка пузырьком. Улучшенные версии
# сортировки, например, расчёской, шейкерная и другие в зачёт не
# идут

# import random
# import collections
#
# n=10
# #step=0
# arr=list()
# for x in range(n):
#     number =random.randint(-100,100)
#     arr.append(number)
#
# print('Исходный массив : ')
# print(arr)
# ######################
# #
#
#
#
# def sort(arr):
#  is_sorted = False
#  for i in range(n):
#    if is_sorted is True:
#       break
#    else:
#      for j in range(n-1):
#
#         if arr[j] > arr[j+1]: #Пузырек
#            # print('no sorted arr', arr, )
#             temp=arr[j]
#             arr[j]=arr[j+1]
#             arr[j+1]=temp
#             #step+=1
#             if arr == sorted(arr):  # если список отсортирован, то выходим из цикла.
#                 print('Массив отсортирован: ',arr)
#                 is_sorted=True
#
#                 break
#         elif arr == sorted(arr):  # если список отсортирован, то выходим.
#             print('Массив отсортирован ', step, arr)
#             is_sorted = True
#             break
#
# sort(arr)


# Отсортируйте по возрастанию методом слияния одномерный
# вещественный массив, заданный случайными числами на
# промежутке [0; 50]. Выведите на экран исходный и
# отсортированный массивы.


# import random
# import collections
#
# n=10
# #step=0
# arr=list()
# for x in range(n):
#     number =random.randint(0,50)
#     arr.append(number)
#
# print('Исходный массив : ')
# print(arr)
#
# def merge(arrl,arrr):
#     sorted_arr= list()
#     curent_left=0
#     curent_right=0
#
#     len_l=len(arrl)
#     len_r=len(arrr)
#
#     for i in range(len_l+len_r):
#
#         if curent_left < len_l and curent_right < len_r:
#
#           if arrl[curent_left] < arrr[curent_right]:
#             sorted_arr.append(arrl[curent_left])
#             curent_left+=1
#
#           else:
#             sorted_arr.append(arrr[curent_right])
#             curent_right += 1
#
#         else:
#
#            if curent_left == len_l:
#                for j in range(curent_right,len_r):
#                    sorted_arr.append(arrr[j])
#
#            else:
#
#                for j in range(curent_left, len_l):
#                    sorted_arr.append(arrl[j])
#
#            break
#
#     return sorted_arr
#
# def merge_sort(arr):
#    if len(arr) <=1:
#        return  arr
#
#    mid=len(arr)//2
#    left_side=list()
#    right_side=list()
#
#    for i in range(0,mid):
#      val=arr[i]
#      left_side.append(val)
#
#    for i in range(mid,len(arr)):
#        val = arr[i]
#        right_side.append(val)
#
#
#
#    left_side=merge_sort(left_side)
#    right_side=merge_sort(right_side)
#
#    result=merge(left_side,right_side)
#    return result
#
#
# arr=merge_sort(arr)
# print('Cортированный массив:',arr)

#
# 2.6. На улице встретились N друзей. Каждый пожал руку всем
# остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

# def create_graph(l):
#     return [[0 if i >= j else 1 for j in range(l)] for i in range(l)]
#
# def sum_graph(graph):
#     result = 0
#     for i in graph:
#         result += sum(i)
#     return result
#
# n = 6
# new_graph = create_graph(n)
# print(f' количество друзей {n} , количество рукопожатй: {sum_graph(new_graph)}')


#  Закодируйте любую строку по алгоритму Хаффмана

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


def count_frequencies(string):
    frequencies = {}
    for char in string:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


def build_huffman_tree(frequencies):
    nodes = []
    for char, freq in frequencies.items():
        nodes.append(Node(char, freq))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes[0]
        right = nodes[1]
        parent = Node(None, left.freq + right.freq, left, right)
        nodes = nodes[2:]
        nodes.append(parent)

    return nodes[0]


def encode_string(string, huffman_tree):
    encoding = {}

    def traverse_tree(node, code):
        if node.char:
            encoding[node.char] = code
        else:
            traverse_tree(node.left, code + "0")
            traverse_tree(node.right, code + "1")

    traverse_tree(huffman_tree, "")

    encoded_string = ""
    for char in string:
        encoded_string += encoding[char]

    return encoded_string


string = "abracadabra"
frequencies = count_frequencies(string)
huffman_tree = build_huffman_tree(frequencies)
encoded_string = encode_string(string, huffman_tree)

print(f'Исходная строка: {string}')
print(f'Кодированная  строка: {encoded_string}')



