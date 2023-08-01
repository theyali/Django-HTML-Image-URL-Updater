import eel

eel.init("web")

@eel.expose
def hello_from_python():
    return "Hello from Python!"

eel.start("main.html", size=(500, 400))