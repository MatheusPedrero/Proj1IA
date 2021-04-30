from agentes.abstrato import AgenteAbstrato
class AgentePrepostoESHumano(AgenteAbstrato):
    
    def adquirirPercepcao(self, percepcao_mundo):
        aux = ''
        elems_dipostos = percepcao_mundo.disposicao_elementos
        i=0
        for i in range(len(elems_dipostos)):
            if elems_dipostos[i] != 0: 
                aux = aux+' '+str(elems_dipostos[i])
            else:
                aux = aux+' '+' '

            if ((i == 2) or (i == 5) or (i == (len(elems_dipostos)-1))):
                
                print(aux+'\n')
                aux = ''
    
    def escolherProximaAcao(self):
        from acoes import AcaoJogador
        escolhido = input("Proxima ação (W - cima, S - baixo, D - direita, A -esquerda)?  ")
        return AcaoJogador.permutar(escolhido)