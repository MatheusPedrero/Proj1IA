from abc import ABC, abstractmethod

class AbstractRegrasJogo(ABC):
    def init(self) -> None:
        super().init()
        mapa_labirinto = { 
                [ ['+','+','+','+',...,'+','+','+','+','+','+','+'],
                  ['+',' ',' ',' ',...,' ',' ',' ','+',' ',' ',' '],
                  ['+',' ','+',' ',...,'+','+',' ','+',' ','+','+'],
                  ['+',' ','+',' ',...,' ',' ',' ','+',' ','+','+'],
                  ['+','+','+',' ',...,'+','+',' ','+',' ',' ','+'],
                  ['+',' ',' ',' ',...,'+','+',' ',' ',' ',' ','+'],
                  ['+','+','+','+',...,'+','+','+','+','+',' ','+'],
                  ['+',' ',' ',' ',...,'+','+',' ',' ','+',' ','+'],
                  ['+',' ','+','+',...,' ',' ','+',' ',' ',' ','+'],
                  ['+',' ',' ',' ',...,' ',' ','+',' ','+','+','+'],
                  ['+','+','+','+',...,'+','+','+',' ','+','+','+']]
            }

        self.labirinto = mapa_labirinto
        self.id_personagens = {Personagens.JOGADOR: 0}
        self.acoes_personagens = {0: None}
        self.msg_jogador = None

    @abstractmethod
    def registrarAgentePersonagem(self, personagem):
        return self.id_personagens[personagem]
    
    @abstractmethod
    def isFim(self,linha,coluna):
        return(linha == 0 or
             linha == self.linhas-1 or
             coluna == 0 or
             coluna == self.parede_adjacente-1 )

    @abstractmethod
    def gerarCampoVisao(self, id_agente):
        percepcoes_jogador = PercepcoesJogador(
            pos_jogador=set(self.labirinto),
            dimensoes=(11, 11),
            mensagem_jogo=self.msg_jogador)

        self.msg_jogador = None
        return percepcoes_jogador

    @abstractmethod
    def registrarProximaAcao(self, id_agente, acao):

        self.acoes_personagens[id_agente] = acao

        return
    
    @abstractmethod
    def atualizarEstado(self, diferencial_tempo):
        acao_jogador = self.acoes_personagens[
            self.id_personagem[Personagens.JOGADOR]]
        if acao_jogador.tipo == AcoesJogador.MOVER_BOLINHA:
            x, y, direcao = acao_jogador.parametros

            if (x, y) in self.labirinto:
                x_mov, y_mov = self.decodificar_direcao(direcao)

                parede_adjacente = (x + x_mov, y + y_mov)
                espaco_pos_adjacente = (x + x_mov2, y + y_mov2)
                if self.is_jogada_valida(parede_adjacente, espaco_pos_adjacente):
                    self.labirinto.discard(parede_adjacente)
                    self.labirinto.discard((x,y))
                    self.labirinto.add(espaco_pos_adjacente)
                    else:
                        self.msg_jogador = f'Impossivel de realizar o movimento, parede a frente.'
            else:
                self.msg_jogador = f'Tecla inválida.'
        return
    
    @abstractmethod
    def terminarJogo(self):
        """ Faz procedimentos de fim de jogo, como mostrar placar final,
        gravar resultados, etc...
        """
        return

def construir_jogo(*args,**kwargs):
    """ Método factory para uma instância RegrasJogo arbitrária, de acordo com os
    parâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    return NomeDoSeuJogo()