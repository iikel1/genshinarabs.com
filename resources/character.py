from flask import redirect, render_template


def character(name, data):
    return render_template('character.html', name=name, data=data)

icons = "rerollcdn.com/GENSHIN/Characters/{}.png"
weaponimages = 'https://rerollcdn.com/GENSHIN/Icons/NEW/{}.png'
vision = '/static/images/Visions/{}.png'
icons = '/static/images/icons/{}.png'
artifact_path = '/static/images/artifact/{}.png'
weapons_path = '/static/images/weapons/{}.png'

artifact_info = {
    "Wanderers_Troupe" : {'2' : '(2) زيادة في نقاط الـ Elemental Mastery', '4' : '(4) زيادة ضرر الضربة المشحونة بنسبة 35% اذا كانت الشخصية تستخدم سلاح قوس او كتاب'},
    "Shimenawas_Reminiscence" : {'2' : '(2) زيادة في قوة الهجوم بنسبة 18%', '4' : '(4) عند إستخدام المهارة (Elemental Skill) سيتم خصم 15 او اكثر من نقاط طاقة المهارة و سيتم زيادة ثوة الضربات العادية و المشحونة و الضربات الساقطة من منتصف الجو بنسبة 50% لمدة 10 ثواني.'},
    "viridescent_venerer" : {'2' : '(2) الحصول على زيادة في قوة عنصر الرياح على الأعداء 15%.', '4' : '(4) زيادة في ضرر تفاعل الدوامة (Swirl) بنسبة 60% و سيقلل من مقاومة العدو بالعنصر المدموج في التفاعل بنسبة 40% لمدة 10 ثواني.'},
    "noblesse_oblige" : {'2' : '(2) زيادة من ضرر المهارة الخاصة بنسبة 20%', '4' : '(4) عند استخدام المهارة الخاصة، ستزداد قوة الهجمات الخاصة بأعضاء الفريق بنسبة 20% لمدة 12 ثانية.'},
    "emblem_of_severed_fate" : {'2' : '(2) زيادة من سرعة شحن المهارة الخاصة بنسبة 20%.', '4' : '(4) زيادة ضرر المهارة الخاصة بمقدار 25% من مجموع سرعة شحن المهارة لديك. المقدار الأقصى الذي يمكن الوصول له بهذه الطريقة هو 75%.'},
    "archaic_petra" :  {'2' : '(2) الحصول على زيادة في قوة عنصر الأرض على الأعداء 15%.', '4' : '(4) عند أخذ كريستالة تم إنشاؤها عن طريق تفاعل عنصر الأرض مع العناصر الأخرى أثناء القتال، سيحصل جميع أعضاء الفريق على زيادة بالضرر العنصري بناء على نفس عنصر الكريستالة الي تم أخذها بنسبة 35%لدة 10 ثواني.'},
    "husk_of_opulent_dreams" : {'2' : '(2) زيادة في مقدار الدفاع بنسبة 30%.', '4' : '(4) عند تواجد الشخصية في ساحة القتال، ستكتسب الشخصية مضاعفة واحدة بعد إصابة العدو بهجمة من عنصر الأرض، و يمكن إكتساب مضاعفة واحدة في كل 0.3 ثانية. عند عدم تواجد الشخصية في ساحة القتال، ستكتسب الشخصية مضاعفة واحدة كل 3 ثوان. يمكن تراكم هذه المضاعفات إلى 4 مضاعفات، و كل مضاعفة ستمنحك زيادة في دفاع الشخصية و زيادة في عنصر الأرض بنسبة 6%. عند مرور 6 ثوان دون الحصول على اي مضاعفة ستفقد الشخصية مضاعفة واحدة.'}
}


