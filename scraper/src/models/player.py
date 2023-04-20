class Player:
    def __init__(self) -> None:
        self.id = ''
        self.name = ''
        self.shirt_number = 0
        self.position = ''
        self.nationality = ''
        self.club = ''
        self.age = 0

    def __str__(self):
        return f"({self.id}) {self.name} ({self.shirt_number}), Age: {self.age}, Club: {self.club}, Position: {self.position}, Nationality: {self.nationality} "