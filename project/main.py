import minecraft, world

while world.people.exists:

    if world.people.like.game == minecraft.game:

        world.make.popular(minecraft.game)
        break

    else:

        continue

print(world.people.everyone.likes)