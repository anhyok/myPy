from abc import ABC, abstractmethod
from dataclasses import dataclass

# [개선 3] 도메인 전용 명확한 예외 정의
class InvalidSoundTypeError(TypeError):
    def __init__(self, given_obj):
        super().__init__(f"Expected AnimalSound instance, but got {type(given_obj).__name__}")

# [개선 2] 상위 사운드 클래스를 불변 데이터 클래스로 선언
@dataclass(frozen=True)
class AnimalSound:
    sound: str

# 하위 사운드 클래스들도 안전하게 상속 및 불변 유지
class DogSound(AnimalSound):
    def __init__(self): super().__init__("Woof!")

class CatSound(AnimalSound):
    def __init__(self): super().__init__("Meow!")

class BirdSound(AnimalSound):
    def __init__(self): super().__init__("Tweet!")

# [개선 1] 추상 클래스에 명확한 타입 계약서 작성
class AnimalABC(ABC):
    @abstractmethod
    def speak(self, animalsound: AnimalSound) -> str:
        pass


class Animal(AnimalABC):
    type: str = "Animal"

    def __str__(self) -> str:
        return self.type    

    def speak(self, animalsound: AnimalSound) -> str:
        # 런타임 타입 가드 + 커스텀 예외 처리
        if not isinstance(animalsound, AnimalSound):
            raise InvalidSoundTypeError(animalsound)
        return animalsound.sound


class Dog(Animal): type = "Dog"
class Cat(Animal): type = "Cat"
class Bird(Animal): type = "Bird"



# 기존 클래스들은 전혀 수정하지 않고 '확장'만 진행
class TigerSound(AnimalSound):
    def __init__(self): super().__init__("Roar!")

class Tiger(Animal):
    type = "Tiger"

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    bird = Bird()

    print(dog)                       # Dog
    print(dog.speak(DogSound()))     # Woof!
    print(cat)                       # Cat
    print(cat.speak(CatSound()))     # Meow!
    print(bird)                      # Bird
    print(bird.speak(BirdSound()))   # Tweet!
        
    # 사용 시점에도 기존 메커니즘 그대로 동작
    tiger = Tiger()
    print(tiger.speak(TigerSound()))  # Roar!
    
    # 에러 테스트 (계약 위반 시 명확한 도메인 에러 발생)
    #dog.speak("Wrong String Data") 
    # __main__.InvalidSoundTypeError: Expected AnimalSound instance, but got str