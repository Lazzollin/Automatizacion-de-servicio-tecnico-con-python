import urllib.request
import time
import url
from bs4 import BeautifulSoup, NavigableString
from tkinter import *


def get_html():
    req = urllib.request.Request(
        url.url,
        headers={"User-Agent": "Chrome"})
    res = urllib.request.urlopen(req)
    result = urllib.request.urlopen(req).read()
    return result


def get_question(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.text
    wanted_text = [x.strip() if isinstance(x, NavigableString) else x.text.strip() for x in
                   soup.find('p')]
    return wanted_text


def understand_monkeys(poo_poo):
    access_dic = ['ingreso', 'inscripcion', ' inscribirse']
    audio_dic = ['sonido', 'no escucho']
    c_video_dic = ['conexion', 'lento', 'conexion lento', 'conexion lenta']
    n_video_dic = ['pantalla en negro', 'imagen negra']

    type_of_question = []

    for i in range(len(access_dic)):
        if access_dic[i].lower() in poo_poo.lower():
            type_of_question.append('access')

    for i in range(len(audio_dic)):
        if audio_dic[i].lower() in poo_poo.lower():
            type_of_question.append('audio')

    for i in range(len(c_video_dic)):
        if c_video_dic[i].lower() in poo_poo.lower():
            type_of_question.append('c_video')

    for i in range(len(n_video_dic)):
        if n_video_dic[i].lower() in poo_poo.lower():
            type_of_question.append('n_video')

    if len(type_of_question) >= 2 or len(type_of_question) == 0:
        return 'generico'
    else:
        return type_of_question


def message(type_of_message):
    my_message = ''

    if type_of_message == 'generico':
        my_message = 'respuesta generico'

    if type_of_message == 'access':
        my_message = 'respuesta access'

    if type_of_message == 'audio':
        my_message = 'respuesta audio'

    if type_of_message == 'c_video':
        my_message = 'respuesta c_video'

    if type_of_message == 'n_video':
        my_message = 'respuesta n_video'

    return my_message


if __name__ == '__main__':
    master = Tk()

    label = Label(master, text="manucoso")

    w = Canvas(master, width=600, height=150)
    w.pack()

    startTime = time.time()
    lastQuestion = ""
    xd = 0

    up_text = w.create_text(300, 12, fill="black", font="Monospaced 16 ",
                            text="Ultima pregunta")

    question_text = w.create_text(300, 52, fill="black", font="Monospaced 10 ",
                                  text="")

    ptdp = w.create_text(300, 72, fill="black", font="Monospaced 10 ",
                         text='')

    pr_text = w.create_text(300, 92, fill="black", font="Monospaced 10 ",
                            text='')

    xd_text = w.create_text(300, 112, fill="black", font="Monospaced 10 ",
                       text=("xd" + str(xd)))
    while True:
        xd += 1
        question = get_question(get_html())
        if question != lastQuestion:
            print("Ultima pregunta: ", question)
            w.delete(up_text)
            w.delete(question_text)
            w.delete(ptdp)
            w.delete(pr_text)

            up_text = w.create_text(300, 12, fill="black", font="Monospaced 16 ",
                          text="Ultima pregunta")

            question_text = w.create_text(300, 52, fill="black", font="Monospaced 10 ",
                          text=question)

            ptdp = w.create_text(300, 72, fill="black", font="Monospaced 10 ",
                          text=("Posible tipo de pregunta: " + understand_monkeys(str(question))))

            pr_text = w.create_text(300, 92, fill="black", font="Monospaced 10 ",
                          text=("Posible respuesta: " + message(understand_monkeys(str(question)))))
            w.update()
            lastQuestion = question

        w.delete(xd_text)

        xd_text = w.create_text(300, 112, fill="black", font="Monospaced 10 ",
                      text=("xd" + str(xd)))

        w.update()

        time.sleep(30.0 - ((time.time() - startTime) % 30.0))

