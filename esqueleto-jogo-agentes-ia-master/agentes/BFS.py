from agentes.humano import AgentePrepostoESHumano
class BFS(AgentePrepostoESHumano):

    def init(self):
        # Uma sequencia de acoes, inicialmente vazia
        self.seq = []

    def formularProblema(self):
        
    def adquirirPercepcao(self, percepcao_mundo):
        super().adquirirPercepcao(percepcao_mundo)

        self.percepcao_mundo = percepcao_mundo.disposicao_elementos


    def escolherProximaAcao(self):