
class Notification:
    def __init__(self, message):
        self._message = message

    def get_message(self):
        return self._message
        
    def send(self):
        print(f'Вам пришло сообщение: {self._message}')

    

class SMSNotification(Notification):
    def __init__(self, message):
        super().__init__(message)

    def get_message(self):
        return self._message
    
    def send(self):
        return f"У вас новое СМС сообщение: {self._message}"
    
    def set_message(self):
        new_message = input('Введите новое SMS сообщение')
        self._message = new_message
        print(f'Ваше новое сообщение - {self._message}')



class EmailNotification(Notification):
    
    def __init__(self, message):
        super().__init__(message)

    def get_message(self):
        return self._message
    
    def send(self):
        return f"У вас новое письмо: {self._message}"
    
    def set_message(self):
        new_message = input('Введите новое письмо: ')
        self._message = new_message
        print(f'Ваше новое письмо - {self._message}')



notifications = [SMSNotification('Hello'), EmailNotification('Bye')]
for i in notifications:
    print(i.send())
    i.set_message()
        
