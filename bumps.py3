def bumps(road):
    return "Woohoo!" if road.count("n") <= 15 else "Car Dead"
# test case below
bumps("nn_nnnn__nn___n____n___nn__nnn")