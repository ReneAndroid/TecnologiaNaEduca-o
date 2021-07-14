from turtle import *
import turtle
pen = turtle.Pen()
import math
from math import sqrt
#biblioteca importadas
x="s"

while x =="s":
    speed(100)
    shape("turtle")
    print ("──────▄▄▄▄▄███████████████████▄▄▄▄▄──────")
    print("────▄██████████▀▀▀▀▀▀▀▀▀▀██████▀████▄────")
    print("──▄██▀████████▄─────────────▀▀████─▀██▄──")
    print("─▀██▄▄██████████████████▄▄▄─────────▄██▀─")
    print("───▀█████████████████████████▄────▄██▀───")
    print("─────▀████▀▀▀▀▀▀▀▀▀▀▀▀█████████▄▄██▀─────")
    print("───────▀███▄──────────────▀██████▀───────")
    print("─────────▀██████▄─────────▄████▀─────────")
    print("────────────▀█████▄▄▄▄▄▄▄███▀────────────")
    print("──────────────▀████▀▀▀████▀──────────────")
    print("────────────────▀███▄███▀────────────────")
    print("───────────────────▀█▀───────────────────")
    print ("────────────────GEOMETRY────────────────── ")
    print ("────────────────GEOMETRY────────────────── ")
    print ("────────────────GEOMETRY────────────────── ")
    print (" ───ALUNO:RENE JOSE ANDRADE DE LIMA")
    print ("****************************************************************************************************************************************** ")
    print ("──────────────────────────Quantos lados têm sua fígura geométrica [3][4] ou digite a tecla [1] para uma circuferência ou digite 0 para ver curiosidade do programa. ?────────────────────────── ")
    print (" ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────  ")
    print ("****************************************************************************************************************************************** ")
    figura8L=float(input())
    if (figura8L!=1 and figura8L!=3 and figura8L!=4 and figura8L!=0):
        print ("Sua fígura não possui lado suficiente ou não existe,por favor escolha uma fígura válida.Deseja tentar novamente? ´s´ para SIM e ´n´para NÃO")
        x=input()
    if(figura8L==0):
        print ("FIM DO PROGRAMA")
        print (" Nº total de linhas = 314")
        print (" Nº total de palavras=898")
        print (" Nº total de caracteres 12266")
        print ("você viu a curiosidade como foi feito o programa,Deseja voltar ao menu anterior novamente? ´s´ para SIM e ´n´para NÃO")
        x=input()

    
    if (figura8L==1):
            pen = turtle.Pen()
            pensize(10)
            color ("blue")
            pen.circle(100)

            print ("Você escolheu a circuferencia")
            print ("Formula da área")

            print("π é um número irracional e tem valor aproximadamente 3,14\n")
            print ("O diâmetro é o comprimento da reta que passa pelo centro e toca dois pontos na borda do círculo.\n ")

            
            print("O raio é a metade do diâmetro de uma circunferência. Pode ser definido também como a distância do centro a um ponto qualquer da circunferência.\n")   
            
            print ("A = π·r²")

            print ("Formula do perímetro") 

            print ("C = 2 * π * r")

            
            print ("*** ──────────── ***")
            print ("***Dígite o valor do diâmetro: ***")
            print ("***──────────── ***")
            
            vDiametro= float (input())
            raio=  vDiametro*0.5
            print ("O valor do raio é = ",raio)
            resultadoCir=raio*math.pi
            resultadoPE=2*raio*math.pi
            print ("O valor da área da circuferência é         = " ,resultadoCir)
            print ("O valor do perímetro da circuferência é = " , resultadoPE)
        
           
           
    

    if (figura8L==4):

            print ("Você escolheu um PARALELOGRAMO")
            print ("Paralelogramo é quadrilátero cujos lados opostos são paralelos.")


            for count in range(1):
                color ("red")
                fillcolor ("blue")
                print ("Dígite o tamanho do perímeiro lado horizontal " )
                Qlado1=float (input ())
                print ("Dígite o tamanho do segundo lado vertícal " )
                Qlado2=float (input ())
                pensize(10)
                forward(150)
                if (Qlado1 == Qlado2):
                

                    print ("Você deseja criar um losango ou um quadrado,pois ambos lados são iguais. Digite [1] para quadrado e [2] para losango")
    
                    n1=float (input ())
                    if(n1!=1 and n1!=2):
                        print ("Erro grave no sistema,os números são entre 1 e 2 ,quer tentar novamente 's' para SIM ou 'n' para Não [S/N]")
                        x=input ()

                    if (n1==1):
                        print ("-------------------Você escolheu quadrado---------------------")
                        print("quadrado é a figura geometrica que tem os lados e os ângulos iguais")
                        right (90)
                        forward(150)
                        right (90)
                        forward(150)
                        right (90)
                        forward(150)
                        AreaQuadrado=Qlado1**Qlado1
                        PerimetroQuadrado=Qlado1*Qlado1*Qlado1*Qlado1
                        print (" À área do quadrado é =  " , AreaQuadrado)
                        print (" Perímetro do quadrado é = " , PerimetroQuadrado)
                        
                        
                    if(n1==2):
                        print("-------------------Você escolheu o losango------------------")
                        print("O losango é um quadrilátero plano cujos lados são iguais.")
                        left(120)
                        forward(150)
                        left(120)
                        forward(150)
                        right(120)
                        forward(150)
                        right(120)
                        forward(150)
                        perimetroLosango=Qlado1*4
                        print ("Dígite a medida da diagonal maior " )
                        diagonalMaior=float (input ())
                 
                        print ("Dígite a medida da diagonal menor " )
                        diagonalMenor=float (input ())
                        if diagonalMaior>=diagonalMenor:    

                            print ("A= D . d" )
                            print ("────")
                            print ("      2")
                        
                            AreaLosango=(diagonalMaior*diagonalMenor)/2

                            print ("À área do Losango é =" , AreaLosango)
                            print ("Perímetro", perimetroLosango)
                            done()
                            
                        if diagonalMaior<diagonalMenor:
                                    print ("Erro grave no sistema,você dígitou a diagonal maior menor do que a diagonal  menor,quer tentar novamente 's' para SIM ou 'n' para Não [S/N]")
                                    x=input ()

         
            if(Qlado1!=Qlado2):
                    print ("Os lados são diferentes,você pode escolher entre o  [1] retangulo e [2] trapézio")
                    n2=float (input())
                    
                    


                    if (n2==1):
                        print ("Você escolheu um PARALELOGRAMO-RETANGULO")
                        print ("----------------------Você escolheu retangulo--------------------------")
                        print("O retângulo é uma figura geométrica plana composta por quatro lados e ângulos internos congruentes e retos. Juntamente com o quadrado e losango,")
                        print("essa figura também é considerada um paralelogramo – polígonos com lados opostos paralelos.")
                        forward (100)
                        right (90)
                        forward(40)
                        right (90)
                        forward (250)
                        right (90)
                        forward(40)
                        areaRetangulo=Qlado1*Qlado2
                        perimetroRetangulo=(2*Qlado1 )+ (2*Qlado2)

                        print ("À area do retangulo é =" , areaRetangulo)
                        print ("O perimetro  do retangulo é =" , perimetroRetangulo)
                    
                    if(n2==2):
                        left (120)
                        forward (150)
                        left(60)
                        forward(150)
                        left(60)
                        forward(150)
                        left(120)
                        forward(150)

                        print ("------------------Você escolheu trapézio----------------------------")
                        print("Trapézio é uma figura geométrica plana pertencente ao grupo dos quadriláteros que possui um par de lados paralelos: ... Os lados paralelos dos trapézios são chamados de bases.")
                        print ("A base que possui maior medida recebe o nome de base maior e a que possui menor medida recebe o nome de base menor.")
                        print ("À base maior do trapézio mede " ,Qlado1, " a altura mede " ,Qlado2,)
                        print ("Dígite o numero da base menor para o trapézio")
                        bTrapezio=float (input())

                        if (bTrapezio<Qlado1):
             
                                        
                            print ("A =      h.(B+ b) ")
                            print ("        _________")
                            print ("                2       " )
                            resultadoTrapezio=(((Qlado1+bTrapezio)*Qlado2 )/2)
                            print ("O resultado é "  ,resultadoTrapezio)
                            print ("Deseja continuar  s para SIM e n para Não?" )
                            x=input ()
                      

                                       

                        if (bTrapezio>Qlado1) :
                            print("Valor do trapézio é invalido!!")
                            print ("Deseja continuar ?" )
                            x=input ()
                        
                
                    
               






    if (figura8L==3):

       
                print (" ----------------------------- Sua figura é um TRIÂNGULO---------------------------------")
                color ("green")
                fillcolor("black")
                print ("***Dígite o tamanho do primeiro lado*** " )
                LadoUm=float (input ())
                pensize(10)
                forward(150)
                print ("***Dígite o tamanho do cateto*** " )
                LadoDois=float (input ())
     
            

                if LadoDois>LadoUm:  
                    left(90)
                    forward(200)
                    left(142)
                    forward(250)
                    print (" ---------Triângulo escaleno----------------")
                    print ("***Descobrir a altura por teorema de pitáguras****")
                    print ("                A² + B² = C²")
                    print ("onde A² é hipotenusa, B² é o cateto oposto, C² é cateto adjacente a hipotenusa")
                    print   (LadoUm,"² +" "B²="  ,LadoDois,"² ")
                    resultado1=LadoUm**2
                    resultado2=LadoDois**2
                    print (resultado1, " + B² = ",resultado2)
                    print ("                      B² = ",resultado2, "-",resultado1)
                    resultado3=resultado2-resultado1
                    print ("√",resultado3)
                    resultado4=resultado3**(1/2)
                    print ("O resultado do teorema de pitáguras é  = " , resultado4)
       


                    print ("A =      (h . b) ")
                    print ("        _________")
                    print ("            2       " )
                    AreaDoTriangulo1=(LadoUm*resultado4)/2
                    PerimetroTriangulo1=LadoDois*LadoUm*LadoDois
                    print ("À area do triângulo é igual a " ,  AreaDoTriangulo1)
                    print ("O perimetro do triângulo é igual a " ,  PerimetroTriangulo1)
                    print ("Perímetro: soma das medidas de todos lados de uma figura. Geralmente, para encontrar a área de uma figura basta multiplicar a base (b) pela altura (h). Já o perímetro é a soma dos segmentos de retas que formam a figura, chamados de lados (l).")
                    print(" Área ou superfície de uma figura plana tem a ver com o conceito (primitivo) de sua extensão (bidimensional). Usamos a área do quadrado de lado unitário como referência de unidade de área, chamando de metro quadrado (m²) sua unidade de medida principal.")
                    

        
                if LadoDois<LadoUm:
                    forward(7)
                    left(110)
                    forward(250)
                    left(143)
                    forward(245)
                    AreaDoTriangulo2=(LadoUm*LadoDois)/2
                    PerimetroTriangulo2=LadoDois*LadoUm*LadoDois
                   


            
                    print (" ---------Triângulo Isósceles----------------")
                    print ("A =      (h . b) ")
                    print ("        _________")
                    print ("            2       " )
                    print ("onde h é a altura do triangulo e b a base do triangulo")
                    print ("A area do triangulo é igual a " ,  AreaDoTriangulo2)
                    print ("O perimetro do triangulo é igual a " ,  PerimetroTriangulo2)
                    print ("Perímetro: soma das medidas de todos lados de uma figura. Geralmente, para encontrar a área de uma figura basta multiplicar a base (b) pela altura (h). Já o perímetro é a soma dos segmentos de retas que formam a figura, chamados de lados (l).")
                    print(" Área ou superfície de uma figura plana tem a ver com o conceito (primitivo) de sua extensão (bidimensional). Usamos a área do quadrado de lado unitário como referência de unidade de área, chamando de metro quadrado (m²) sua unidade de medida principal.")
                    
                if LadoDois==LadoUm:
                        left(120)
                        forward(150)
                        left(120)
                        forward(150)

                        print (" ---------Triângulo Equilátero----------------")
                        AreaDoTriangulo3=(LadoUm*LadoDois)/2
                        PerimetroTriangulo3=LadoDois*LadoUm*LadoDois
                        print ("A =      (h . b) ")
                        print ("        _________")
                        print ("            2       " )
                        print ("onde h é a altura do triangulo e b a base do triangulo")
                        print ("À area do triangulo é igual a " ,  AreaDoTriangulo3)
                        print ("À area do triangulo é igual a " ,  PerimetroTriangulo3)
                        print ("Perímetro: soma das medidas de todos lados de uma figura. Geralmente, para encontrar a área de uma figura basta multiplicar a base (b) pela altura (h). Já o perímetro é a soma dos segmentos de retas que formam a figura, chamados de lados (l).")
                        print(" Área ou superfície de uma figura plana tem a ver com o conceito (primitivo) de sua extensão (bidimensional). Usamos a área do quadrado de lado unitário como referência de unidade de área, chamando de metro quadrado (m²) sua unidade de medida principal.")


                        



        
        
    
        
                    

   


                        








        



