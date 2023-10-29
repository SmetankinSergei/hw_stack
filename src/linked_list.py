class LinkedList:
    def __init__(self):
        self.__content = []
        self.__head = None
        self.__tail = None

    def __str__(self):
        res = f'{self.__head.data} -> '
        next_node = self.__head.next_node
        while next_node:
            res += f'{next_node.data} -> '
            next_node = next_node.next_node
        res += 'None'
        return res

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    def insert_beginning(self, data):
        node = Node(data, None)
        if not self.__content:
            self.__insert_first_node(node)
        else:
            node.next_node = self.__content[0]
            self.__head = node
            self.__content.append(node)

    def insert_at_end(self, data):
        node = Node(data, None)
        if not self.__content:
            self.__insert_first_node(node)
        else:
            self.__content[-1].next_node = node
            self.__tail = node
            self.__content.append(node)

    def __insert_first_node(self, node):
        self.__content.append(node)
        self.__head = node
        self.__tail = node

    def to_list(self):
        """Возвращает список данных всех Node"""
        return [node.data for node in self.__content]

    def get_data_by_id(self, item_id):
        """Возвращает словарь по id, если данные - это словарь, и в нём есть такой id"""
        for item in self.to_list():
            # if not isinstance(item, dict) or 'id' not in item.keys():
            #     raise TypeError("Данные не являются словарем или в словаре нет id")
            """В задании сказано, что обработку сделать нужно тут, но мне кажется, что тот вариант, который я 
            закомментировал, был бы лучше. Потому как мы предоставляем обработку ошибки вызывающему коду! а не делаем 
            это за него так, как хотим. Может в вызывающем коде нужно что-то другое в этом случае. То есть 
            гибкость страдает, переиспользование под вопросом"""
            try:
                if item['id'] == item_id:
                    return item
            except:
                raise TypeError("Данные не являются словарем или в словаре нет id")




class Node:
    def __init__(self, data, next_node):
        self.__data = data
        self.next_node = next_node

    def __str__(self):
        return f'{__class__.__name__}({self.__data})'

    @property
    def data(self):
        return self.__data
