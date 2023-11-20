import pyautogui
import random
import time
import pydirectinput
from PIL import Image

#SCRIPT WINDOWS PC
#SCRIPT LVL 120+ COM SH VILE

#ROBO COM SHINY VILEPLUME SEM ISCA

#CODIGO QUE DERROTA O SHINY GIANT MAGIKARP E JOGA BALL NELE
#LUGAR: CHAT ME

#VARIAVEL CONTAGEM QUASE MORTES
quase = 0
#VARIAVEL CONTAGEM SHINY
shiny = 0
#VARIAVEL CHAT
chat = 0
#VARIAVEL PLAYER
pl = 0
#VARIVEL ESPERA CD
cd = 0
#REGIÃO MINI GAME PEIXE
REGION = (667, 336, 30, 356)
#REGIÃO BARRA DE TAREFAS
REGIONBARRAWIN = (0,732, 1100, 33)
#REGIÃO MAR PARA PESCA 1
REGIONMAR1 = (790, 428, 72, 60)
#REGIÃO MAR PARA PESCA 2
REGIONMAR2 = (831, 417, 81, 72)
#REGIÃO CHAT
REGCHAT = (219, 649, 459, 42)
#REGIÃO BAT
REGBAT = (1164, 400, 198, 149)
#REGIAO CHAT PV
REGPV = (255, 620, 534, 33)
#VARIAVEL TEMPO HUMAN TEST
tempo = 0
#VARIAVEL CALCULA FALHAS HUMAN TEST
falhou = 0
#VARIAVEL NAO MOSTRA TEMPO CASO FALHAS HUMAN TEST
humanfail = 0
#VARIAVEL SAIR WHILE PESCA PARA NET DOWN
pescanet = 0


#FUNÇÃO INICIAR PXG
def initpxg():

    #ARMAZENA A IMAGEM
    image = Image.open('pxgmeclient.png')
    #LOCALIZAR A IMAGEM NA TELA E CLICA NELA
    if pyautogui.locateOnScreen('pxgmeclient.png', confidence=0.8, region=REGIONBARRAWIN):

        imagelocation = pyautogui.locateOnScreen(image, confidence=0.8, region=REGIONBARRAWIN)
        imagelocation2 = pyautogui.center(imagelocation)
        #LOCALIZA OS EIXOS X E Y E ARMAZENA NA ARRAYLIST
        l, u = imagelocation2[0], imagelocation2[1]

        pyautogui.moveTo(l, u)
        pyautogui.click()

    else:

        #ALERTA QUE NAO ENCONTROU O CLIENT AO INICIAR
        pyautogui.alert('NÃO FOI ENCONTRADO CLIENT PXG')

        exit()
        
    time.sleep(2)

    #SE ENCONTRAR O ICONE DA PARTY SEGUE O CÓDIGO SE NAO PARA O CODIGO
    if pyautogui.locateCenterOnScreen('party-init.png', confidence=0.9, region=REGPV):

        pass
    
    else:

        #ALERTA QUE NAO ENCONTROU O CLIENT AO INICIAR
        pyautogui.alert('NÃO FOI ENCONTRADO O ICONE DA PARTY')

        exit()


#FUNÇÃO PEGA LOOT
def loot():

    #LOOT
    pydirectinput.keyDown('e')
    time.sleep(0.3)
    pydirectinput.keyUp('e')


#FUNÇÃO VIDA BAIXA OU POKE DEAD
def redvida():

    #TORNAR GLOBAL VARIAL SAIR
    global sair

    sair = 0

    time.sleep(4)

    #SE O POKE MORRER
    if pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)):

        sc = pyautogui.screenshot()
        sc.save('CHECAR-RED.png')

        sair = 1

        print('ENTROU DEAD POKE REDVIDA')

        #SELECIONAR REVIVE
        pyautogui.moveTo(x=771, y=581)
        pyautogui.click()

        #MOVER PARA O SH VILE
        pyautogui.moveTo(x=35, y=50)
        pyautogui.click()

        time.sleep(1)

        #CLICAR SH VILEPLUME
        pyautogui.moveTo(32, 53)
        pyautogui.click()

        time.sleep(1)

        #MID POKE
        pyautogui.moveTo(689, 243)
        pyautogui.middleClick()
        time.sleep(2)

        #PARE-MID
        pydirectinput.keyDown('shift')
        pydirectinput.keyDown('s')
        pydirectinput.keyUp('shift')
        pydirectinput.keyUp('s')

            
