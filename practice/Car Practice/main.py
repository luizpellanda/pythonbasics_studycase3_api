from carro import Carro
from moto import Moto

corsa = Carro('Chevrolet', 'Corsa', 4)
fusca = Carro('Volkswagen', 'Fusca', 2)
civic = Carro('Honda', 'Civic', 4)

harley = Moto('Harley Davidson', 'Road King', 'Cruiser')
cbr = Moto('Honda', 'CBR 600', 'Esportiva')
biz = Moto('Honda', 'Biz', 'Casual')


def main():
    print(corsa)
    print(fusca)
    print(civic)
    print(harley)
    print(cbr)
    print(biz)

if __name__ == '__main__':
    main()