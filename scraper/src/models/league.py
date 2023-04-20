class League:
    def __init__(self) -> None:
        self.teams = []

    def __str__(self) -> str:
        return f"League; Team Count: {len(self.teams)}"