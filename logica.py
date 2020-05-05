from config import *
from funcoes import *
from webexteams import getwebexMsg, webexmsgRoomviaID
import json
from dna import *

def logica(comando,usermail):

    # faz a logica de entender o comando pedido e a devida resposta para o usuario
    # o parametro usermail e' utilizado para identificar o usuario que solicitou o comando
    # O usuario pode ser uzado como filtro para se executar ou negar o comando
    #
    # Retorna mensagem para ser enviada para console ou Webex teams
    
    #Separa o comando por espacos
    #Primeiro item e'o comando em si, os demais sao parametros deste comando
    #
    
    comando = comando.lower()
    box=comando

    while box == "oi" or box == "ola" or box == "hey" or box == "ei" or box == "alo" or box == "connected medicine oi" or box == "connected medicine ola" or box == "connected medicine hey" or box == "olá" or box == "connected medicine olá":
        msg=""
        arquivo=""
        msg= "Olá eu sou o **Connect Medicine** e estou aqui pra ajudar:" 
        msg=msg+ " "
        msg=msg+ "\n Qual das seguintes opções deseja ?"   
        msg=msg+ " "
        msg=msg+ "\n **(1)** - Ativo mais **próximo** ?"
        msg=msg+ " "
        msg=msg+ "\n **(2)** - Ativos **disponíveis** ?"
        msg=msg+ " "
        msg=msg+ "\n **(3)** - Ventilador mais próximo ?"
        msg=msg+ " "
        msg=msg+ "\n **(4)** - Cadeira de rodas mais próxima ?"
        msg=msg+ " "
        msg=msg+ "\n **(5)** - Onde está o paciente ?"
        msg=msg+ " "
        msg=msg+ "\n **help** - Digite help se precisar de ajuda "
        return msg,arquivo
    else:
        msg=""
        arquivo=""
        box2 = box
        #condicional para os serviços de ativos proximos
        if box2 == "1":
            msg=("o ativo mais próximo é o ativo")
            return msg,arquivo
        elif box2 == "ativo":
            msg="o ativo mais próximo é o ativo 32545"
            return msg,arquivo
        elif box2 == "proximo":
            msg="o ativo mais próximo é o ativo 32545"
            return msg,arquivo
        elif box2 == "ativo proximo":
            msg="o ativo mais próximo é o ativo 32545"
            return msg,arquivo
        #ajudinha antecedendo possíveis erros de digitação de ativos proximos 
        elif box2 == "ativa":
            msg="As palavras que você digitou chegaram perto de 'ativo proximo' e 'proximo', tente elas"
            return msg,arquivo
        elif box2 == "procimo":
            msg="As palavras que você digitou chegaram perto de 'ativo proximo' e 'proximo', tente elas"
            return msg,arquivo
        elif box2 == "acivo":
            msg="As palavras que você digitou chegaram perto de 'ativo proximo' e 'proximo', tente elas"
            return msg,arquivo



        #ativos disponíveis
        elif box2 == "2":
            msg="Os ativos disponíveis são a maca de serial: 12345 e a cadeira de rodas de serial: 12331"
            return msg,arquivo
        elif box2 == "disponivel":
            msg="Os ativos disponíveis são a maca de serial: 12345 e a cadeira de rodas de serial: 12331"
            return msg,arquivo
        elif box2 == "disponibilidade":
            msg="Os ativos disponíveis são a maca de serial: 12345 e a cadeira de rodas de serial: 12331"
            return msg,arquivo
        elif box2 == "ativo disponível":
            msg="Os ativos disponíveis são a maca de serial: 12345 e a cadeira de rodas de serial: 12331"
            return msg,arquivo
        #possíveis erros de digitação em ativos disponíveis
        elif box2 == "disponibel":
            msg="\n As palavras que você digitou chegaram perto de 'disponivel' , 'disponibilidade', tente elas"
            return msg,arquivo        
        elif box2 == "disponibilidads":
            msg="\n As palavras que você digitou chegaram perto de 'disponivel' , 'disponibilidade', tente elas"
            return msg,arquivo


        #Ventilador
        elif box2 == "3" or box2 == "ventilador" or box2 == "ventilador próximo" or box2 == "connected medicine 3" or box2 == "connected medicine ventilador":
            msg= "\n O ventilador pulmonar mais próximo se encontra ={0}".format(localidade_ventilador)
            msg=msg+ " "
            msg=msg+ "\n*Antes de entrar em contato com algum equipamento, lembre-se de utilizar uma mascára e mantenha-se higienizado*"
            msg=msg+ " "
            msg=msg+ "\n Se deseja mais alguma informação, é só dizer 'olá', que irei te ajudar"
            return msg,arquivo
        #Possiveis erros Ventilador
        elif box2 == "vnetilador" or box2 == "ventilado":
            msg= "\n A(s) palavra(s) que você utilizou chegaram perto da palavra chave **ventilador**, tente ela!"
            return msg,arquivo

        #Cadeira
        elif box2 == "4" or box2 == "cadeira" or box2 == "cadeira próxima" or box2 == "cadeira de rodas" or box2 == "connected medicine 4" or box2 == "connected medicine cadeira":
            msg= "\n A cadeira de rodas mais próxima se encontra no {0}".format(localidade_cadeira)
            msg=msg+ " "
            msg=msg+ "\n*Antes de entrar em contato com algum equipamento, lembre-se de utilizar uma mascára e mantenha-se higienizado*"
            msg=msg+ " "
            msg=msg+ "\n Se deseja mais alguma informação, é só dizer 'olá', que irei te ajudar"
            return msg, arquivo
        #Possíveis erros Cadeira
        elif box2 == "cadera" or box2 ==  "cadera roda" or box2 == "cadeira de roda" or box2 =="connected medicine cadera" or box2 == "connected medicine cadeira de roda":
            msg= "\n A(s) palavra(s) que você utilizou chegaram perto da palavra chave **cadeira** e/ou **cadeira de rodas**, tente elas"
            return msg, arquivo

        elif box2 == "5" or box2 == "paciente" or box2 == "pacientes" or box2 == "connected medicine 5" or box2 == "connected medicine paciente" or box2 == "connected medicine pacientes":
            msg= "\n O(s) Paciente(s) se encontram no {0} {1}".format(localidade_paciente, localidade_sonim)
            msg=msg+ " "
            msg=msg+ "\n*Antes de entrar em contato com algum paciente, lembre-se de utilizar uma mascára e mantenha-se higienizado*"
            msg=msg+ " "
            msg=msg+ "\n Se deseja mais alguma informação, é só dizer 'olá', que irei te ajudar"
            return msg, arquivo

        elif box2 == "pacient" or box2 == "pacineti":
            msg="\n A(s) palavra(s) que você utilizou chegaram perto da palavra chave **paciente**, tente ela"

        elif box2 == "help":
            msg="\n "

        
        
        

        
            



    # sp=comando.split(" ")

    # print(sp)
    
    # comando na variavel box, lower deixa em minusculo para normalizar
    
    # Para o caso de nenhum pedido coberto aqui
    
    
    # 21.11.19
    # variavel arquivo para o caso do bot devolver arquivos anexados
    
    # arquivo=""
    
    # msg=""
	
    # chamadas de acordo com os parametros

    # Funcoes para todos
    
    # Uso da funcao "mais"


    #  if len(sp)>2:
    #             tema=sp[1]
    #             msg=maissobre(tema)
    #             print(sp)
    
        
    # # Funcoes que usam outras APIs
    # if len(sp)>1 and box=="api":
    #     # URL
    #     site="apitesteexample.com"
    #     # Parametro de autorizacao
    #     token="123456"
    #     msg=APICall(site,token)
        

    return msg,arquivo


def trataPOST(content):

    # resposta as perguntas via webexteams
    # trata mensagem quando nao e' gerada pelo bot. Se nao e' bot, entao usuario
    try:     
        if content['name']==webhook_name and content['data']['personEmail']!=botmail:
            # identifica id da mensagem
            msg_id=(content['data']['id'])
            # identifica dados da mensagem
            webextalk=getwebexMsg(msg_id)
            usermail=webextalk[2]
            mensagem=webextalk[0]
            sala=webextalk[1]

            # executa a logica
            msg,arquivo=logica(mensagem,usermail)
        
            # Envia resposta na sala apropriada
            webexmsgRoomviaID(sala,msg,arquivo)

    except:
            print("POST nao reconhecido")
            pass