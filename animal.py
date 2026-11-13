from abc import ABC, abstractmethod

# 1. 상위 클래스를 추상 클래스로 선언
class AnimalABC(ABC):
    @abstractmethod
    def speak(self, animalsound):
        pass

class Animal(AnimalABC):
    type = "Animal"
    def __str__(self):
        return self.type    
    def speak(self, animalsound):
        if not isinstance(animalsound, AnimalSound):
            raise ValueError("Invalid sound object")
        return animalsound.sound

class AnimalSound():
    def __init__(self, sound):
        self.sound = sound

class DogSound(AnimalSound):
    def __init__(self):
        super().__init__("Woof!")

class CatSound(AnimalSound):
    def __init__(self):
        super().__init__("Meow!")

class BirdSound(AnimalSound):
    def __init__(self):
        super().__init__("Tweet!")

class Dog(Animal):
    type = "Dog"

class Cat(Animal):
    type = "Cat"

class Bird(Animal):
    type = "Bird"

# 기존 클래스들은 전혀 수정하지 않고 '확장'만 진행
class TigerSound(AnimalSound):
    def __init__(self): super().__init__("Roar!")

class Tiger(Animal):
    type = "Tiger"

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    bird = Bird()

    print(dog)  # Dog
    print(dog.speak(DogSound()))  # Woof!
    print(cat)  # Cat
    print(cat.speak(CatSound()))  # Meow!
    print(bird)  # Bird
    print(bird.speak(BirdSound()))  # Tweet!
        
    # 사용 시점에도 기존 메커니즘 그대로 동작
    tiger = Tiger()
    print(tiger.speak(TigerSound()))  # Roar!