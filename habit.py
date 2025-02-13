class Habit:
    def __init__(self, name, description, unique_id):
        self.name = name
        self.description = description
        self.id = unique_id
        self.times_checked = 0

    def check(self):
        self.times_checked += 1
        
    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nStreak: {self.times_checked}\n"
    
    def to_table_row(self):
        return f"| {self.name:16} | {self.description:24} | {self.id:10} | {self.times_checked:6} |"
    
    def to_csv(self):
        pass