#FUNÇÃO SAIR JOGO CHAT
def sairjogo():

    #ENQUANTO NAO TIVER SAIDO DO JOGO FICAR TENTANDO
    while pyautogui.pixelMatchesColor(976, 236, (212, 212, 212)):

        #CTRL + Q PARA DAR DISPLAY DO MENU SAIR
        pydirectinput.keyDown('ctrl')
        pydirectinput.keyDown('q')
        pydirectinput.keyUp('ctrl')
        pydirectinput.keyUp('q')

        time.sleep(2)

        #CONFIRMAR SAIR
        pydirectinput.press('enter')

        time.sleep(4)
    
    #ESPERA UM POUCO (1hr // 3600s)
    time.sleep(3600)

    #SE ESTIVER NA PARTE DE LOGIN (PUXA COR ENGRENAGEM)
    if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

        #IR PARA JOGAR
        pyautogui.moveTo(x=679, y=628)
        pyautogui.click()

        #ESPERA LOGAR
        time.sleep(30)

        #CLICAR VILEPLUME
        pyautogui.moveTo('vilepoke.png')
        pyautogui.click()

        time.sleep(1.5)
    
    else:

        print('SAIU JOGO N ENCONTROU')

        #SAIR JOGO
        pyautogui.moveTo(x=1342, y=12)
        pyautogui.click()

        time.sleep(1)

        #CLICAR SIM SAIR JOGO
        pyautogui.moveTo(x=569, y=409)
        pyautogui.click()

        exit()


#FUNÇÃO VOLTAR PXG QND CAIR NET
def caiunet():

    #CAPTURAR A TELA
    sc = pyautogui.screenshot()
    sc.save('fimbotnet.png')

    #300 - espera voltar net
    time.sleep(300)

    #CLICAR BOTÃO JOGAR CIMA
    pyautogui.moveTo(x=762, y=78)
    pyautogui.click()

    time.sleep(1)

    #CLICAR BOTÃO JOGAR AZUL
    pyautogui.moveTo(x=687, y=642)
    pyautogui.click()
    
    #35 - espera entrar server
    time.sleep(35)

    #CHECAGEM BOTÃO VERMELHO
    if pyautogui.pixelMatchesColor(777, 478, (171, 51, 26)):

        #CLICAR BOTÃO CANCELAR
        pyautogui.moveTo(793, 476)
        pyautogui.click()

        #MINIMIZA
        pyautogui.moveTo(x=1242, y=14)
        time.sleep(1.5)
        pyautogui.click()

        print('PROBLEMA NET OU SERVER')

        exit()


    #CHECAGEM COR X
    if pyautogui.pixelMatchesColor(976, 236, (212, 212, 212)):

        #CLICAR VILEPLUME
        pyautogui.moveTo('vilepoke.png')
        pyautogui.click()

        time.sleep(1.5)
    
    else:

        #CAPTURA A TELA ERRO NET
        sc = pyautogui.screenshot()
        sc.save('fimbotnet-ou-dead.png')

        #SAIR JOGO
        pyautogui.moveTo(x=1342, y=12)
        pyautogui.click()

        time.sleep(1)

        #CLICAR SIM SAIR JOGO
        pyautogui.moveTo(x=569, y=409)
        pyautogui.click()

        print('SAIU DO JOGO')

        exit()


#FUNÇAO CHAT
def resposta():

    global chat

    #CHAT 1
    if chat == 0:

        #CHECA COR CHAT
        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):

            sc = pyautogui.screenshot()
            sc.save('chat1.png')
            
            #ANTI-GM
            chatbot()


