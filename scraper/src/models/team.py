class Team:
    def __init__(self) -> None:
        self.id = ''
        self.name = ''
        self.players = []

    def __str__(self) -> str:
        return f"({self.id}) {self.name}, Player Count: {len(self.players)}"