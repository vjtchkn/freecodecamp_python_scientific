# Function that returns greeting in the specified language


def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"


print(greet("en"))
print(greet("es"))
print(greet("fr"))
