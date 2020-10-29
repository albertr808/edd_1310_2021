class Array:
    def __init__(self, tam):
        self.__info=[0 for x in range(tam)]

    def get_item(sel , posicion):
        dato=-1
        try:
            dato=self.__info[posicion]
        except Exception as e:
            print("error de posicion")
            dato="error"
        return dato


    def set__item(self , dato , posicion):
        try:
            self.__info[posicion]= dato
        except Exception as e:
                print("error de posicion")

    def get_lenght (self):
        return len (self.info)

    def clear(self, dato):
        self.info=[dato for x in range(len(self.__info))]

    def __iter__(self):
        return self _IteradorArreglo(self.__info)

class _IteradorArreglo:
    def __init__(self , arr):
        self.__arr= arr
        self.__indice=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice < len(self.arr):
            dato= self.__arr[self.__indice]
            self.__indice +=1
            return dato
        else:
            raise StopIteration



algo= Array(10)
print(algo.get_item(6363))
algo.set_item(555,3)
print(algo.get_item(3))

print(f"el arreglo tiene {algo.get_length()} elementos")
algo.clear(777)
print("____")
for x in algo:
    print(x)
print("----prueba de iterador----")
for x in range(algo.getlength()):
    print(f"{x}-> {algo.get_item(x)}")