#FUNÇÃO CHECEGAGEM PLAYER
def checagemplayer():

    global pl
    global sair

    #CASO BUGAR CORRIGE CHECKPLAYER (icone poke)
    if pyautogui.pixelMatchesColor(1256, 387, (102, 102, 102)):

        #CLICAR NO ICONE PLAYER BATTLE 1
        pyautogui.moveTo(x=1185, y=384)
        pyautogui.click()

    #CASO BUGAR ICONE PLAYER
    if pyautogui.pixelMatchesColor(1184, 392, (204, 204, 204)):

        #REMOVER ICONE PLAYER BATTLE 1
        pyautogui.moveTo(x=1185, y=384)
        pyautogui.click()


    #CLICAR NO ICONE POKEBATTLE 1
    pyautogui.moveTo(x=1256, y=387)
    pyautogui.click()

    #CLICAR NO ICONE PLAYER BATTLE 1
    pyautogui.moveTo(x=1185, y=384)
    pyautogui.click()

    time.sleep(0.5)

    #CHECAGEM PLAYER PARADO
    if pyautogui.pixelMatchesColor(1221, 482, (7, 9, 12)):

        pl = 0
    
    else:

        pl = pl + 1

        #SAI E VOLTA DO JOGO CASO HOUVER PLAYER NA TELA
        if pl == 5: 

            print('PLAYER TELA, MANDANDO MENSAGEM')

            sc = pyautogui.screenshot()
            sc.save('PLAYER-TELA.png')

            pydirectinput.press('enter')

            pyautogui.write('TEXTO')
            time.sleep(0.2)
            pydirectinput.press('enter')

            #APAGA CHAT
            pyautogui.moveTo(1084, 634)
            pyautogui.click()

            #sairjogo()
            #sair = 1


    #RETIRAR ICONE PLAYER BATTLE 2
    pyautogui.moveTo(x=1185, y=384)
    pyautogui.click()

    #CLICAR NO ICONE POKEBATTLE 2
    pyautogui.moveTo(x=1256, y=387)
    pyautogui.click()

    time.sleep(1)

    #CASO BUGAR ICONE PLAYER
    if pyautogui.pixelMatchesColor(1184, 392, (204, 204, 204)):

        #RETIRAR ICONE PLAYER BATTLE 2
        pyautogui.moveTo(x=1185, y=384)
        pyautogui.click()

    #CASO BUGAR CORRIGE CHECKPLAYER (icone poke)
    if pyautogui.pixelMatchesColor(1256, 387, (102, 102, 102)):

        #CLICAR NO ICONE POKEBATTLE 2
        pyautogui.moveTo(x=1256, y=387)
        pyautogui.click()


#FUNÇÃO ESPERA PESCA
def espera_pesca():

    global pescanet

    while True:

        try:

            #SE IDENTIFICAR A BOLHA NA AGUA ELE CLICA NA PESCA 2
            if pyautogui.locateOnScreen('bolha.png', confidence=0.7, region=REGIONMAR2):
                
                #if pescanet > 99:
                    #print('&&&&&&&&111&&&&&&&&&&&&', pescanet)

                break
            
            #SE IDENTIFICAR A BOLHA NA AGUA ELE CLICA NA PESCA 1
            if pyautogui.locateOnScreen('bolha.png', confidence=0.7, region=REGIONMAR1):

                #if pescanet > 99:
                    #print('&&&&&&&&222&&&&&&&&&&&', pescanet)

                break

            else:

                pescanet = pescanet + 1
                
                #REALIZA CONTAGEM PESCA PARA VERIFICAR SE CAIU NET
                if pescanet == 200:

                    print('SAINDO CICLO PESCA PARA VERIFICAR SE CAIU NET')

                    break
        except:
            
            #CASO GERAR ALGUM ERRO ESPERAR 10S
            time.sleep(10)

            #GERAR INFORME DE ERRO
            print('ERRO GERADO 808012')


