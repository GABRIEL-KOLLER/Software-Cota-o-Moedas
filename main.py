# importar o App, Builder (GUI)
# criar o nosso aplicativo
# criar a função build

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["moeda 1"].text = f"Dólar R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda 2"].text = f"Euro R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda 3"].text = f"Bitcoin R${self.pegar_cotacao('BTC')}"
        self.root.ids["moeda 4"].text = f"Ethereum R${self.pegar_cotacao('ETH')}"



    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao







MeuAplicativo().run()
