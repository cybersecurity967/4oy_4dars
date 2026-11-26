class Coach:
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport


class Athlete:
    def __init__(self, name, age, coach):
        self.name = name
        self.age = age
        self.coach = coach

    def info(self):
        return f"{self.name} ({self.age}) - {self.coach.name} ({self.coach.sport})"


coach1 = Coach("Boltavoy Teshayev", "Boxing")
coach2 = Coach("Qo'ndiddin falonchiyev", "Swimming")

athlete1 = Athlete("Ali Valiyev", 20, coach1)
athlete2 = Athlete("Alisher ", 18, coach1)
athlete3 = Athlete("Toshmat", 17, coach2)
athlete4 = Athlete("Fazullo", 19, coach2)

athletes = [athlete1, athlete2, athlete3, athlete4]

with open("info.txt", "w", encoding="utf-8") as file:
    for athlete in athletes:
        line = athlete.info()
        print(line)             
        print(line, file=file)  