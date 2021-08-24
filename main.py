# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI
from routes.index import user

app = FastAPI()

app.include_router(user)


# class MyClass(object):
#     def __init__(self, name, number, birthDay, image):
#         self.name = name
#         self.number = number
#         self.birthDay = birthDay
#         self.image = image
#
#
# my_objects = []
# my_objects.append(MyClass("MD. ARIFUL ISLAM", "01711240984", "27th March",
#                           "https://media-exp1.licdn.com/dms/image/C4D03AQF4EBI7h2LSiQ/profile-displayphoto-shrink_200_200/0/1517272352221?e=1616630400&v=beta&t=4RiirycFp-sIS_dAJiEOm9d80UfCVWhNuWdPLpzaOX0"))
# my_objects.append(MyClass("MD. Zunayed Arifin", "01683174774", "09th December",
#                           "https://media-exp1.licdn.com/dms/image/C5103AQEG7u4KCMfGTg/profile-displayphoto-shrink_200_200/0/1569730984063?e=1616630400&v=beta&t=A_05QmnPCsl3AEC9xvB3ctXu7OuQ26_VPWXdDGVxSbg"))
# my_objects.append(MyClass("Rounak aftab", "01723755664", "Not Defined",
#                           "https://media-exp1.licdn.com/dms/image/C5103AQFeLuWKxBsUvw/profile-displayphoto-shrink_200_200/0/1578300901332?e=1616630400&v=beta&t=KZBg6FAepuHVlaLjQFGbOyHup190e5Txzpo4ArhzVpA"))
# my_objects.append(MyClass("Md. Ashrafuzzaman Rafi", "01401155138", "11th June",
#                           "https://media-exp1.licdn.com/dms/image/C4E03AQGk4Lw4evUz3w/profile-displayphoto-shrink_200_200/0/1516926922423?e=1616630400&v=beta&t=W_KgHvlrznsk7R6OoOLmvnKBZQ0PzAY-UDE01Apl2J8"))
# my_objects.append(MyClass("Md.Rashedul Hoque Bhuiyan", "01401155118", "Not Defined",
#                           "https://media-exp1.licdn.com/dms/image/C5603AQGzfnyiAoFL9g/profile-displayphoto-shrink_200_200/0/1588599590225?e=1616630400&v=beta&t=nvqKXhatEFPCRIbu5J1nFerwMn7VuAs78Vju4ApNm4g"))
# my_objects.append(MyClass("Ramananda Sarkar", "01401155116", "07th October",
#                           "https://media-exp1.licdn.com/dms/image/C5603AQFSso5OlE_amw/profile-displayphoto-shrink_200_200/0/1517486587719?e=1616630400&v=beta&t=MltdJG1DNzDAQDE9xeEnt5wnTeFhL4MNo9fTpaJF5mY"))
# my_objects.append(MyClass("Kowsar Ahmed", "01401155152", "Not Defined",
#                           "https://media-exp1.licdn.com/dms/image/C4E03AQGGM9nfn4MzDA/profile-displayphoto-shrink_200_200/0/1604983267236?e=1616630400&v=beta&t=8ciz_6HJhUmpkESJplFtVlIVIc-NFXSjAjcngU1WBeU"))


# later

@app.get("/partners")
async def root():
    return {"message": my_objects}
