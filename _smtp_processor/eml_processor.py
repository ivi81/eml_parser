# -*- coding: utf8 -*-
"""
  _eml_processor - модуль структурного разбора email-сообщений
"""
#!/usr/bin/python3

import datetime
import base64
import struct
import hashlib

import os
import mimetypes
import email

import time
import random

__all__ = ['EmlParser']

class EmlParser:
    """
    Класс EmlParser извлекает вложения из почтовых сообщений, декодирует их,
    формируюет метаинформацию о письме, сохраняет вложения в структуру каталогов на диске.
    """
    def __init__(self):
        pass

    def pars_eml(self, msg):
        """
         Метод pars_eml извлекет вложения из письма
        """
        if msg.is_multipart():
            for part in msg.get_payload():
                self.pars_eml(part)
        else:
            if(msg.get_content_maintype() != 'text'):
                print(msg.get_content_type())
                conver_from_base64(msg)  
            else:
                conver_from_base64(msg)   


        def conver_from_base64(self , msg):
            main_mime_type = msg.get_content_maintype()    #Извлекаем информацию о типе вложения
            sub_mime_type = msg.get_content_subtype()      #Извлекаем информацию о подтипе вложения
            charset = msg.get_charsets()[0]                #Извлекаем информацию о первоначальной кодировке в которой находится вложение 
            raw_data = msg.get_payload()                   #Извлекаем тело вложения
            raw_data = base64.b64decode(raw_data)          #Декодируем тело вложения из Base64 в строку байт 'b'
            ext = mimetypes.guess_extension(msg.get_content_type())
            if(main_mime_type == "text"):
                if(charset is not None):
                    raw_data = raw_data.decode(charset)
                    print(raw_data)
            else:
                m = hashlib.sha256()
                s = m.update(raw_data)
                d = m.hexdigest()
                file_name = msg.get_filename()
        
            print("###########################################################")

        def mkdir_eml_content(**kwargs):
            """ 
            mkdir_eml_content
            Вспомогательная функция создающая двухуровневую структуру папок 
            на основании заданных параметров 'dir' и 'file'.
            В итоге получаем path = '/dir/file'
            Если 'dir' или 'file' = None то они генерируются на основе системной даты.
            """
            if (kwargs.get('dir') is None):
                kwargs['dir'] = os.getcwd()+"/dir_"+datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            if (kwargs.get('file') is None):
                kwargs['file'] = "file_"+datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            try:
                full_path = kwargs['dir']+"/"+kwargs['file']
                os.makedirs(full_path)
            except FileExistsError as e:
                if (os.path.isdir(full_path)): #Если папка была созданна раньше то ждем секунду
                    time.sleep(1)       
                kwargs['file'] = '{0}_{1}'.format(kwargs['file'],datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))  #Если названия файла или папки совпадают с создаваемой паки то создаем её с названием текущей датой и временем
                full_path = mkdir_eml_content(**kwargs)
            return full_path


    ''' with open(eml_path,'rb') as fp:
            msg=email.message_from_binary_file(fp)
           
            full_path=mkdir_eml_content(dir=os.getcwd()+"/dst_eml")   
            pars_eml(msg)
    '''