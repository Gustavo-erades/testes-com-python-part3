def temperatura():
    print("* *********** *")
    print("* TEMPERATURA *")
    print("* *********** *")
    F=float(input("Informe a temperatura em graus Fahrenheit: "))
    C=float(5*(F-32)/9)
    print("{:.2f}".format(F),"em gruas fahrenheit é {:.2f} graus Celsius".format(C))
    print("* ************* *")
    print("* TEMPERATURA_2 *")
    print("* ************* *")
    C=float(input("Informe a temperatura em graus Celsius: "))
    F=float((9*C)/5+32)
    print("{:.2f}".format(C),"em gruas Celsius é {:.2f} graus Fahrenheit".format(F))

def imc():
    print("* *********** *")
    print("*    I.M.C    *")
    print("* *********** *")
    resp=int(input("Homem --> 1 \nMulher --> 2\nResposta: "))
    if resp==1:
        height=float(input("Informe sua altura: "))
        peso_ideal=(72.7*height)-58
        print("Seu peso ideal é: {:.2f}".format(peso_ideal))
    elif resp==2:
        height = float(input("Informe sua altura: "))
        peso_ideal = (62.1 * height) - 44.7
        print("Seu peso ideal é: {:.2f}".format(peso_ideal))
    else:
        print("opção inválida!")

def sal_liquid():
    print("* *********** *")
    print("* SAL LIQUID  *")
    print("* *********** *")
    val_hora=float(input("Valor ganho por hora trabalhada: "))
    quant_hora=float(input("Quantidade de horas trabalhadas: "))
    sal_bruto=float(val_hora*quant_hora)
    IR=sal_bruto*0.11
    INSS=sal_bruto*0.08
    SINDICATO=sal_bruto*0.05
    total_desc= IR+INSS+SINDICATO
    sal_liq=float(sal_bruto-total_desc)
    print("\n+ SALÁRIO BRUTO : R${:.2f}\n".format(sal_bruto))
    print("- IR : R${:.2f}\n".format(IR))
    print("- INSS : R${:.2f}\n".format(INSS))
    print("- SINDICATO : R${:.2f}\n".format(SINDICATO))
    print("= SALÁRIO LIQUIDO : R${:.2f}".format(sal_liq))

def vel():
    print("* ************ *")
    print("*     UPLOAD   *")
    print("* ************ *")
    tam=float(input("informe o tamanho do arquivo em MB: "))
    vel=float(input("informe a velocidade da internet em Mbps: "))
    temp=float(tam/vel)/60
    print("o arquivo será baixado em aproximadamente {:.2f} minutos".format(temp))

def pintura():
    tam=float(input("Informe o tamanho em metros quadrados a ser pintado: "))
    quant_latas= int(tam/108)
    val_latas=float(quant_latas*80)
    dis_lata=float(tam-(quant_latas*108))
    if(dis_lata>=1):
        quant_latas_2= int(dis_lata/108)
        if(quant_latas_2<=1):
            total_latas= quant_latas+1
            val_latas_2 = float(total_latas * 80)
            print("será necessário {} latas".format(total_latas), "e custará R$ {:.2f}".format(val_latas_2))
        else:
            total_latas= quant_latas+quant_latas_2
            val_latas_2 = float(total_latas * 80)
            print("será necessário {} latas".format(total_latas), "e custará R$ {:.2f}".format(val_latas_2))
    if(dis_lata<1):
        print("será necessário {} latas".format(quant_latas),"e custará R$ {:.2f}".format(val_latas))

    quant_gal=int(tam/21.6)
    val_gal=float(quant_gal*25)
    dis_gal=float(tam-(quant_gal*21.6))
    if(dis_gal>=1):
        quant_gal_2= int(dis_gal/21.6)
        if(quant_gal_2<=1):
            total_gal= quant_gal+1
            val_gal_2 = float(total_gal * 25)
            print("será necessário {} galões".format(total_gal), "e custará R$ {:.2f}".format(val_gal_2))
        else:
            total_gal= quant_gal+quant_gal_2
            val_gal_2 = float(total_gal * 25)
            print("será necessário {} galões".format(total_gal), "e custará R$ {:.2f}".format(val_gal_2))
    if(dis_gal<1):
        print("será necessário {} galões".format(quant_gal),"e custará R$ {:.2f}".format(val_gal))

    num_latas=int(tam/108)
    val_num_latas=float(num_latas*80)
    div_num_gal=int(tam%108)
    if num_latas<1:
        num_gal=int(tam/21.6)
    else:
        num_gal = int(div_num_gal / 21.6)
    val_num_gal=float(num_gal*25)
    val_total_mist=float(val_num_gal+val_num_latas)
    dis_mist=int(tam-((num_latas*108)+(num_gal*21.6)))
    while dis_mist>0 and dis_mist<108:
        num_gal=num_gal+1
        val_total_mist=val_total_mist+25
        break
    while dis_mist>108:
        num_latas=num_latas+1
        break
    print("Será necessário {} latas".format(num_latas),"e {} galões".format(num_gal),"e custará {:.2f}".format(val_total_mist))

def menu(): 
    print("************************************")
    print("* 1 --> temperatura                *")
    print("* 2 --> clcular imc                *")
    print("* 3 --> salário líquido            *")
    print("* 4 -->   velocidade de upload     *")
    print("* 5 --> alternativas para pintura  *")
    print("* 6 -->       sair                 *")
    print("************************************\n")
    num=int(input("Opção desejada: "))
    if num==1:
        temperatura()
    elif num==2:
        imc()
    elif num==3:
        sal_liquid()
    elif num==4:
        vel()
    elif num==5:
        pintura()
    elif num==6: 
        print("FIM.")
    elif num!=1 and 2 and 3 and 4 and 5 and 6:
        print("Escolha uma opção válida\n")
        menu()
menu()