endpoint_list = [
    {"route": "/anemo-traveler",
    "view_func": character,
    "name" : "ترافلر",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "رياح",
    "type" : f"{vision}".format("Anemo"),
    "released" : True,
    "build" : {
        "Type" : "شخصية هجومية ثانوية",
        "artifact" :  {
            "best" : {
                "name" : "Viridescent Venerer",
                "type" : "ATK% / Anemo DMG / CRIT DMG",
                "img" : f"{artifact_path}".format("viridescent_venerer"),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
        },
        "weapons" : {
            "best" : {
                "name" : "Skyward Blade",
                "type" : "Energy Recharge",
                "img" : f"{weapons_path}".format("Skyward_Blade")
            },
            "optional" : {
                "name" : "Favonius Sword",
                "type" : "Energy Recharge",
                "img" : f"{weapons_path}".format("Favonius_Sword")
            }
        }
    },
    "portrait" : f"{icons}".format('traveler-anemo')
    },
    {"route": "/electro-traveler",
    "view_func": character,
    "name" : "ترافلر",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "كهرباء",
    "type" : f"{vision}".format("Electro"),
    "released" : True,
    "build" : {
        "Type" : "شخصية داعمة",
        "artifact" :  {
            "best" : {
                "name" : "Emblem of Severed Fate",
                "type" : "Energy Recharge / Electro DMG / CRIT DMG",
                "img" : f"{artifact_path}".format("emblem_of_severed_fate"),
                "info" : {
                    "2" : f"{artifact_info['emblem_of_severed_fate']['2']}",
                    "4" : f"{artifact_info['emblem_of_severed_fate']['4']}"
                }
            },
            "optional" : {
                "name" : "Noblesse Oblige",
                "type" : "Energy Recharge / Electro DMG / CRIT DMG",
                "img" : f"{artifact_path}".format("noblesse_oblige"),
                "info" : {
                    "2" : f"{artifact_info['noblesse_oblige']['2']}",
                    "4" : f"{artifact_info['noblesse_oblige']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "Sacrificial Sword",
                "type" : "Energy Recharge",
                "img" : f"{weapons_path}".format("Sacrificial_Sword")
            },
            "optional" : {
                "name" : "Favonius Sword",
                "type" : "Energy Recharge",
                "img" : f"{weapons_path}".format("Favonius_Sword")
            }
        }
    },
    "portrait" : f"{icons}".format('traveler-electro')
    },
    {"route": "/geo-traveler",
    "view_func": character,
    "name" : "ترافلر",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "أرض",
    "type" : f"{vision}".format("Geo"),
    "released" : True,
    "build" : {
        "Type" : "شخصية هجومية ثانوية",
        "artifact" :  {
            "best" : {
                "name" : "Archaic Petra",
                "type" : "ATK% / Geo DMG / ATK%",
                "img" : f"{artifact_path}".format("archaic_petra"),
                "info" : {
                    "2" : f"{artifact_info['archaic_petra']['2']}",
                    "4" : f"{artifact_info['archaic_petra']['4']}"
                }
            },
            "optional" : {
                "name" : "Noblesse Oblige",
                "type" : "ATK% / Geo DMG / ATK%",
                "img" : f"{artifact_path}".format("noblesse_oblige"),
                "info" : {
                    "2" : f"{artifact_info['noblesse_oblige']['2']}",
                    "4" : f"{artifact_info['noblesse_oblige']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "Skyward_Blade",
                "type" : "Energy Recharge",
                "img" : f"{weapons_path}".format("Skyward_Blade")
            },
            "optional" : {
                "name" : "Favonius Sword",
                "type" : "Energy Recharge",
                "img" : f"{weapons_path}".format("Favonius_Sword")
            }
        }
    },
    "portrait" : f"{icons}".format('traveler-geo')
    },
    {"route": "/albedo",
    "view_func": character,
    "name" : "البيدو",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "أرض",
    "type" : f"{vision}".format("Geo"),
    "released" : True,
    "build" : {
        "Type" : "شخصية هجومية ثانوية",
        "artifact" :  {
            "best" : {
                "name" : "Husk of Opulent Dreams",
                "type" : "DEF% / Geo DMG / CRIT DMG",
                "img" : f"{artifact_path}".format("husk_of_opulent_dreams"),
                "info" : {
                    "2" : f"{artifact_info['husk_of_opulent_dreams']['2']}",
                    "4" : f"{artifact_info['husk_of_opulent_dreams']['4']}"
                }
            },
            "optional" : {
                "name" : "Archaic Petra",
                "type" : "DEF% / Geo DMG / CRIT DMG",
                "img" : f"{artifact_path}".format("archaic_petra"),
                "info" : {
                    "2" : f"{artifact_info['archaic_petra']['2']}",
                    "4" : f"{artifact_info['archaic_petra']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "Cinnabar Spindle",
                "type" : "DEF",
                "img" : f"{weapons_path}".format("Cinnabar_Spindle")
            },
            "optional" : {
                "name" : "Harbinger of Dawn",
                "type" : "CRIT DMG",
                "img" : f"{weapons_path}".format("Harbinger_of_Dawn")
            }
        }
    },
    "portrait" : f"{icons}".format('albedo')
    },
    {"route": "/aloy",
    "view_func": character,
    "name" : "ألوي",
    "rate" : 5,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "ثلج",
    "type" : f"{vision}".format("Cryo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('aloy')
    },
    {"route": "/amber",
    "view_func": character,
    "name" : "آمبر",
    "rate" : 4,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "نار",
    "type" : f"{vision}".format("Pyro"),
    "released" : True,
    "build" : {
        "Type" : "شخصية هجومية",
        "artifact" : {
            "best" : {
                "name" : "Shimenawa's Reminiscence",
                "type" : "ATK% / Pyro DMG / CRIT DMG",
                "img" : f"{artifact_path}".format("Shimenawa's_Reminiscence"),
                "info" : {
                    "2" : f"{artifact_info['Shimenawas_Reminiscence']['2']}",
                    "4" : f"{artifact_info['Shimenawas_Reminiscence']['4']}",
                }
            },
            "optional" : {
                "name" : "Wanderer's Troupe",
                "type" : "ATK% / Pyro DMG / CRIT DMG",
                "img" : f"{artifact_path}".format("Wanderer's_Troupe"),
                "info" : {
                    "2" : f"{artifact_info['Wanderers_Troupe']['2']}",
                    "4" : f"{artifact_info['Wanderers_Troupe']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "Amos' Bow",
                "type" : "ATK",
                "img" : f"{weapons_path}".format("Amos'_Bow")
            },
            "optional" : {
                "name" : "Sharpshooter's Oath",
                "type" : "CRIT DMG",
                "img" : f"{weapons_path}".format("Sharpshooter's_Oath")
            }
        }
    },
    "portrait" : f"{icons}".format('amber')
    },
    {"route": "/kamisato-ayaka",
    "view_func": character,
    "name" : "كاميساتو أياكا",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "ثلج",
    "type" : f"{vision}".format("Cryo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('ayaka')
    },
    {"route": "/kamisato-ayato",
    "view_func": character,
    "name" : "كاميساتو أياتو",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "ثلج",
    "type" : f"{vision}".format("Cryo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('Ayato')
    },
    {"route": "/barbara",
    "view_func": character,
    "name" : "باربارا",
    "rate" : 4,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "ماء",
    "type" : f"{vision}".format("Hydro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('barbara')
    },
    {"route": "/beidou",
    "view_func": character,
    "name" : "بيدو",
    "rate" : 4,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "كهرباء",
    "type" : f"{vision}".format("Electro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('beidou')
    },
    {"route": "/bennett",
    "view_func": character,
    "name" : "بينيت",
    "rate" : 4,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "نار",
    "type" : f"{vision}".format("Pyro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('bennett')
    },
    {"route": "/childe",
    "view_func": character,
    "name" : "تشايلد",
    "rate" : 5,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "ماء",
    "type" : f"{vision}".format("Hydro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('tartaglia')
    },
    {"route": "/chongyun",
    "view_func": character,
    "name" : "شونقيون",
    "rate" : 4,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "ثلج",
    "type" : f"{vision}".format("Cryo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('chongyun')
    },
    {"route": "/diluc",
    "view_func": character,
    "name" : "ديلوك",
    "rate" : 5,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "ثلج",
    "type" : f"{vision}".format("Cryo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('diluc')
    },
    {"route": "/diona",
    "view_func": character,
    "name" : "ديونا",
    "rate" : 4,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "ثلج",
    "type" : f"{vision}".format("Cryo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('diona')
    },
    {"route": "/eula",
    "view_func": character,
    "name" : "أيولا",
    "rate" : 5,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "ثلج",
    "type" : f"{vision}".format("Cryo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('eula')
    },
    {"route": "/fischl",
    "view_func": character,
    "name" : "فيشل",
    "rate" : 4,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "كهرباء",
    "type" : f"{vision}".format("Electro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('fischl')
    },
    {"route": "/ganyu",
    "view_func": character,
    "name" : "قانيو",
    "rate" : 5,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "ثلج",
    "type" : f"{vision}".format("Cryo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('ganyu')
    },
    {"route": "/gorou",
    "view_func": character,
    "name" : "قورو",
    "rate" : 4,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "أرض",
    "type" : f"{vision}".format("Geo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('gorou')
    },
    {"route": "/hutao",
    "view_func": character,
    "name" : "هوتاو",
    "rate" : 5,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "نار",
    "type" : f"{vision}".format("Pyro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('hu-tao')
    },
    {"route": "/arataki-itto",
    "view_func": character,
    "name" : "أراتاكي إيتو",
    "rate" : 5,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "أرض",
    "type" : f"{vision}".format("Geo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('arataki-itto')
    },
    {"route": "/jean",
    "view_func": character,
    "name" : "جين",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "رياح",
    "type" : f"{vision}".format("Anemo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('jean')
    },
    {"route": "/kaeya",
    "view_func": character,
    "name" : "كايا",
    "rate" : 4,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "ثلج",
    "type" : f"{vision}".format("Cryo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('kaeya')
    },
    {"route": "/kaedehara-kazuha",
    "view_func": character,
    "name" : "كازوها",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "رياح",
    "type" : f"{vision}".format("Anemo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('kazuha')
    },
    {"route": "/keqing",
    "view_func": character,
    "name" : "كيتشنق",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "كهرباء",
    "type" : f"{vision}".format("Electro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('keqing')
    },
    {"route": "/klee",
    "view_func": character,
    "name" : "كلي",
    "rate" : 5,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "نار",
    "type" : f"{vision}".format("Pyro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('klee')
    },
    {"route": "/sangonomiya-kokomi",
    "view_func": character,
    "name" : "كوكومي",
    "rate" : 5,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "ماء",
    "type" : f"{vision}".format("Hydro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('kokomi')
    },
    {"route": "/kuki-shinobu",
    "view_func": character,
    "name" : "شينوبو",
    "rate" : 4,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "كهرباء",
    "type" : f"{vision}".format("Electro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('Kuki_Shinobu')
    },
    {"route": "/lisa",
    "view_func": character,
    "name" : "ليسا",
    "rate" : 4,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "كهرباء",
    "type" : f"{vision}".format("Electro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('lisa')
    },
    {"route": "/mona",
    "view_func": character,
    "name" : "مونا",
    "rate" : 5,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "ماء",
    "type" : f"{vision}".format("Hydro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('mona')
    },
    {"route": "/ningguang",
    "view_func": character,
    "name" : "نينقوانق",
    "rate" : 4,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "أرض",
    "type" : f"{vision}".format("Geo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('ningguang')
    },
    {"route": "/noelle",
    "view_func": character,
    "name" : "نويل",
    "rate" : 4,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "أرض",
    "type" : f"{vision}".format("Geo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('noelle')
    },
    {"route": "/qiqi",
    "view_func": character,
    "name" : "تشي تشي",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "ثلج",
    "type" : f"{vision}".format("Cryo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('qiqi')
    },
    {"route": "/raiden-shogun",
    "view_func": character,
    "name" : "رايدن شوغن",
    "rate" : 5,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "كهرباء",
    "type" : f"{vision}".format("Electro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('raiden')
    },
    {"route": "/razor",
    "view_func": character,
    "name" : "ريزر",
    "rate" : 4,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "كهرباء",
    "type" : f"{vision}".format("Electro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('razor')
    },
    {"route": "/rosaria",
    "view_func": character,
    "name" : "روزاريا",
    "rate" : 4,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "ثلج",
    "type" : f"{vision}".format("Cryo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('rosaria')
    },
    {"route": "/kujou-sara",
    "view_func": character,
    "name" : "سارا",
    "rate" : 4,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "كهرباء",
    "type" : f"{vision}".format("Electro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('sara')
    },
    {"route": "/sayu",
    "view_func": character,
    "name" : "سايو",
    "rate" : 4,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "رياح",
    "type" : f"{vision}".format("Anemo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('sayu')
    },
    {"route": "/shenhe",
    "view_func": character,
    "name" : "شينهي",
    "rate" : 5,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "ثلج",
    "type" : f"{vision}".format("Cryo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('shenhe')
    },
    {"route": "/sucrose",
    "view_func": character,
    "name" : "سوكروس",
    "rate" : 4,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "رياح",
    "type" : f"{vision}".format("Anemo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('sucrose')
    },
    {"route": "/thoma",
    "view_func": character,
    "name" : "توما",
    "rate" : 4,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "نار",
    "type" : f"{vision}".format("Pyro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('thoma')
    },
    {"route": "/venti",
    "view_func": character,
    "name" : "فينتي",
    "rate" : 5,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "رياح",
    "type" : f"{vision}".format("Anemo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('venti')
    },
    {"route": "/xiangling",
    "view_func": character,
    "name" : "شانقلينق",
    "rate" : 4,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "نار",
    "type" : f"{vision}".format("Pyro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('xiangling')
    },
    {"route": "/xiao",
    "view_func": character,
    "name" : "شاو",
    "rate" : 5,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "رياح",
    "type" : f"{vision}".format("Anemo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('xiao')
    },
    {"route": "/xingqiu",
    "view_func": character,
    "name" : "شنيقشو",
    "rate" : 4,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "ماء",
    "type" : f"{vision}".format("Hydro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('xingqiu')
    },
    {"route": "/xinyan",
    "view_func": character,
    "name" : "شينيان",
    "rate" : 4,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "نار",
    "type" : f"{vision}".format("Pyro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('xinyan')
    },
    {"route": "/yea-miko",
    "view_func": character,
    "name" : "ياي ميكو",
    "rate" : 5,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "كهرباء",
    "type" : f"{vision}".format("Electro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('Yae%20Miko')
    },
    {"route": "/yanfei",
    "view_func": character,
    "name" : "يانفي",
    "rate" : 4,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "نار",
    "type" : f"{vision}".format("Pyro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('yanfei')
    },
    {"route": "/yelan",
    "view_func": character,
    "name" : "ييلان",
    "rate" : 5,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "ماء",
    "type" : f"{vision}".format("Hydro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('Yelan')
    },
    {"route": "/yoimiya",
    "view_func": character,
    "name" : "يويميا",
    "rate" : 5,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "نار",
    "type" : f"{vision}".format("Pyro"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('yoimiya')
    },
    {"route": "/yunjin",
    "view_func": character,
    "name" : "يونجين",
    "rate" : 4,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "أرض",
    "type" : f"{vision}".format("Geo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('yun-jin')
    },
    {"route": "/zhongli",
    "view_func": character,
    "name" : "زونقلي",
    "rate" : 5,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "أرض",
    "type" : f"{vision}".format("Geo"),
    "released" : True,
    "build" : {
        "Type" : "",
        "artifact" :  {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{artifact_path}".format(""),
                "info" : {
                    "2" : f"{artifact_info['viridescent_venerer']['2']}",
                    "4" : f"{artifact_info['viridescent_venerer']['4']}"
                }
            }
        },
        "weapons" : {
            "best" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            },
            "optional" : {
                "name" : "",
                "type" : "",
                "img" : f"{weapons_path}".format("")
            }
        }
    },
    "portrait" : f"{icons}".format('zhongli')
    }
]
