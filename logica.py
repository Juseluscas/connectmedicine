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
        msg= "Olá\n"
        msg=msg+ "\n"
        msg=msg+ "Estou sempre a disposição para te ajudar!!\n"
        msg=msg+ "\n"
        msg=msg+ "Atualmente posso monitorar os ativos dessa unidade."
        msg=msg+ "\n"
        msg=msg+ " Quando oportuno, poderei muito mais..."
        msg=msg+ "\n"
        msg=msg+ "\n Por favor, escolha as opções abaixo:"   
        msg=msg+ "\n"
        msg=msg+ "\n **(1)** - Ativo mais **próximo** ?"
        msg=msg+ "\n"
        msg=msg+ "\n **(2)** - Ativos **disponíveis** ?"
        msg=msg+ "\n"
        msg=msg+ "\n **(3)** - **Ventilador** mais próximo ?"
        msg=msg+ "\n"
        msg=msg+ "\n **(4)** - **Cadeira de rodas** mais próxima ?"
        msg=msg+ "\n"
        msg=msg+ "\n **(5)** - Onde está o **paciente** ?"
        msg=msg+ "\n"
        msg=msg+ "\n **help** - Digite **help** se precisar de ajuda "
        return msg,arquivo
    else:
        msg=""
        arquivo=""
        box2 = box
        #condicional para os serviços de ativos proximos
        if box2 == "1":
            msg= "Em qual lugar do 12°Andar você está ?\n"
            msg=msg+ "\n"
            msg=msg+ "\n **1)**Corredor         **2)**Retail"
            msg=msg+ "\n"
            msg=msg+ "\n **3)**e-Cafe         **4)**Educação"
            msg=msg+ "\n"
            msg=msg+ "\n **5)**Lobby         **6)**Smartgrid"
            msg=msg+ "\n"
            msg=msg+ "\n **7)**Recepção         **8)**PSS       **9)**Healthcare"
            msg=msg+ "\n"
            msg=msg+ "\n *Use os números para se referênciar*"
            return msg,arquivo


        #ativos disponíveis
        elif box2 == "2" or box2 == "ativos disponíveis" or box2 == "disponível" or box2 == "connected medicine 2" or box2 == "disponíveis" or box2 == "connected medicine ativos disponíveis" or box2 == "disponível" or box2 == "connected disponível" or box2 == "connected 2":
            msg= "Os ativos disponíveis são: \n"
            msg=msg+ "\n"
            msg=msg+ "\n O ventilador que está no(a) {}".format(localidade_ventilador)
            msg=msg+ "\n"
            msg=msg+ "\n A cadeira de rodas que está no(a) {}".format(localidade_cadeira)
            msg=msg+ "\n"
            msg=msg+ "\n O paciente 1 que está no(a) {}".format(localidade_paciente)
            msg=msg+ "\n"
            msg=msg+ "\n O paciente 2 que está no(a) {}".format(localidade_cliente)
            return msg,arquivo
    


        #Ventilador
        elif box2 == "3" or box2 == "ventilador" or box2 == "ventilador próximo" or box2 == "connected medicine 3" or box2 == "connected medicine ventilador" or box2 == "connected 3" or box2 == "connected ventilador":
            msg= "\n O ventilador pulmonar mais próximo se encontra no(a){0}".format(localidade_ventilador)
            msg=msg+ "\n"
            msg=msg+ "\n*Antes de entrar em contato com algum equipamento, lembre-se de utilizar uma mascára e mantenha-se higienizado*"
            msg=msg+ "\n"
            msg=msg+ "\n Se deseja mais alguma informação, é só dizer **'olá'**, que irei te ajudar"
            return msg,arquivo
        #Possiveis erros Ventilador
        elif box2 == "vnetilador" or box2 == "ventilado":
            msg= "\n A(s) palavra(s) que você utilizou chegaram perto da palavra chave **ventilador**, tente ela!"
            return msg,arquivo

        #Cadeira
        elif box2 == "4" or box2 == "cadeira" or box2 == "cadeira próxima" or box2 == "cadeira de rodas" or box2 == "connected medicine 4" or box2 == "connected medicine cadeira" or box2 == "connected cadeira" or box2 == "connected 4" or "connected cadeira":
            msg= "\n A cadeira de rodas mais próxima se encontra no(a) {0}".format(localidade_cadeira)
            msg=msg+ "\n"
            msg=msg+ "\n*Antes de entrar em contato com algum equipamento, lembre-se de utilizar uma mascára e mantenha-se higienizado*"
            msg=msg+ "\n"
            msg=msg+ "\n Se deseja mais alguma informação, é só dizer **'olá'**, que irei te ajudar"
            return msg, arquivo
        #Possíveis erros Cadeira
        elif box2 == "cadera" or box2 ==  "cadera roda" or box2 == "cadeira de roda" or box2 =="connected medicine cadera" or box2 == "connected medicine cadeira de roda" or box2 == "connected medicine 4":
            msg= "\n A(s) palavra(s) que você utilizou chegaram perto da palavra chave **cadeira** e/ou **cadeira de rodas**, tente elas"
            return msg, arquivo

        elif box2 == "5" or box2 == "paciente" or box2 == "pacientes" or box2 == "connected medicine 5" or box2 == "connected medicine paciente" or box2 == "connected medicine pacientes" or box2 == "connected paciente" or box2 == "connected 5":
            msg= "\n O paciente 1 se encontra no(a): {0}".format(localidade_paciente)
            msg=msg+ "\n"
            msg=msg+ "\n O paciente 2 se encontra no(a): {0}".format(localidade_cliente)
            msg=msg+ "\n"
            msg=msg+ "\n*Antes de entrar em contato com algum paciente, lembre-se de utilizar uma mascára e mantenha-se higienizado*"
            msg=msg+ "\n"
            msg=msg+ "\n Se deseja mais alguma informação, é só dizer **'olá'**, que irei te ajudar"
            return msg, arquivo

        elif box2 == "pacient" or box2 == "pacineti":
            msg="\n A(s) palavra(s) que você utilizou chegaram perto da palavra chave **paciente**, tente ela"
            return msg, arquivo
        elif box2 == "help" or box2 == "connected medicine help" or box2 == "connected help":
            msg="\n "
            return msg, arquivo 

        
        
        

        
            



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