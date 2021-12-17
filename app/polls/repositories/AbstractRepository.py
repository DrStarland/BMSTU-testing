#import abc
from ..models import *
from abc import ABCMeta, abstractmethod, abstractproperty

class abstractclassmethod(classmethod):
    slots = ()

    def init(self, function):
        super(abstractclassmethod, self).init(function)
        function.isabstractmethod = True

    isabstractmethod = True

class CRUDRepository:
    metaclass = ABCMeta

    @staticmethod  
    def connect(user):
        pass

    @classmethod
    @abstractmethod
    def create(c, user, model):
        """Добавить объект model в соответствующую модели таблицу"""
        pass

    @classmethod
    @abstractmethod
    def read_all(c, user):
        """Прочитать все объекты"""
        pass

    @classmethod
    @abstractmethod
    def update_all(c, user, update_dict):
        """Обновить все объекты"""
        pass

    @classmethod
    @abstractmethod
    def delete_filtered(c, user, filter_dict):
        """Удалить выборку объектов по фильтру"""
        pass