#FUNÇÃO CHATBOT GM
def chatbot():

    #ENCONTRA CHAT GM E SAI DA PXG
    if pyautogui.locateCenterOnScreen('gm.png', confidence=0.8, region=REGCHAT):

        pydirectinput.press('enter')

        pyautogui.write('TEXTO-GM')
        time.sleep(0.2)
        pydirectinput.press('enter')

        time.sleep(1.5)
        pydirectinput.press('enter')

        pyautogui.write('TEXTO-GM')
        time.sleep(0.2)
        pydirectinput.press('enter')

        time.sleep(1.5)

        sc = pyautogui.screenshot()
        sc.save('GM-TELA.png')

        #CTRL + Q PARA DAR DISPLAY DO MENU SAIR
        pydirectinput.keyDown('ctrl')
        pydirectinput.keyDown('q')
        pydirectinput.keyUp('ctrl')
        pydirectinput.keyUp('q')

        time.sleep(2)

        #CONFIRMAR SAIR
        pydirectinput.keyUp('enter')
        pydirectinput.keyDown('enter')

        print('GM NA TELA')
        exit()


#FUNÇAO SAIRBOT PARA SAIR 1HR
def sairbot():

    global sair

    #IDENTIFICAR SAIDA PXG
    if pyautogui.locateCenterOnScreen('party.png', confidence=0.9, region=REGPV):

        #CLICANDO NO PV PARTY
        image = Image.open('party.png')
        imagelocation = pyautogui.locateCenterOnScreen(image, confidence=0.9, region=REGPV)
        h , j = imagelocation[0], imagelocation[1]

        pyautogui.moveTo(h,j)
        pyautogui.click()

        time.sleep(1.5)

        sair = 1

        #IDENTIFICAR SAIDA PXG
        if pyautogui.locateCenterOnScreen('comando-sair.png', confidence=0.8, region=REGCHAT):

            sairjogo()


#FUNÇÕES JOGAR ISCA LAGO 1
def lago1():

    pyautogui.moveTo(823, 467)
    pyautogui.click()


#FUNÇÕES JOGAR ISCA LAGO 2
def lago2():

    pyautogui.moveTo(868, 462)
    pyautogui.click()


#IR PARA PXG
initpxg()

time.sleep(1)

#PARE-MID
pydirectinput.keyDown('shift')
pydirectinput.keyDown('s')
pydirectinput.keyUp('shift')
pydirectinput.keyUp('s')

