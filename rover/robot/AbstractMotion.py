from abc import ABCMeta, abstractmethod

class AbstractMotion(metaclass=ABCMeta):
    @property
    @abstractmethod
    def forward(self): pass
    def reverse(self): pass
    def left(self): pass
    def right(self): pass
