from flask import redirect, render_template


def character(name):
    return render_template('character.html', name=name)

charactericon = 'https://api.genshin.dev/characters/{}/icon.png'
iconv2 = "https://rerollcdn.com/GENSHIN/Characters/{}.png"
weaponimages = 'https://rerollcdn.com/GENSHIN/Icons/NEW/{}.png'

endpoint_list = [
    {"route": "/anemo-traveler",
    "view_func": character,
    "name" : "ترافلر",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "رياح",
    "type" : "https://api.genshin.dev/elements/anemo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('traveler-anemo')
    },
    {"route": "/electro-traveler",
    "view_func": character,
    "name" : "ترافلر",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "كهرباء",
    "type" : "https://api.genshin.dev/elements/electro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('traveler-electro')
    },
    {"route": "/geo-traveler",
    "view_func": character,
    "name" : "ترافلر",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "أرض",
    "type" : "https://api.genshin.dev/elements/geo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('traveler-geo')
    },
    {"route": "/albedo",
    "view_func": character,
    "name" : "البيدو",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "أرض",
    "type" : "https://api.genshin.dev/elements/geo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('albedo')
    },
    {"route": "/aloy",
    "view_func": character,
    "name" : "ألوي",
    "rate" : 5,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "ثلج",
    "type" : "https://api.genshin.dev/elements/cryo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('aloy')
    },
    {"route": "/amber",
    "view_func": character,
    "name" : "آمبر",
    "rate" : 4,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "نار",
    "type" : "https://api.genshin.dev/elements/pyro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('amber')
    },
    {"route": "/kamisato-ayaka",
    "view_func": character,
    "name" : "كاميساتو أياكا",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "ثلج",
    "type" : "https://api.genshin.dev/elements/cryo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('ayaka')
    },
    {"route": "/kamisato-ayato",
    "view_func": character,
    "name" : "كاميساتو أياتو",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "ثلج",
    "type" : "https://api.genshin.dev/elements/cryo/icon.png",
    "released" : True,
    "portrait" : f"{iconv2}".format('Ayato')
    },
    {"route": "/barbara",
    "view_func": character,
    "name" : "باربارا",
    "rate" : 4,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "ماء",
    "type" : "https://api.genshin.dev/elements/hydro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('barbara')
    },
    {"route": "/beidou",
    "view_func": character,
    "name" : "بيدو",
    "rate" : 4,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "كهرباء",
    "type" : "https://api.genshin.dev/elements/electro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('beidou')
    },
    {"route": "/bennett",
    "view_func": character,
    "name" : "بينيت",
    "rate" : 4,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "نار",
    "type" : "https://api.genshin.dev/elements/pyro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('bennett')
    },
    {"route": "/childe",
    "view_func": character,
    "name" : "تشايلد",
    "rate" : 5,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "ماء",
    "type" : "https://api.genshin.dev/elements/hydro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('tartaglia')
    },
    {"route": "/chongyun",
    "view_func": character,
    "name" : "شونقيون",
    "rate" : 4,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "ثلج",
    "type" : "https://api.genshin.dev/elements/cryo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('chongyun')
    },
    {"route": "/diluc",
    "view_func": character,
    "name" : "ديلوك",
    "rate" : 5,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "ثلج",
    "type" : "https://api.genshin.dev/elements/cryo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('diluc')
    },
    {"route": "/diona",
    "view_func": character,
    "name" : "ديونا",
    "rate" : 4,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "ثلج",
    "type" : "https://api.genshin.dev/elements/cryo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('diona')
    },
    {"route": "/eula",
    "view_func": character,
    "name" : "أيولا",
    "rate" : 5,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "ثلج",
    "type" : "https://api.genshin.dev/elements/cryo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('eula')
    },
    {"route": "/fischl",
    "view_func": character,
    "name" : "فيشل",
    "rate" : 4,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "كهرباء",
    "type" : "https://api.genshin.dev/elements/electro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('fischl')
    },
    {"route": "/ganyu",
    "view_func": character,
    "name" : "قانيو",
    "rate" : 5,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "ثلج",
    "type" : "https://api.genshin.dev/elements/cryo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('ganyu')
    },
    {"route": "/gorou",
    "view_func": character,
    "name" : "قورو",
    "rate" : 4,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "أرض",
    "type" : "https://api.genshin.dev/elements/geo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('gorou')
    },
    {"route": "/hutao",
    "view_func": character,
    "name" : "هوتاو",
    "rate" : 5,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "نار",
    "type" : "https://api.genshin.dev/elements/pyro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('hu-tao')
    },
    {"route": "/arataki-itto",
    "view_func": character,
    "name" : "أراتاكي إيتو",
    "rate" : 5,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "أرض",
    "type" : "https://api.genshin.dev/elements/geo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('arataki-itto')
    },
    {"route": "/jean",
    "view_func": character,
    "name" : "جين",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "رياح",
    "type" : "https://api.genshin.dev/elements/anemo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('jean')
    },
    {"route": "/kaeya",
    "view_func": character,
    "name" : "كايا",
    "rate" : 4,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "ثلج",
    "type" : "https://api.genshin.dev/elements/cryo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('kaeya')
    },
    {"route": "/kaedehara-kazuha",
    "view_func": character,
    "name" : "كازوها",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "رياح",
    "type" : "https://api.genshin.dev/elements/anemo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('kazuha')
    },
    {"route": "/keqing",
    "view_func": character,
    "name" : "كيتشنق",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "كهرباء",
    "type" : "https://api.genshin.dev/elements/electro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('keqing')
    },
    {"route": "/klee",
    "view_func": character,
    "name" : "كلي",
    "rate" : 5,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "نار",
    "type" : "https://api.genshin.dev/elements/pyro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('klee')
    },
    {"route": "/sangonomiya-kokomi",
    "view_func": character,
    "name" : "كوكومي",
    "rate" : 5,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "ماء",
    "type" : "https://api.genshin.dev/elements/hydro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('kokomi')
    },
    {"route": "/kuki-shinobu",
    "view_func": character,
    "name" : "شينوبو",
    "rate" : 4,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "كهرباء",
    "type" : "https://api.genshin.dev/elements/electro/icon.png",
    "released" : True,
    "portrait" : f"{iconv2}".format('Kuki%20Shinobu')
    },
    {"route": "/lisa",
    "view_func": character,
    "name" : "ليسا",
    "rate" : 4,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "كهرباء",
    "type" : "https://api.genshin.dev/elements/electro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('lisa')
    },
    {"route": "/mona",
    "view_func": character,
    "name" : "مونا",
    "rate" : 5,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "ماء",
    "type" : "https://api.genshin.dev/elements/hydro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('mona')
    },
    {"route": "/ningguang",
    "view_func": character,
    "name" : "نينقوانق",
    "rate" : 4,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "أرض",
    "type" : "https://api.genshin.dev/elements/geo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('ningguang')
    },
    {"route": "/noelle",
    "view_func": character,
    "name" : "نويل",
    "rate" : 4,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "أرض",
    "type" : "https://api.genshin.dev/elements/geo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('noelle')
    },
    {"route": "/qiqi",
    "view_func": character,
    "name" : "تشي تشي",
    "rate" : 5,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "ثلج",
    "type" : "https://api.genshin.dev/elements/cryo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('qiqi')
    },
    {"route": "/raiden-shogun",
    "view_func": character,
    "name" : "رايدن شوغن",
    "rate" : 5,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "كهرباء",
    "type" : "https://api.genshin.dev/elements/electro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('raiden')
    },
    {"route": "/razor",
    "view_func": character,
    "name" : "ريزر",
    "rate" : 4,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "كهرباء",
    "type" : "https://api.genshin.dev/elements/electro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('razor')
    },
    {"route": "/rosaria",
    "view_func": character,
    "name" : "روزاريا",
    "rate" : 4,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "ثلج",
    "type" : "https://api.genshin.dev/elements/cryo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('rosaria')
    },
    {"route": "/kujou-sara",
    "view_func": character,
    "name" : "سارا",
    "rate" : 4,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "كهرباء",
    "type" : "https://api.genshin.dev/elements/electro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('sara')
    },
    {"route": "/sayu",
    "view_func": character,
    "name" : "سايو",
    "rate" : 4,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "رياح",
    "type" : "https://api.genshin.dev/elements/anemo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('sayu')
    },
    {"route": "/shenhe",
    "view_func": character,
    "name" : "شينهي",
    "rate" : 5,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "ثلج",
    "type" : "https://api.genshin.dev/elements/cryo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('shenhe')
    },
    {"route": "/sucrose",
    "view_func": character,
    "name" : "سوكروس",
    "rate" : 4,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "رياح",
    "type" : "https://api.genshin.dev/elements/anemo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('sucrose')
    },
    {"route": "/thoma",
    "view_func": character,
    "name" : "توما",
    "rate" : 4,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "نار",
    "type" : "https://api.genshin.dev/elements/pyro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('thoma')
    },
    {"route": "/venti",
    "view_func": character,
    "name" : "فينتي",
    "rate" : 5,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "رياح",
    "type" : "https://api.genshin.dev/elements/anemo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('venti')
    },
    {"route": "/xiangling",
    "view_func": character,
    "name" : "شانقلينق",
    "rate" : 4,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "نار",
    "type" : "https://api.genshin.dev/elements/pyro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('xiangling')
    },
    {"route": "/xiao",
    "view_func": character,
    "name" : "شاو",
    "rate" : 5,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "رياح",
    "type" : "https://api.genshin.dev/elements/anemo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('xiao')
    },
    {"route": "/xingqiu",
    "view_func": character,
    "name" : "شنيقشو",
    "rate" : 4,
    "weapon" : "سيف",
    "weaponimg" : f"{weaponimages}".format("sword-icon"),
    "vision" : "ماء",
    "type" : "https://api.genshin.dev/elements/hydro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('xingqiu')
    },
    {"route": "/xinyan",
    "view_func": character,
    "name" : "شينيان",
    "rate" : 4,
    "weapon" : "سيف ثقيل",
    "weaponimg" : f"{weaponimages}".format("claymore-icon"),
    "vision" : "نار",
    "type" : "https://api.genshin.dev/elements/pyro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('xinyan')
    },
    {"route": "/yea-miko",
    "view_func": character,
    "name" : "ياي ميكو",
    "rate" : 5,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "كهرباء",
    "type" : "https://api.genshin.dev/elements/electro/icon.png",
    "released" : True,
    "portrait" : f"{iconv2}".format('Yae%20Miko')
    },
    {"route": "/yanfei",
    "view_func": character,
    "name" : "يانفي",
    "rate" : 4,
    "weapon" : "كتاب",
    "weaponimg" : f"{weaponimages}".format("catalyst-icon"),
    "vision" : "نار",
    "type" : "https://api.genshin.dev/elements/pyro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('yanfei')
    },
    {"route": "/yelan",
    "view_func": character,
    "name" : "ييلان",
    "rate" : 5,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "ماء",
    "type" : "https://api.genshin.dev/elements/hydro/icon.png",
    "released" : True,
    "portrait" : f"{iconv2}".format('Yelan')
    },
    {"route": "/yoimiya",
    "view_func": character,
    "name" : "يويميا",
    "rate" : 5,
    "weapon" : "قوس",
    "weaponimg" : f"{weaponimages}".format("bow-icon"),
    "vision" : "نار",
    "type" : "https://api.genshin.dev/elements/pyro/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('yoimiya')
    },
    {"route": "/yunjin",
    "view_func": character,
    "name" : "يونجين",
    "rate" : 4,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "أرض",
    "type" : "https://api.genshin.dev/elements/geo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('yun-jin')
    },
    {"route": "/zhongli",
    "view_func": character,
    "name" : "زونقلي",
    "rate" : 5,
    "weapon" : "رمح",
    "weaponimg" : f"{weaponimages}".format("polearm-icon"),
    "vision" : "أرض",
    "type" : "https://api.genshin.dev/elements/geo/icon.png",
    "released" : True,
    "portrait" : f"{charactericon}".format('zhongli')
    }
]