#CICLO PESCA, ATTACK, LOOT, FUGIR
while True:

    #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
    if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

        caiunet()
        cd = 0
        continue

    #VARIAVEL VOLTA AO COMEÇO SHINY
    sair = 0
    #VARIAVAL PROTEC PLAYER
    battleplayer = 0
    #VOLTANDO VARIAVEL TEMPO
    tempo = 0
    #VOLTANDO VARIAVEL FALHA HUMAN TEST
    humanfail = 0
    #VOLTANDO VARIAVEL PESCANET
    pescanet = 0

    #VERIFICAÇAO RED & YELLOW LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)):

        redvida()
        quase = quase + 1
        print('O total de quase mortes foi:', quase)
        continue

    #LOOT GERAL
    loot()

    #ESPERA CD
    if cd == 1:
        
        #SE CONTIVER ALGO NA PRIMEIRA POSI NO BAT
        if pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)):

            #SE NAO TIVER NADA ELE PASSA
            pass

        else:

            #SE TIVER FEEBAS NO BAT
            
            #CASO OCORRER ALGUM ERRO ELE PASSA
            try:

                #ENQUANTO TIVER UM POKEMON NO BATTLE ELE EXECUTA VERIFICAÇÃO REDLIFE
                while pyautogui.locateOnScreen('feebas.png', confidence=0.8, region=REGBAT) or pyautogui.locateOnScreen('feebas-red.png', confidence=0.8, region=REGBAT):
                    
                    #ATACAR BAT 1
                    if battleplayer == 0:
                        try:
                            image = Image.open('feebas.png')
                            imagelocation = pyautogui.locateCenterOnScreen(image, confidence=0.8, region=REGBAT)
                            u , p = imagelocation[0], imagelocation[1]

                            #CLICAR NO FEEBAS
                            pyautogui.moveTo(u,p)
                            pyautogui.click()

                        except:

                            pass

                        #2 - SEED ABSORB
                        time.sleep(1)
                        pyautogui.moveTo(x=597, y=514)
                        pyautogui.click()


                    #SOMATORIA VARIVEL PARA SAIR WHILE
                    battleplayer = battleplayer + 1

                    #SE FALHAR AO CLICAR NO FEEBAS TENTA NOVAMENTE
                    if pyautogui.locateOnScreen('feebas.png', confidence=0.8, region=REGBAT):

                        battleplayer = 0

                    #VERIFICAÇAO RED & YELLOW LIFE
                    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)):

                        redvida()
                        quase = quase + 1
                        print('O total de quase mortes foi:', quase)
                        sair = 1
                        
                    #4 - MAGIC LEAF
                    time.sleep(1)
                    pyautogui.moveTo(x=667, y=515)
                    pyautogui.click()

                    #5 - LEAF BLADE
                    time.sleep(1)
                    pyautogui.moveTo(x=704, y=514)
                    pyautogui.click()

                    #5 - RAZOR LEAF
                    time.sleep(1)
                    pyautogui.moveTo(x=633, y=514)
                    pyautogui.click()

                    #SE TIVER ALGUEM DO LADO (protec player)
                    if battleplayer == 45:
                        print('sistema entrou no protec player, a contagem parou em', battleplayer)
                        break
            except:

                pass

    #VOLTAR AO COMEÇO (UTILIZA POR CONTA DO 'WHILE')
    if sair == 1:
        continue

    #ESPERA CD NA VOLTA
    cd = 1

    #PESCA 1
    pyautogui.moveTo(x=346, y=582)
    pyautogui.click()

    #LAGO
    #LISTA SQMs LAGO
    lagolista = [lago1,lago2]
    #JOGA ALEATORIAMENTE EM EM SQM DA LSITA
    random.choice(lagolista)()

    #LOOT GERAL 2
    loot()

    #CICLO CHECAGEM POSIÇÃO POKE
    for posi in range(0, 2):

        #CHECAGEM POKE POSIÇÃO
        if pyautogui.pixelMatchesColor(689, 243, (157, 109, 60)) == True:

            #MID POKE
            pyautogui.moveTo(689, 243)
            pyautogui.middleClick()
            time.sleep(2)

            #PARE-MID
            pydirectinput.keyDown('shift')
            pydirectinput.keyDown('s')
            pydirectinput.keyUp('shift')
            pydirectinput.keyUp('s')


    #FOME POKEMON
    if pyautogui.pixelMatchesColor(175, 84, (203, 98, 79)):

        #CLICA NA FOOD
        time.sleep(0.5)
        pyautogui.moveTo(x=809, y=585)
        pyautogui.click()

    #ESPERAR QUALQUER MSG
    time.sleep(3)

    #CHECAGEM PESCA LAGO
    if pyautogui.pixelMatchesColor(664, 279, (119, 166, 200)):

        pass

    else:
        
        #REMOVE PESCA BUGADA
        pyautogui.moveTo(7, 31)
        pyautogui.click()

        #VOLTA NO INICIO
        continue

    #PARE-MID
    pydirectinput.keyDown('shift')
    pydirectinput.keyDown('s')
    pydirectinput.keyUp('shift')
    pydirectinput.keyUp('s')

    #CHAMA FUNÇÃO RESPOSTA CHAT
    resposta()

    #CHAMA FUNCAO SAIRBOT CASO BOT MAIN MANDAR SAIR
    sairbot()

    #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
    if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

        caiunet()
        cd = 0
        continue

    #VOLTAR AO COMEÇO (UTILIZA POR CONTA DO 'WHILE')
    if sair == 1:
        continue

##############################################################################################################

    #EXECUTA FUNÇÃO QUE IDENTIFICA BOLHA NO MAR
    espera_pesca()

