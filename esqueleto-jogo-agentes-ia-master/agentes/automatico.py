from agentes.humano import AgentePrepostoESHumano
class automatico(AgentePrepostoESHumano):

    def init(self):
        # Uma sequencia de acoes, inicialmente vazia
        self.seq = []

    def formularProblema(self):
        
    def adquirirPercepcao(self, percepcao_mundo):
        super().adquirirPercepcao(percepcao_mundo)

        self.percepcao_mundo = percepcao_mundo.disposicao_elementos

         def tartaruga(self, coluna, linha)
     if jogador[linha][coluna] == OBSTACLE :
        return False
     
     if jogador[linha][coluna] == TRIED:
        return False   
     
     if jogador.isFim(linha,coluna, parte_caminho):
        jogador.updatePosition(linha,coluna)
        return True
    jogador.updatePosition(linha,coluna, TRIED)

   
    encontrado = searchFrom(jogador, linha-1,coluna) or \
            searchFrom(jogador, linha+1, coluna) or \
            searchFrom(jogador, linha, coluna-1) or \
            searchFrom(jogador, linha, coluna+1)
    if encontrado:
        jogador.updatePosition(linha,coluna, parte_caminho)
    else:
        jogador.updatePosition(linha,coluna, fim_caminho)
    return encontrado   


    def escolherProximaAcao(self):
        
    
   





   
    