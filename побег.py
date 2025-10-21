def intro():
    print("🔔 Звонок! Последний урок закончился, но ты задержан после колледжа.")
    print("Твоя цель — сбежать из колледжа, не попавшись охраннику.")
    input("Нажми Enter, чтобы начать побег...")


def choose_path():
    print("\nТы находишься в коридоре. Перед тобой две дороги:")
    print("1. Пойти налево, к лестнице.")
    print("2. Пойти направо, в библиотеку.")
    choice = input("Куда пойдешь? (1/2): ")
    return choice


def stair_path():
    print("\nТы идешь к лестнице. Она ведет к выходу, но охранник часто там сидит.")
    print("1. Попробовать проскользнуть мимо.")
    print("2. Спрятаться и подождать.")
    choice = input("Что сделаешь? (1/2): ")
    if choice == "1":
        print("\n🚨 О нет! Охранник тебя заметил. Побег провален.")
        return False
    elif choice == "2":
        print("\n⏳ Ты подождал, охранник ушел покурить. Ты быстро выбегаешь на улицу.")
        print("🎉 Побег удался! Свобода!")
        return True
    else:
        print("Некорректный выбор.")
        return stair_path()


def library_path():
    print("\nТы заходишь в библиотеку. Пусто.")
    print("На столе лежит ключ и карта школы.")
    print("1. Взять ключ.")
    print("2. Взять карту.")
    print("3. Взять оба предмета.")
    choice = input("Что возьмешь? (1/2/3): ")
    has_key = False
    has_map = False
    if choice == "1":
        has_key = True
    elif choice == "2":
        has_map = True
    elif choice == "3":
        has_key = True
        has_map = True
    else:
        print("Некорректный выбор.")
        return library_path()

    print("\nТы выходишь из библиотеки и слышишь шаги.")
    print("1. Спрятаться в туалете.")
    print("2. Попробовать открыть запасной выход.")
    choice2 = input("Что делаешь? (1/2): ")

    if choice2 == "1":
        print("\nТы спрятался. Шаги стихли.")
        print("Ты выходишь, но дверь запасного выхода закрыта.")
        if has_key:
            print("🔑 У тебя есть ключ! Ты открываешь дверь и выходишь наружу.")
            print("🎉 Побег удался!")
            return True
        else:
            print("🔒 У тебя нет ключа. Ты застрял внутри. Побег провален.")
            return False
    elif choice2 == "2":
        if has_key:
            print("🔑 Ты быстро открываешь дверь и убегаешь.")
            print("🎉 Побег удался!")
            return True
        else:
            print("🔒 Дверь закрыта. Ты не можешь её открыть.")
            print("🚨 Охранник тебя находит. Побег провален.")
            return False
    else:
        print("Некорректный выбор.")
        return library_path()


def main():
    intro()
    path = choose_path()
    success = False
    if path == "1":
        success = stair_path()
    elif path == "2":
        success = library_path()
    else:
        print("Некорректный выбор. Игра завершена.")
        return

    print("\nСпасибо за игру!")
    if success:
        print("Ты успешно сбежал из школы!")
    else:
        print("Попробуй снова!")


if __name__ == "__main__":
    main()
