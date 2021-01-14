"""

# Mục đích:
    - Cung cấp một interface cho một họ đối tượng liên quan hoặc phụ thuộc mà không cần chỉ rõ lớp cụ thể của chúng
    - Một hệ thống phân cấp bao gồm nhiều: Nhiều platform có thể có và xây dựng một bộ "products"
    - phương thức new bị xem là không tốt

# Đặt vấn đề:
  Nếu một ứng dụng có thể portable, nó cần được đóng gói vào nền tảng phụ thuộc. Platform này có thể bao gồm: windowing system, OS, database, etc. Và quá thường xuyên là những bản đống gói này sẽ không được sử dụng tốt, và các trường hợp  #ifdef với các tùy  chọn sẽ được tạo ra như thỏ trong code.

From sourcemaking.com
"""
"""
Provide an interface for creating families of related or dependent
objects without specifying their concrete classes.
"""

import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    """
    Declare an interface for operations that create abstract product
    objects.
	->  Định nghĩa interface cho việc tạo đối tượng trừu tương product
    """

    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Implement the operations to create concrete product objects.
    """

    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Implement the operations to create concrete product objects.
    """

    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface_a(self):
        pass


class ConcreteProductA2(AbstractProductA):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface_a(self):
        pass


class AbstractProductB(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface_b(self):
        pass


class ConcreteProductB2(AbstractProductB):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface_b(self):
        pass


def main():
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()
        print(product_a)
        print(product_b)


if __name__ == "__main__":
    main()
