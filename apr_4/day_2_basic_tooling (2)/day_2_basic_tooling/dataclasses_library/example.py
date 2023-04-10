from dataclasses import dataclass

@dataclass
class Mountain:
    name: str
    elevation: float

m1 = Mountain(name="karakaram", elevation=8611)
print(type(m1))
print(type(str(m1)))

# from dataclasses import dataclass

# @dataclass
# class Person:
#     first_name: str
#     last_name: str







# print(m1.name)
# print(m1.elevation)



# print(f"Name of mountain is {m1.name} and elevation is {m1.elevation}")