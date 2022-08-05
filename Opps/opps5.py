# multiple inheritance
class Bestie:
    stars=5

    def __init__(self,bname,bage,blook):
        self.name=bname
        self.age=bage
        self.look=blook

    def bestieDetails(self):
        return f"My besti name is {self.name}\nage is {self.age}\nlook is {self.look}"  

class Memories:
    placeMemo="Bangalore"

    def __init__(self,placename,taste,items):
        self.placename=placename
        self.taste=taste
        self.items=items

    def ResturantReview(self):
        return f"The resturant name is {self.placename}\nwe ate {self.items}\n the taste was {self.taste}"

    def Greeting(self):
        return f"Good Morning {self.name} your age is {self.age}"

class Race(Bestie,Memories):
    place="Bangalore NS highway"

    def Racing(self):
        return f"we had a race while coming back at {self.place}"


besti=Bestie("sai",25,"handsome")
memory=Memories("cherry","awesome","biryani")
race=Race("anees",23,"cool")

# print(besti.bestieDetails())
# print(besti.stars)
# #print(besti.place)
# print(memory.ResturantReview())
# print(memory.place)

print(race.bestieDetails())
print(race.Racing())
print(race.place)
print(race.placeMemo)
print(race.Greeting())