class Coach:
    def __init__(self,name , sport):
        self.name = name
        self.sport = sport

    def info(self):
        print (f"{self.name} - {self.sport}")


class Sportsmen:
    def __init__(self, name , age, coach: Coach):
        self.name = name 
        self.age = age
        self.coach = coach

    def infos(self):
        text = f"{self.name} ({self.age}) - {self.coach.name} ({self.coach.sport})"
        print(text)
        with open("infos.txt", "w", encoding="utf-8") as file:
            file.write(text)
        


s1 = Coach("Pep Guardiola" , "Football")

c1 = Sportsmen("Mbappe", 25, s1)

s1.info()

c1.infos()