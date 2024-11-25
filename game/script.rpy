define Game = Character('', color="#FF8000")
define f = Character('...', color="#C6C3B5")

# Kostya
define Kostya = Character('Костя', color="#C6C3B5", image="KostyaI")
image side KostyaI = 'Kostya/Kostya.png'

# Bus
define Bus = Character('Автобус', color="#FFFF00")

# Dima
define Dima = Character('Дима', color="#C6C3B5", image="DimaI")
image side DimaI = 'Dima/Dima.png'


label start:
    play music "music/music1.mp3"
    scene home
    Game "Главный герой Костя видит сон, где еле различимая фигура со светом говорит непонятные вещи"
    f "Ты должен написать код"

    Game "*звенит будильник*"

    Kostya "Блин, проспал всё таки"
    Kostya "4 часа сна перед уником - не лучшая идея"

    Game "*Костя надевает футболку с логотипом УрФУ, джинсы и бежит на автобус*"

    scene bus
    with dissolve

    Game "*В автобусе Костя встречает своего коллегу*"
    Dima "Здарова!! Тоже проспал?"
    Kostya "Ага, работал над нашей прогой до 4 утра. А ты чего?"
    Dima "Да, отмечали вчера запуск нашего квантового компа в лабе. Ты чего не пришёл кстати?"
    Kostya "И без того дел хватает, я же так-то ещё учусь, помимо аспирантуры."
    Dima "Ну ладно, потом ещё отметим с тобой лично"
    play sound "sounds/bus.mp3"
    Bus 'Остановка "профессорская"'
    Kostya "Ладно, побежали быстрее"

    return
