# ООП
# принципы ООП:
#

class Book:
    strr = 400

    def __init__(self, title, author, color):
        self.title = title
        self.author = author
        self.color = color

    def info(self):
        print(self.title, self.author, self.color, self.strr)

    def __str__(self):
        return (f'Title: {self.title}, Author: {self.author},\n'
                f'Color: {self.color}, strr: {self.strr}\n')

    def __len__(self):
        return len(self.title + self.author + self.color)

# объект\экземпляр класса
город_воров=Book('город воров', 'Байжигит', 'зеленый')
капитанская_дочка=Book('Капитанская дочь', 'Пушкин', 'серый')

beka=Book('ЭТОМИР', 'beka', 'black')
print(len(beka))

ls=[1,1,1,1,1]
print(ls)







# город_воров.info()
# капитанская_дочка.info()


