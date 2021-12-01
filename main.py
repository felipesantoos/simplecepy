from tkinter.constants import E
import requests
import json
import PySimpleGUI as sg

class PythonScreen:
    def __init__(self):
        layout = [
            [sg.Text("CEP"), sg.Input(size = (25, 0), key="CEP")],
            [sg.Button("Buscar")],
            [sg.Output(size = (40, 10))]
        ]

        self.screen = sg.Window("Buscar por CEP", layout)

    def search_by_CEP(self, CEP):
        URL = requests.get(f"https://viacep.com.br/ws/{CEP}/json/")
        
        if URL.status_code == 200:
            print("Solicitação realizada com sucesso!")
        else:
            print(f"Erro {URL.status_code}")
        
        address = URL.json()

        return address
    
    def start_window(self):
        while True:
            self.button, self.values = self.screen.Read()

            try:
                values = self.search_by_CEP(self.values["CEP"])
                for k, v in values.items():
                    print(f"{k}: {v}")
            except:
                print("Name error, function not defined!")

app = PythonScreen()
app.start_window()
