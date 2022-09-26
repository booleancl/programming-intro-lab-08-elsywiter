# Podemos utilzar el método especial  __init__ (conocido como constructor)
# y el objeto actual self para hacer un creador de objetos del tipo definido con la
# palabra reservada class
# 

first_dict = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skillis": ["python", "Git", "HTML", "CSS", "javascript"]
}

class student:
    def __init__(self,name,position,skills):
       self.name = name
       self.position = position
       self.skills
    def say_name(self):
        print("Mi nombre es",self.name,"Mi cargo es",self.position,"Mis habilidades son",self.skills)

    Elsy = student("Elsy","Fullstack Developer",["python", "Git", "HTML", "CSS", "javascript",])
    Bob_el_chef = student("Bob_el_chef","kitchen helper",["pastry chef international and cake shop"])
    Elsy.say_name()
    Bod_el_chef.say_name()
