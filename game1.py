import random
from time import sleep
import keyboard

pow = 0
dex = 0
con = 0
int = 0
sab = 0
car = 0
life = 10

v = '\033[1;31m'
a = '\033[1;34m'
l = '\033[m'

def linha():
    print('-='*50)


def classes():
    loop = True
    while loop:
        if keyboard.is_pressed('1'):
            classes.classe = 'guerreiro'
            loop = False
            break
        elif keyboard.is_pressed('2'):
            classes.classe = 'mago'
            loop = False
            break
        elif keyboard.is_pressed('3'):
            classes .classe = 'ladino'
            loop = False
            break       
        elif keyboard.is_pressed('4'):
            classes.classe = 'clérigo'
            loop = False
            break


def escolha(): #escolha de ação
    escolha.act = 0
    loop = True
    while loop:
        if keyboard.is_pressed('1'):
            escolha.act = 1
            loop = False
            break
        else:
            if keyboard.is_pressed('2'):
                escolha.act = 2
                loop = False
                break

      
def d20(scss, atrib):
    d20.sucesso = scss
    d20.d20 = random.randint(1, 20)
    roll = d20.d20 + atrib
    #print(scss, atrib, d20.d20, roll)
      

    if roll <= 5:
        #print('Fracasso crítico!')
        d20.f_crit = True
        d20.fail = True
    elif roll >= 20:
        #print('Sucesso crítico!')
        d20.s_crit = True
        d20.fail = False
    elif roll >= d20.sucesso:
        #print('Sucesso')
        d20.s_crit = False
        d20.fail = False
    else:
        #print('Fracasso')
        d20.f_crit = False
        d20.fail = True

        
def d4(crit):
    d4.d4 = random.randint(1, 4)
    d4.d4_2 = random.randint(1, 4)
    d4.life = life
    if crit == False:
        d4.life -= d4.d4
    else:
        d4.life -= d4.d4 + d4.d4_2


def op(t1, t2):
   op.dec = '| 1-'+ t1 + ' | 2-'+ t2 +' |'
   print(v,op.dec,l)


    


linha()
nome = input('Qual é seu nome, viajante? ').strip()
linha()

print(f'{a}Escolha uma classe:{l} {v}| 1-Guerreiro | 2-Mago | 3-Ladino | 4-Clérigo |{l} ')
linha()

classes()
                
print(f'É um prazer te conhecer {nome}!')
linha()

sleep(1)

if classes.classe.upper() == 'MAGO':
    print('Você escolheu a classe: Mago!')
    pow = 0
    dex = 3
    con = 2
    int = 4
    sab = 4
    car = 1
    life = life + con
if classes.classe.upper() == 'GUERREIRO':
    print('Você escolheu a classe: Guerreiro!')
    pow = 4
    dex = 0
    con = 4
    int = 3
    sab = 1
    car = 2
    life = life + con
if classes.classe.upper() == 'LADINO':
    print('Você escolheu a classe: Ladino!')
    pow = 1
    dex = 4
    con = 0
    int = 3
    sab = 2
    car = 4
    life = life + con
if classes.classe.upper() == 'CLERIGO' or classes.classe.upper() == 'CLÉRIGO':
    print('Você escolheu a classe: Clérigo')
    pow = 0
    dex = 1
    con = 2
    int = 3
    sab = 4
    car = 4
    life = life + con
linha()

sleep(1)

print('Ao adentrar a pirâmide, você nota diversos hierógrifos na parede, o que deseja fazer?')
op('Investigar.', 'Passar direto.')
linha()

escolha()

sleep(1)

if escolha.act == 1:
    print('Os hierógrifos te mostram: Viashinos devorando humanos ainda vivos!')
else:
    print('Você anda até a entrada do corredor.')
linha()

sleep(1)

print('Você vê um longo corredor na sua frente, o que deseja fazer?')
op('Continuar seguindo!', 'Voltar.')
linha()

escolha()

sleep(1)

if escolha.act == 1:
    print('Você segue, vendo ossos humanos espalhados por todo o corredor.')
else:
    print('Game Over!')
linha()

sleep(1)

print('No meio corredor, você avista uma pilha de ossos! o que deseja fazer?')
op('Investigar.', 'Passar direto.')
linha()

escolha()

sleep(1)

if escolha.act == 1:
    d20(10, sab)
    if d20.fail == False:
        investigar_ossos = True
        print('Você analisa a pilha de ossos e descobre uma armadilha logo à frente!')
    else:
        investigar_ossos = False
        print('A pilha de ossos não diz nada a você.')
else:
    print('Você passa direto pela pilha de ossos!')
    investigar_ossos = False
linha() 

sleep(1)
       
print('O que deseja fazer?')
op('Continuar pelo corredor.','Voltar.')     
linha() 

escolha()

if escolha.act == 1:
    if investigar_ossos == True:
        print('Você segue o corredor e não ativa a armadilha!')
    else:
        print('Ao seguir o corredor, você ouve um barulho de pedra se movendo e repentinamente são dispardos dardos das paredes!')
        d20(12, dex)
        if d20.fail == False:
            print('Você consegue desviar de todos os dardos e não sofre nenhum dano!')
        elif d20.f_crit == True:
            d4(d20.f_crit)
            print(f'Você tomou {(d4.d4 + d4.d4_2)} de dano e está agora com {d4.life} de vida')
        else:
            d4(d20.f_crit)
            print(f'Você tomou {d4.d4} de dano e está agora com {d4.life} de vida')                                               
else:
    print(f'{v}Game Over!{l}')             
linha()

sleep(1)

print('Você entra em uma nova câmara da pirâmide, à frente está um corredor e à esquerda tem uma porta. O que deseja fazer?')

op('Seguir em frente.', 'Verificar a porta.')

linha()

escolha()

sleep(1)


if escolha.act == 1:
    pass
else:
    print('Você verificou a porta e descobre uma pequena câmara. O que deseja fazer?')
    op('Seguir em frente.','Entrar na pequena câmara.')
    linha()
    escolha()
    sleep(1)
    if escolha.act == 1:
        pass
    else:
        print('Ao entrar, você se depara com um báu. O que deseja fazer?')
        op('Sair', 'Abrir o báu')
        linha()
        escolha()
        sleep(1)
        if escolha.act == 1:
            print('Você retornou à câmara principal, mas ao sair a pequena câmara desmorona. O que deseja fazer?')
            op('Seguir em frente', 'Voltar')
            linha()
            escolha()
            sleep(1)
            if escolha.act == 1:
                pass
            else:
                print(f'{v}Game Over!{l}')
                linha()
                exit()
        else:
            print('ABRIU O BAU')


print('Você chegou à mais uma câmara!')
linha()
   












input('Gostou do game? ')
