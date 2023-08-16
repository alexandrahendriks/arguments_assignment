# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Greet Template
def greet(name, template='Hello, <name>!'):
    return(template.replace("<name>", name))

print(greet("Lucas", "What's up <name>?"))

# Force
def force(mass, body="earth"):
    planets = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6,
    }
    if (body in planets):
        force = mass * planets[body]
        return force
    
print(force(2, "pluto"))

# Gravity
def pull(m1, m2, d):
    G = 6.674*(10**-11)
    gravitaion_pull = G * ((m1*m2)/(d**2))
    return gravitaion_pull

print(pull(800, 1500, 3))