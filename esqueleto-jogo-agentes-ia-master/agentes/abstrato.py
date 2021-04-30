from abc import ABC, abstractmethod

class AgenteAbstrato(ABC):
    '''
    Classe abstrata de agentes artificiais racionais.
    '''

    @abstractmethod
    def adquirirPercepcao(self, percepcao_mundo):
        ''' Forma uma percepcao interna por meio de seus sensores, a partir das
        informacoes de um objeto de visao de mundo.
        '''
        return
    
    @abstractmethod
    def escolherProximaAcao(self):
        ''' Escolhe proxima acao, com base em seu entendimento do mundo, a partir
        das percepções anteriores.
        '''
        return

def construir_agente(*args, **kwargs):
    """ Método factory para uma instância Agente arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    from agentes.humano import AgentePrepostoESHumano
    return AgentePrepostoESHumano()

while True:
        resp = input('1 -> Agente humano.'+"\n"+ 
                     '2 -> Agente BFS.'+"\n"+
                     '3 -> Agente DFS.'+"\n"+
                     '4 -> Agente DFS limitado.'+"\n"+
                     '5 -> Agente DFS com aprofundamento Iterativo.'+"\n"+
                     '6 -> Busca gulosa.'+"\n"+
                     '7 -> Busca A-Estrela'+"\n"
                    )
        if resp == '1':
            return AgentePrepostoESHumano()
        elif resp == '2':
            return AgenteBFS()    