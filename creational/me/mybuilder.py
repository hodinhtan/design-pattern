import abc

class Director:
    # tao ra doi tuong su dung Builder interface
    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()

class Builder(abc.ABC):
    def __init__(self): 
        # khi thang builder nao dc tao ra thi se co Product khoi tao ben trong
        self.product = Product()

    @abc.abstractmethod
    def _build_part_a(self): # tao ra a
        pass

class Product:
    pass

class ConcreteBuilder(Builder):
    def _build_part_a(self):
        print("tao phuong thuc a")


def main():
    # tao ra doi tuong builder cu the
    concrete_builder = ConcreteBuilder()
    concrete_builder2 = ConcreteBuilder()
    
    # tao ra director
    director = Director()

    director.construct(concrete_builder)
    product = concrete_builder.product # product duoc tao ra 
    print(product)

    director.construct(concrete_builder2)
    product = concrete_builder2.product # product duoc tao ra 
    print(product)

if __name__ == "__main__":
    main()


    # thang giam doc Director thue thang BUilder xay dung mot san pham product
    # thang nha thau chinh builder co san quy trinh xay dung (cac abstracmethod)
    # thang builder cho thang cac thang thau phu concretebuilder 1,2 xay dung nhung phai theo quy trinh
    # cua no (phai co cac method do). Con lam the nao thi ke tui no (implement lai cac method)
    # thang thau phu 1,2 se tao ra cac san pham product 1,2 khac nhau
