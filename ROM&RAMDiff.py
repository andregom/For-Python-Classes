class MemoriaROM:
    def __init__(self):
        # Dados pré-gravados na memória ROM (não podem ser alterados)
        self.dados = "Dados de inicialização do sistema (firmware)."

    def ler_dados(self):
        # Apenas leitura dos dados da ROM
        return self.dados


class MemoriaRAM:
    def __init__(self):
        # Inicializa a RAM como vazia
        self.dados = ""

    def gravar_dados(self, novos_dados):
        # Gravação de novos dados na RAM
        self.dados = novos_dados

    def ler_dados(self):
        # Leitura dos dados atuais na RAM
        return self.dados

    def limpar_memoria(self):
        # Limpeza dos dados da RAM, simulando perda de dados após desligamento
        self.dados = ""


def main():
    print("Simulação de Memória ROM e RAM")
    
    # Criando instância da Memória ROM
    rom = MemoriaROM()
    print("\nMemória ROM:")
    print("Dados na ROM:", rom.ler_dados())

    # Criando instância da Memória RAM
    ram = MemoriaRAM()
    print("\nMemória RAM antes de gravar dados:")
    print("Dados na RAM:", ram.ler_dados())

    # Gravando dados na RAM
    ram.gravar_dados("Documento temporário, sessão de trabalho.")
    print("\nMemória RAM após gravar dados:")
    print("Dados na RAM:", ram.ler_dados())

    # Limpar a memória RAM (simulando desligamento do sistema)
    ram.limpar_memoria()
    print("\nMemória RAM após desligar o sistema:")
    print("Dados na RAM:", ram.ler_dados())


if __name__ == "__main__":
    main()
