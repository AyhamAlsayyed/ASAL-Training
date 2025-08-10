from animal import Animal

class Cat(Animal):
    def speak(self):
        print(f"{self.name} Meow")

    def rename(self, new_name):
        return super().rename(new_name)
