import configparser

config_ini = "config.ini"

numbers = {
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
    "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10,
    "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13,
    "четырнадцать": 14, "пятнадцать": 15, "шестнадцать": 16,
    "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19,
    "двадцать": 20, "двадцать один": 21, "двадцать два": 22,
    "двадцать три": 23, "двадцать четыре": 24, "двадцать пять": 25,
    "двадцать шесть": 26, "двадцать семь": 27, "двадцать восемь": 28,
    "двадцать девять": 29, "тридцать": 30, "тридцать один": 31,
    "тридцать два": 32, "тридцать три": 33, "тридцать четыре": 34,
    "тридцать пять": 35, "тридцать шесть": 36, "тридцать семь": 37,
    "тридцать восемь": 38, "тридцать девять": 39, "сорок": 40,
    "сорок один": 41, "сорок два": 42, "сорок три": 43,
    "сорок четыре": 44, "сорок пять": 45, "сорок шесть": 46,
    "сорок семь": 47, "сорок восемь": 48, "сорок девять": 49,
    "пятьдесят": 50, "пятьдесят один": 51, "пятьдесят два": 52,
    "пятьдесят три": 53, "пятьдесят четыре": 54, "пятьдесят пять": 55,
    "пятьдесят шесть": 56, "пятьдесят семь": 57, "пятьдесят восемь": 58,
    "пятьдесят девять": 59, "шестьдесят": 60, "шестьдесят один": 61,
    "шестьдесят два": 62, "шестьдесят три": 63, "шестьдесят четыре": 64,
    "шестьдесят пять": 65, "шестьдесят шесть": 66, "шестьдесят семь": 67,
    "шестьдесят восемь": 68, "шестьдесят девять": 69, "семьдесят": 70,
    "семьдесят один": 71, "семьдесят два": 72, "семьдесят три": 73,
    "семьдесят четыре": 74, "семьдесят пять": 75, "семьдесят шесть": 76,
    "семьдесят семь": 77, "семьдесят восемь": 78, "семьдесят девять": 79,
    "восемьдесят": 80, "восемьдесят один": 81, "восемьдесят два": 82,
    "восемьдесят три": 83, "восемьдесят четыре": 84, "восемьдесят пять": 85,
    "восемьдесят шесть": 86, "восемьдесят семь": 87, "восемьдесят восемь": 88,
    "восемьдесят девять": 89, "девяносто": 90, "девяносто один": 91,
    "девяносто два": 92, "девяносто три": 93, "девяносто четыре": 94,
    "девяносто пять": 95, "девяносто шесть": 96, "девяносто семь": 97,
    "девяносто восемь": 98, "девяносто девять": 99, "сто": 100, "стол": 100
}

press_words = ["нажми"]
pressing_words = ["зажми"]
unpressing_words = ["отпусти"]

buttons = {
    "альт": "Alt",
    "контроль": "Ctrl",
    "шифт": "Shift",
    "капс": "Caps Lock",
    "капс лок": "Caps Lock",
    "таб": "Tab",
    "ввод": "Enter",
    "энтер": "Enter",
    "нтр": "Enter",
    "возврат": "Backspace",
    "бэкспейс": "Backspace",
    "бекспейс": "Backspace",
    "удаление": "Delete",
    "делит": "Delete",
    "вставка": "Insert",
    "домой": "Home",
    "конец": "End",
    "страница вверх": "Page Up",
    "страница вниз": "Page Down",
    "стрелка вверх": "Arrow Up",
    "стрелка вниз": "Arrow Down",
    "стрелка влево": "Arrow Left",
    "стрелка вправо": "Arrow Right",
    "эф один": "F1",
    "эф два": "F2",
    "эф три": "F3",
    "эф четыре": "F4",
    "эф пять": "F5",
    "эф шесть": "F6",
    "эф семь": "F7",
    "эф восемь": "F8",
    "эф девять": "F9",
    "эф десять": "F10",
    "эф одиннадцать": "F11",
    "эф двенадцать": "F12",
    "escape": "Escape",
    "печать экрана": "Print Screen",
    "блок прокрутки": "Scroll Lock",
    "пауза": "Pause",
    "пробел": "Space",
    "эй": "A",
    "би": "B",
    "си": "C",
    "ди": "D",
    "и": "E",
    "еф": "F",
    "джи": "G",
    "эйч": "H",
    "ай": "I",
    "джей": "J",
    "кей": "K",
    "эл": "L",
    "эм": "M",
    "эн": "N",
    "оу": "O",
    "пи": "P",
    "кью": "Q",
    "ар": "R",
    "эс": "S",
    "ти": "T",
    "ю": "U",
    "ви": "V",
    "дабл ю": "W",
    "экс": "X",
    "уай": "Y",
    "зи": "Z"
}

config = configparser.ConfigParser()
config.read(config_ini)

def save_ini_file(config):
    with open(config_ini, "w") as configfile:
        config.write(configfile)