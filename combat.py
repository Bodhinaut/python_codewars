def combat(health, damage):
    new_health = (health - damage)
    if new_health < 0:
        new_health = 0

    return (new_health)

combat(500, 700)
    
