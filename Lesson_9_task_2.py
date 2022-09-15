# Задача 2.
# Закодируйте любую строку по алгоритму Хаффмана.

string = 'nice sleepy hedgehog'
all_freq = {}

for i in string:

    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

sorted_values = dict(sorted(all_freq.items(), key=lambda item: item[1]))
print(f"Количество всех символов в строке: {sorted_values}.")

# Класс узла
class Node():
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.leftchild = None
        self.rightchild = None

# Создать дерево Хаффмана
class HuffmanTree():

    def __init__(self, char_Weights):
        self.Leaf = [Node(k,v) for k, v in char_Weights.items()]
        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda node: node.value, reverse=True)
            n = Node(value=(self.Leaf[-1].value + self.Leaf[-2].value))
            n.leftchild = self.Leaf.pop(-1)
            n.rightchild = self.Leaf.pop(-1)
            self.Leaf.append(n)
        self.root = self.Leaf[0]
        self.Buffer = list(range(10))

    # Создавать коды с рекурсивным мышлением
    def Hu_generate(self, tree, length):

        node = tree
        if not node:
            return
        elif node.name:
            print(f'[{node.name}] - ' + 'кодировка Хаффмана:', end='')
            for i in range(length):
                print(self.Buffer[i], end='')
            print('\n')
            return

        self.Buffer[length] = 0
        self.Hu_generate(node.leftchild, length + 1)
        self.Buffer[length] = 1
        self.Hu_generate(node.rightchild, length + 1)

    #Output кодировка Хаффмана
    def get_code(self):
        self.Hu_generate(self.root, 0)

if __name__=='__main__':
    tree = HuffmanTree(sorted_values)
    tree.get_code()
