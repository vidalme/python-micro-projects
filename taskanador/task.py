class Task:
    def __init__(self, id: int, title: str, status: str = "pending"):
        
        # controlados pela classe que agrupa tasks
        self.id = id
        self.title = title
        
        # controlado internamente
        self.status = status

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.title}, {self.status})"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
        }