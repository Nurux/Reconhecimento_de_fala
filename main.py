# Trabalhando com reconhecimento de voz

import speech_recognition as sr
from PySimpleGUI import popup_get_file as file
from os import system

def limpar():
    system('cls')

def falar(option):
    if option == 1:
        mic = sr.Recognizer()

        with sr.Microphone() as audio:
            mic.adjust_for_ambient_noise(audio)

            print('Fale alguma coisa: ')

            arq_audio = mic.listen(audio)

            try:
                limpar()
                frase = mic.recognize_google(arq_audio, language='pt-BR')
                print(f'Voce falou:\n{frase}')
            except sr.UnknownValueError:
                print('Não entendi')
            
            return frase 
    else: 
        mp4 = file('Procure o arquivo que queira transcrever ')
        r = sr.Recognizer()
        
        with sr.AudioFile(mp4) as audio:
            txt = r.record(audio)

            try:
                limpar()
                texto = r.recognize_google(txt, language='pt-BR')
                print(f'O audio falava:\n{texto}')
            except sr.UnknownValueError:
                print('Não entendi')
        
        return texto

        
    pass

def main():

    while True:
        print('-'*50)
        print('Bem vindo ao escritor de fala')
        print('-'*50)

        print('1 - Gerar texto a partir de fala')
        print('2 - Gerar texto a partir de audio ')
        print('3 - Sair ')

        try:
            op = int(input('Digite a opção desejada: '))
            limpar()

            if op == 1:
                falar(1)
            elif op == 2:
                falar(2)
            elif op == 3:
                break
            else:
                print('Por favor escolha somente uma das opções propostas no menu')
                continue
        except:
            print('Por favor digite somente o numero da opção desejada')
            continue

if __name__ == '__main__':
    main()