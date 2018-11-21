
# -*- coding: utf8 -*-
"""
   Модуль многопоточного поиска SMTP-сообщений в сетевом трафике, и обработки eml-файлов
"""
#!/usr/bin/python3
import sys
#sys.path.append('./')

from eml_processor import EmlParser as EmlPars

try:
    from Queue import Queue
except Exception:
    from queue import Queue
from threading import Thread

__all__ = ['SMTPHandlersCollection','SMTPStreamHandler']

class SMTPHandlersCollection:
    '''
     Класс SMTPHandlersColection является коллекцией объектов  класса SMTPStreamHandler 
     используемых для обрабатки потоков данных.
     Может управлять обработкой параметрически фиксированным числом потоков данных.
     Каждый новый элемент коллекции создается по мере необходимости в результате вызыва метода handle_stream() 
     кототрому  в качестве параметра передается объект потока данных.
     Элементами коллекции являются экземпляры класса StreamHandler
     По завершению обработки потока данных созданный элемент (обработчик) коллекции живет (для его повторного использования)
     до тех пор пока в очереди есть объекты для обработки и уничтожается по истечению заданного таймаута в случае пустой очереди. 
    '''
    def __init__(self,num_threads=5,queue_stream_size=20):                      
        self.__num_threads=num_threads                   #параметр задающий колличество потоков по умолчанию = 1
        self.__queue_stream_size=queue_stream_size       #параметр задающий размер очереди заданий = 20
        self.__stream_queue=Queue(self.__queue_stream_size)
        
        self.__threads=list()
       
            
    def processing_stream(self,data_stream):
        """
        processing_stream Метод для передачи в обработку потока данных - (API)
        data_stream - объект описывающий поток данных
        """

        self.__stream_queue.put(data_stream,block=True)
        if len(self.__threads) < self.__num_threads:
            thread=SMTPStreamHandler(self.__stream_queue)
            self.__threads.append(thread)
            thread.start()
            #self.__threads[-1].start()

class SMTPStreamHandler(Thread ):
    """
        Класс SMTPStreamHandler является обработчиком потока двоичных либо символьных (ascii) данных. 
    Умеет:
    - распознавать тип входные данные (двоичные либо в кодировке ascii) и выбрать соответствующий алгоритм для их обработки, 
    - извлекать из входных данных почтовые сообщения отправляемые по протоколу SMTP, 
    - извлекать из почтовых сообщений вложенныеф файлы, подсчитать их hash-суммы,
    - формировать метаинформацию о почтовом вложении,
    - сохранять вложения и их описание (hash-суммы и т.д.) в указанный каталог.
    Обрабатывает переданный ему объект потока данных (stream) в отдельном потоке (Thread).
    """
    def __init__(self,queue):
        self.__queue=queue
        self.__eml_parser=EmlPars()
        super(SMTPStreamHandler, self).__init__()
        self.setDaemon(True)
    
    def run(self):
        while not self.__queue.empty():
            stream=self.__queue.get()
            if self.is_eml(stream):
                pass
              # делаем видимость занятости потока
              # путем усыпления его на случайную величину
             # sleep_time=random.randint(0,10)
             # time.sleep(sleep_time)
            self.__queue.task_done()

    def is_binary(self):
        pass

    def is_ascii(self):
        pass

    def is_eml(self,stream):
        pass
        
    def dissect(self):
        pass

              
    


