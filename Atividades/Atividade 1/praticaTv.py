class TV:
    def __init__(self, fabricante, modelo, resolucao, polegada):
        self.fabricante = fabricante
        self.modelo = modelo
        self.resolucao = resolucao
        self.polegada = polegada
        self.ligada = False
        self.canal_atual = 1
        self.volume_atual = 15

    def ligar_desligar(self):
        self.ligada = not self.ligada
        if self.ligada:
            print("TV ligada")
        else:
            print("TV desligada")

    def alterar_canal(self, novo_canal):
        if self.ligada:
            self.canal_atual = novo_canal
            print(f"Canal alterado para {novo_canal}")
        else:
            print("A TV está desligada")

    def aumentar_volume(self):
        if self.ligada:
            if self.volume_atual < 100:
                self.volume_atual += 15
                print(f"Volume aumentado para {self.volume_atual}")
            else:
                print("Volume máximo alcançado")
        else:
            print("A TV está desligada")

    def diminuir_volume(self):
        if self.ligada:
            if self.volume_atual > 0:
                self.volume_atual -= 15
                print(f"Volume diminuído para {self.volume_atual}")
            else:
                print("Volume mínimo alcançado")
        else:
            print("A TV está desligada")

    def mute(self):
        if self.ligada:
            self.volume_atual = 0
            print("Mudo ativado!")
        else:
            print("Mudo desativado!")

    def get_info(self):
        print(f"Fabricante: {self.fabricante}")
        print(f"Modelo: {self.modelo}")
        print(f"Resolução: {self.resolucao}")
        print(f"Polegada: {self.polegada}")

        if self.ligada:
            print(f"Canal atual: {self.canal_atual}")
            print(f"Volume atual: {self.volume_atual}")



minha_tv = TV(fabricante= "Samsung", modelo= "SmartTV", resolucao= "4K", polegada= 32)

minha_tv.ligar_desligar()
minha_tv.alterar_canal(5)
minha_tv.aumentar_volume()
minha_tv.diminuir_volume()
minha_tv.get_info()
minha_tv.mute()

