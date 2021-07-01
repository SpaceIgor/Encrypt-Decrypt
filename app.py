from flask import  Flask
from flask import request, render_template

app= Flask (__name__)
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

@app.route ("/")
@app.route ("/encrypt")
def encrypt ():
    '''Эта страница (ф-ция) служит для шифрования строки, которую вводит пользователь в адресную строку.
    Пользовтель вводит свой текст в формате /encrypt?string=<string_to_encrypt> и делает запрос на страницу,
    которая выводит ему зашифрованный текст. Например, Encrypted result: adf9420-12fnkadl;f=4fjmqe.'''
    str = request.args.get ('string')
    if str== '' or str is None:
        return render_template("index.html", title="Параметр не был введен. "
                                                   "Пожалуйста, введите строку для шифровки в адреской строке!")
    else:
        string = f.encrypt (str.encode())
        return render_template("index.html", title="Encrypted result: ", string=string)

@app.route ("/decrypt")
def decrypt ():
    '''Эта страница (ф-ция) служит для расшифровки строки, которую вводит пользователь в адресную строку.
    Пользовтель вводит код, представляющий из себя зашифрованный текст (который он предварительно получил при помощи
    страницы encrypt) в адресную
    строку в формате /decrypt?string=<string_to_decrypt> и делает запрос на страницу. Страница возвращает пользователю
    расшифрованный текст.
    Пример: Decrypted result: Hello World!
    '''
    str = request.args.get ('string')
    if str== '' or str is None:
        return render_template("index.html", title="Параметр не был введен. "
                                                   "Пожалуйста, введите строку для шифровки в адреской строке!")
    else:
        string = f.decrypt(str.encode())
        return render_template ("index.html", title= "Decrypted result: ", string=string)

if __name__ == '__main__':
    app.run (debug = True)