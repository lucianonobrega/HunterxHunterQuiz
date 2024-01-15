from time import sleep
from random import choice

class Quiz():
    def __init__(self):
        self.alternativas = ["a","b","c","d","e","f"]
        self.dicionario = {"Reforço":0, "Transmutação":0, "Conjuração":0, "Manipulação":0, "Emissão":0, "Especialização":0}
        self.tipo_nen = ""

    def apresentacao(self):
        print("-" * 24)
        print("| Hunter x Hunter Quiz |")
        print("-" * 24)

    def opcao_invalida(self):
        print("Opção inválida.\nPor favor, tente novamente.")

    def pergunta_1(self):
        try:
            while True:
                pergunta = str(input("1)Qual das qualidades abaixo você considera estar mais presente na sua personalidade?\n"
                                     "a)Esperto.\nb)Paciente.\nc)Resiliente.\nd)Racional.\ne)Determinado.\nf)Independente.\nResposta: ")).lower()
                if pergunta in self.alternativas:
                    if pergunta == "a":
                        self.dicionario["Reforço"] += 1
                    elif pergunta == "b":
                        self.dicionario["Transmutação"] += 1
                    elif pergunta == "c":
                        self.dicionario["Conjuração"] += 1
                    elif pergunta == "d":
                        self.dicionario["Manipulação"] += 1
                    elif pergunta == "e":
                        self.dicionario["Emissão"] += 1
                    elif pergunta == "f":
                        self.dicionario["Especialização"] += 1
                    print("\n")
                    break
                else:
                    self.opcao_invalida()
                    sleep(2)
        except:
            print("Ocorreu um erro inesperado.\nPor favor, tente novamente.")
            sleep(2)

    def pergunta_2(self):
        try:
            while True:
                pergunta = str(input("2)Das opções abaixo, qual você considera estar mais próxima de um defeito seu?\n"
                                     "a)Teimoso.\nb)Mentiroso.\nc)Impulsivo.\nd)Indiferente.\ne)Nervoso.\nf)Egoísta.\nResposta: ")).lower()
                if pergunta in self.alternativas:
                    if pergunta == "a":
                        self.dicionario["Reforço"] += 1
                    elif pergunta == "b":
                        self.dicionario["Transmutação"] += 1
                    elif pergunta == "c":
                        self.dicionario["Conjuração"] += 1
                    elif pergunta == "d":
                        self.dicionario["Manipulação"] += 1
                    elif pergunta == "e":
                        self.dicionario["Emissão"] += 1
                    elif pergunta == "f":
                        self.dicionario["Especialização"] += 1
                    print("\n")
                    break
                else:
                    self.opcao_invalida()
                    sleep(2)
        except:
            print("Ocorreu um erro inesperado.\nPor favor, tente novamente.")
            sleep(2)

    def pergunta_3(self):
        try:
            while True:
                pergunta = str(input("3)Como você acha que seus amigos te enxergam?\na)Muito Sincero e Direto.\nb)Pavio curto, mas de bom coração.\n"
                                     "c)Cuidadoso e Observador.\nd)Muito malandro e esperto.\ne)Protetor e Racional.\nf)Carismático e Inteligente.\n"
                                     "Resposta: ")).lower()
                if pergunta in self.alternativas:
                    if pergunta == "a":
                        self.dicionario["Reforço"] += 1
                    elif pergunta == "b":
                        self.dicionario["Transmutação"] += 1
                    elif pergunta == "c":
                        self.dicionario["Conjuração"] += 1
                    elif pergunta == "d":
                        self.dicionario["Manipulação"] += 1
                    elif pergunta == "e":
                        self.dicionario["Emissão"] += 1
                    elif pergunta == "f":
                        self.dicionario["Especialização"] += 1
                    print("\n")
                    break
                else:
                    self.opcao_invalida()
                    sleep(2)
        except:
            print("Ocorreu um erro inesperado.\nPor favor, tente novamente.")
            sleep(2)

    def pergunta_4(self):
        try:
            while True:
                pergunta = str(input("4)Que tipo de pessoa te irrita profundamente?\na)Muito emocionais.\nb)Desrespeitosas.\nc)Invasivas.\nd)Debochadas."
                                     "\ne)Certinhas demais.\nf)Mentirosas.\nResposta: ")).lower()
                if pergunta in self.alternativas:
                    if pergunta == "a":
                        self.dicionario["Reforço"] += 1
                    elif pergunta == "b":
                        self.dicionario["Transmutação"] += 1
                    elif pergunta == "c":
                        self.dicionario["Conjuração"] += 1
                    elif pergunta == "d":
                        self.dicionario["Manipulação"] += 1
                    elif pergunta == "e":
                        self.dicionario["Emissão"] += 1
                    elif pergunta == "f":
                        self.dicionario["Especialização"] += 1
                    print("\n")
                    break
                else:
                    self.opcao_invalida()
                    sleep(2)
        except:
            print("Ocorreu um erro inesperado.\nPor favor, tente novamente.")
            sleep(2)

    def pergunta_5(self):
        try:
            while True:
                pergunta = str(input("5)Como você gosta de se divertir ou relaxar?\na)Atividades físicas e animadas.\nb)Transitar de atividades.\nc)Atividades sozinho e pensativas.\n"
                             "d)Atividades básicas e na rotina.\ne)Atividades em grupo.\nf)Estimular a inteligência ou criatividade.\n"
                             "Resposta: ")).lower()
                if pergunta in self.alternativas:
                    if pergunta == "a":
                        self.dicionario["Reforço"] += 1
                    elif pergunta == "b":
                        self.dicionario["Transmutação"] += 1
                    elif pergunta == "c":
                        self.dicionario["Conjuração"] += 1
                    elif pergunta == "d":
                        self.dicionario["Manipulação"] += 1
                    elif pergunta == "e":
                        self.dicionario["Emissão"] += 1
                    elif pergunta == "f":
                        self.dicionario["Especialização"] += 1
                    print("\n")
                    break
                else:
                    self.opcao_invalida()
                    sleep(2)
        except:
            print("Ocorreu um erro inesperado.\nPor favor, tente novamente.")
            sleep(2)

    def pergunta_6(self):
        try:
            while True:
                pergunta = str(input("6)Você se considera uma pessoa que age mais pela:\na)Razão.\nb)Emoção.\nResposta: ")).lower()
                if pergunta in self.alternativas:
                    if pergunta == "a":
                        self.dicionario["Reforço"] += 1
                        self.dicionario["Emissão"] += 1
                        self.dicionario["Conjuração"] += 1
                    elif pergunta == "b":
                        self.dicionario["Transmutação"] += 1
                        self.dicionario["Manipulação"] += 1
                        self.dicionario["Especialização"] += 1
                    print("\n")
                    break
                else:
                    self.opcao_invalida()
                    sleep(2)
        except:
            print("Ocorreu um erro inesperado.\nPor favor, tente novamente.")
            sleep(2)

    def pergunta_7(self):
        try:
            while True:
                pergunta = str(input("7)Como você gosta de lidar com os problemas que aparecem?\n"
                                     "a)Tenta solucionar da melhor forma que consegue, porém quanto mais pessoal for o problema, mais drástica é a solução.\n"
                                     "b)Verifica qual a forma mais simples de chegar na solução, para não ter confusão durante o processo.\n"
                                     "c)Se isola mentalmente para pensar melhor, evitar pedir muitas ajudas e ser influenciado na decisão.\n"
                                     "d)Só resolve o problema se ele realmente valer a pena, se não, tende a ignorar o problema.\n"
                                     "e)Procura ajuda e opiniões sobre os problemas para tomar a melhor decisão.\n"
                                     "f)Analisa todos os prováveis eventos para solucionar o problema e tenta encontrar a melhor forma de resolver.\n"
                                     "Resposta: ")).lower()
                if pergunta in self.alternativas:
                    if pergunta == "a":
                        self.dicionario["Reforço"] += 1
                    elif pergunta == "b":
                        self.dicionario["Transmutação"] += 1
                    elif pergunta == "c":
                        self.dicionario["Conjuração"] += 1
                    elif pergunta == "d":
                        self.dicionario["Manipulação"] += 1
                    elif pergunta == "e":
                        self.dicionario["Emissão"] += 1
                    elif pergunta == "f":
                        self.dicionario["Especialização"] += 1
                    print("\n")
                    break
                else:
                    self.opcao_invalida()
                    sleep(2)
        except:
            print("Ocorreu um erro inesperado.\nPor favor, tente novamente.")
            sleep(2)

    def pergunta_8(self):
        try:
            while True:
                pergunta = str(input("8)Qual dessas frases mais te representa?\na)Desistência não está na minha rotina.\nb)Meu espaço pessoal é algo essencial em minha vida.\n"
                                     "c)Todos tem seu próprio tempo de aprendizagem.\nd)Eu nunca me contento com uma coisa só.\ne)Não espere a vitória vir até você.\n"
                                     "f)Esteja sempre três passos a frente.\nResposta: ")).lower()
                if pergunta in self.alternativas:
                    if pergunta == "a":
                        self.dicionario["Reforço"] += 1
                    elif pergunta == "b":
                        self.dicionario["Transmutação"] += 1
                    elif pergunta == "c":
                        self.dicionario["Conjuração"] += 1
                    elif pergunta == "d":
                        self.dicionario["Manipulação"] += 1
                    elif pergunta == "e":
                        self.dicionario["Emissão"] += 1
                    elif pergunta == "f":
                        self.dicionario["Especialização"] += 1
                    print("\n")
                    break
                else:
                    self.opcao_invalida()
                    sleep(2)
        except:
            print("Ocorreu um erro inesperado.\nPor favor, tente novamente.")
            sleep(2)

    def analisando_respostas(self):
        print("Analisando...")
        resultado = max(self.dicionario, key=self.dicionario.get)
        sleep(3)
        self.tipo_nen = resultado
        print(f"* O seu tipo Nen[念] é: {resultado} *")

    def cor_nen(self):
        lista_cores = ["Azul","Vermelho","Amarelo","Verde","Laranja","Roxo"]
        cor = choice(lista_cores)
        print(f"* A cor da sua aura é: {cor} *")

    def tipos_nen_explicacao(self):
        if self.tipo_nen == "Reforço":
            print("Usuários de Reforço buscam fortalecer seus corpos ou objetos, ampliando suas capacidades físicas ou durabilidade. Isso pode incluir aumento de força, resistência e velocidade.")
        elif self.tipo_nen == "Emissão":
            print("Emissão envolve a capacidade de separar a aura do corpo e usá-la independentemente. Isso permite a criação de ataques à distância, como projéteis de Nen.")
        elif self.tipo_nen == "Manipulação":
            print("Usuários de Manipulação têm a capacidade de controlar objetos ou seres vivos de acordo com sua vontade, assumindo temporariamente o controle sobre eles. Isso pode variar de manipular marionetes a controlar mentes.")
        elif self.tipo_nen == "Conjuração":
            print("Conjuração envolve a materialização de objetos a partir da aura. Os usuários desse tipo de Nen podem criar armas, ferramentas ou até mesmo seres conjurados com habilidades específicas.")
        elif self.tipo_nen == "Transmutação":
            print("Usuários de Transmutação alteram as propriedades da aura para imitar as características de substâncias existentes. Isso permite transformar a aura em algo diferente, como torná-la elástica como borracha, afiada como metal, etc.")
        elif self.tipo_nen == "Especialização":
            print("A Especialização é um tipo de Nen mais raro e aberto, sem uma regra específica. Geralmente, envolve habilidades únicas e personalizadas que não se encaixam completamente nos outros tipos mencionados.")

    def sair(self):
        encerrar = str(input("Aperte 'ENTER' para sair do programa."))
        if encerrar:
            exit()

quiz = Quiz()
if __name__ == "__main__":
    quiz.apresentacao()
    quiz.pergunta_1()
    quiz.pergunta_2()
    quiz.pergunta_3()
    quiz.pergunta_4()
    quiz.pergunta_5()
    quiz.pergunta_6()
    quiz.pergunta_7()
    quiz.pergunta_8()
    quiz.analisando_respostas()
    sleep(2)
    quiz.cor_nen()
    sleep(2)
    quiz.tipos_nen_explicacao()
    sleep(5)
    quiz.sair()