##############################################################################################################

    #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
    if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

        caiunet()
        cd = 0
        continue

    #VOLTAR AO COMEÇO (UTILIZA POR CONTA DO 'WHILE')
    if sair == 1:
        continue

    #ESPERA CD 1
    while pyautogui.pixelMatchesColor(562, 523, (34, 96, 12)) or pyautogui.pixelMatchesColor(559, 527, (16, 42, 10)):
        
        time.sleep(1)

        #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
        if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

            caiunet()
            cd = 0
            sair = 1
            break

    #VOLTA INICIO CODIGO
    if sair == 1:

        continue

    #PESCA 2
    pyautogui.moveTo(x=346, y=582)
    pyautogui.click()

    time.sleep(1.3)

    #ENCONTRA TEST HUMAN
    while pyautogui.pixelMatchesColor(683, 543, (17, 17, 17)) == False:

        #ENTROU HUMAN TEST
        tempo = 1

        peixe = pyautogui.locateOnScreen('peixeg.png', confidence=0.8, region=REGION, grayscale= True)
        barra = pyautogui.locateOnScreen('pontabarra.png', confidence=0.8, region=REGION)

        #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
        if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

            caiunet()
            cd = 0
            sair = 1
            break

        if peixe != None and barra != None:

            if barra.top > peixe.top:
                
                pydirectinput.keyDown('space')

            else:
                
                pydirectinput.keyUp('space')
        
        else:
            #desbuga a tecla espaço 1
            pydirectinput.keyDown('space')
            time.sleep(0.2)
            pydirectinput.keyUp('space')


    time.sleep(0.5)

    #desbuga a tecla espaço 2
    pydirectinput.keyDown('space')
    time.sleep(0.2)
    pydirectinput.keyUp('space')

    #VOLTA INICIO CODIGO
    if sair == 1:

        continue

    #VERIFICAÇÃO SHINY
    for s in range(0, 3):

        #VERIFICA COR E POKE SH KINGLER BAT
        if pyautogui.locateOnScreen('estrela-shiny.png', confidence=0.8, region=REGBAT):
            
            #CONTANDO OS SHINY
            shiny = shiny + 1
            print('-----'*20)
            print('O total de shinys que apareceram eh:', shiny)
            print('-----'*20)

            #ESPERA DESCER O SH CASO ESTIVER NO TOPO
            time.sleep(1)

            #9 - SOLZIN
            #time.sleep(1)
            #pyautogui.moveTo(x=847, y=513)
            #pyautogui.click()

            try:
                #ATACAR SHINY GIANT MAGIKARP
                image = Image.open('estrela-shiny.png')
                imagelocation = pyautogui.locateCenterOnScreen(image, confidence=0.8, region=REGBAT)
                h , j = imagelocation[0], imagelocation[1]

                #CLICAR DIRETO NO SHINY
                h = h - 25
            
                #CLICAR SHINY
                pyautogui.moveTo(h,j)
                pyautogui.click()

            except:
                
                pass

            #7 - PETAL BLIZARD
            time.sleep(1)
            pyautogui.moveTo(x=780, y=511)
            pyautogui.click()

            #8 - DORMIR
            time.sleep(1)
            pyautogui.moveTo(x=810, y=514)
            pyautogui.click()

            #1 - ABSORB SEED RAIN
            time.sleep(1)
            pyautogui.moveTo(x=560, y=518)
            pyautogui.click()

            #4 - MAGIC LEAF
            time.sleep(1)
            pyautogui.moveTo(x=667, y=515)
            pyautogui.click()

            #5 - LEAF BLADE
            time.sleep(1)
            pyautogui.moveTo(x=704, y=514)
            pyautogui.click()

            #3 - RAZOR LEAF
            time.sleep(1)
            pyautogui.moveTo(x=633, y=514)
            pyautogui.click()

            #2 - SEED ABSORB
            time.sleep(1)
            pyautogui.moveTo(x=597, y=514)
            pyautogui.click()

            time.sleep(2)

            #ENQUANTO TIVER UM POKEMON NO BATTLE ELE EXECUTA VERIFICAÇÃO REDLIFE
            while pyautogui.locateOnScreen('estrela-shiny.png', confidence=0.8, region=REGBAT):

                print('entrou no cd while SHINY')
                battleplayer = battleplayer + 1

                #ATTKS

                #4 - MAGIC LEAF
                time.sleep(1)
                pyautogui.moveTo(x=667, y=515)
                pyautogui.click()

                #VERIFICAÇAO RED & YELLOW LIFE
                if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)):

                    redvida()
                    quase = quase + 1
                    print('O total de quase mortes foi:', quase)
                    sair = 1

                #SAI DO LOOP CASO SAIR FOR IGUAL 1
                if sair == 1:
                    break
        
                #5 - LEAF BLADE
                time.sleep(1)
                pyautogui.moveTo(x=704, y=514)
                pyautogui.click()

                #VERIFICAÇAO RED & YELLOW LIFE
                if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)):

                    redvida()
                    quase = quase + 1
                    print('O total de quase mortes foi:', quase)
                    sair = 1
                
                #SAI DO LOOP CASO SAIR FOR IGUAL 1
                if sair == 1:
                    break

                #5 - RAZOR LEAF
                time.sleep(1)
                pyautogui.moveTo(x=633, y=514)
                pyautogui.click()

                #VERIFICAÇAO RED & YELLOW LIFE
                if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)):

                    redvida()
                    quase = quase + 1
                    print('O total de quase mortes foi:', quase)
                    sair = 1
                
                #SAI DO LOOP CASO SAIR FOR IGUAL 1
                if sair == 1:
                    break

                #SE TIVER ALGUEM DO LADO (protec player)
                if battleplayer == 55:

                    print('sistema entrou no protec player, a contagem parou em', battleplayer)
                    break


            time.sleep(2)
        
            #PEGA LOOT SHINY
            loot()

            #JOGAR BALL

            #TIRAR CURSOR ATK
            pyautogui.moveTo(700, 100)
            time.sleep(1)

            #BALL 1 ok
            if pyautogui.pixelMatchesColor(600, 236, (247, 253, 17)) or pyautogui.pixelMatchesColor(613, 211, (242, 248, 57)):

                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(636, 243)
                pyautogui.click()


            #ball 3 ok
            if pyautogui.pixelMatchesColor(702, 211, (254, 255, 109)) or pyautogui.pixelMatchesColor(702, 211, (254, 255, 109)) or pyautogui.pixelMatchesColor(730, 216, (174, 226, 247)):
                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(733, 240)
                pyautogui.click()


            #ball 4 ok
            if pyautogui.pixelMatchesColor(696, 269, (247, 253, 17)) or pyautogui.pixelMatchesColor(702, 256, (252, 254, 80)) or pyautogui.pixelMatchesColor(729, 260, (77, 176, 231)):

                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(720, 284)
                pyautogui.click()

            
            #ball 8 ok
            if pyautogui.pixelMatchesColor(614, 280, (240, 246, 15)) or pyautogui.pixelMatchesColor(630, 256, (139, 209, 242)) or pyautogui.pixelMatchesColor(604, 271, (236, 236, 14)):

                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(637, 289)
                pyautogui.click()


            #VOLTA AO INICIO DO CODIGO
            sair = 1


    #VOLTA INICIO CODIGO
    if sair == 1:
        continue
    
    #CHECAGEM CONTINUAR A PESCAR
    while pyautogui.pixelMatchesColor(1183, 531, (7, 9, 12)) == False:

        time.sleep(0.1)

        #CHECA MAGIKARP LADO DIREITO BAIXO
        if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

            break

        #CHECA MAGIKARP LADO DIREITO CIMA
        if pyautogui.pixelMatchesColor(723, 208, (146, 97, 49)):

            break

        #CHECA MAGIKARP LADO ESQUERDO BAIXO
        if pyautogui.pixelMatchesColor(630, 256, (129, 82, 36)):

            break

        #CHECA MAGIKARP LADO ESQUERDO CIMA
        if pyautogui.pixelMatchesColor(628, 208, (155, 107, 59)):

            break

        #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
        if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

            caiunet()
            sair = 1
            break

    #VOLTA INICIO CODIGO
    if sair == 1:

        continue

    #VERIFICAÇAO RED & YELLOW LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)):

        redvida()
        quase = quase + 1
        print('O total de quase mortes foi:', quase)
        continue
    
    #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
    if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

        caiunet()
        continue

