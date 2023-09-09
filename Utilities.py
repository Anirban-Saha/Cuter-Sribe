extensions = {
    "java": "java",
    "python": "py",
    "sh": "sh"
}

runstring = {
    "java": "javac Main.java; java Main < inputs 1> outputs 2> errors",
    "python": "python Main.py < inputs 1> outputs 2> errors",
    "sh": "sh Main.sh < inputs 1> outputs 2> errors"
}