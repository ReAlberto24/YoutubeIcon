class people:
    
    exists = True

    class like:

        game = 'Minecraft Java Edition'

    class everyone:

        likes = []

class make:

    def popular(obj):

       alsoLike = people.everyone.likes 

       alsoLike.append(obj)

       people.everyone.likes = alsoLike
