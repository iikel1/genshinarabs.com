from flask import redirect, render_template


def character(name):
    return render_template('character.html', name=name)


endpoint_list = [
    {"route": "/amber",
    "view_func": character,
    "name" : "Amber"
    },
    {"route": "/traveller",
    "view_func": character,
    "name" : "Traveller"
    },
]
