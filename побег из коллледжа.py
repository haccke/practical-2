import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)


player_score = 0

def print_slow(text, delay=0.03, color=Fore.WHITE):
    """Печатает текст с эффектом и цветом"""
    for ch in text:
        print(color + ch + Style.RESET_ALL, end='', flush=True)
        time.sleep(delay)
    print()  # новая строка


def line():
    print(Fore.YELLOW + "-" * 60 + Style.RESET_ALL)


def start_game():
    global player_score
    player_score = 0

    line()
    print_slow("🎮 Добро пожаловать в игру 'Побег из колледжа'!", color=Fore.CYAN)
    print_slow("Ты студент, заснувший на последней паре.", color=Fore.WHITE)
    print_slow("Проснулся — колледж закрыт. Нужно выбраться!", color=Fore.WHITE)
    line()

    choice = input(Fore.GREEN + "Начать игру? (да/нет): " + Style.RESET_ALL).strip().lower()

    if choice == "да":
        level_one()
    else:
        print_slow("Ты решил остаться ночевать в колледже. Конец игры.", color=Fore.RED)
        sys.exit()


def level_one():
    global player_score
    line()
    print_slow("🔒 УРОВЕНЬ 1: ЗАПЕРТАЯ АУДИТОРИЯ", color=Fore.MAGENTA)
    print_slow("Ты в пустой аудитории. Дверь заперта.", color=Fore.WHITE)
    print_slow("На столе лежит записка, под партой что-то блестит.", color=Fore.WHITE)
    line()

    has_key = False
    read_note = False

    while True:
        print(Fore.YELLOW + "\nЧто ты сделаешь?" + Style.RESET_ALL)
        print("1 — Прочитать записку")
        print("2 — Проверить шкаф")
        print("3 — Осмотреть дверь")
        print("4 — Проверить под партой")
        print("5 — Сесть и подумать")

        choice = input(Fore.GREEN + "Выбор: " + Style.RESET_ALL).strip()

        if choice == "1":
            print_slow("На записке написано: 'Ключ там, где тень не кончается.'", color=Fore.CYAN)
            read_note = True
            player_score += 5

        elif choice == "2":
            print_slow("Ты открыл шкаф... внутри старая метла и пыль.", color=Fore.WHITE)
            print_slow("Ничего полезного.", color=Fore.RED)
            player_score -= 1

        elif choice == "3":
            if has_key:
                print_slow("Ты вставляешь ключ в замок и открываешь дверь!", color=Fore.GREEN)
                print_slow("Ты выходишь в коридор.", color=Fore.CYAN)
                player_score += 10
                level_two()
                break
            else:
                print_slow("Дверь заперта. Без ключа не открыть.", color=Fore.RED)

        elif choice == "4":
            if not has_key:
                print_slow("Ты находишь блестящий ключ под партой!", color=Fore.GREEN)
                has_key = True
                player_score += 10
            else:
                print_slow("Под партой уже ничего нет.", color=Fore.WHITE)

        elif choice == "5":
            print_slow("Ты сел и задумался... Но время идёт.", color=Fore.YELLOW)
            if not read_note:
                print_slow("Может, стоит прочитать записку?", color=Fore.CYAN)
            player_score -= 2

        else:
            print_slow("Такого варианта нет. Введи число от 1 до 5.", color=Fore.RED)


def level_two():
    global player_score
    line()
    print_slow("🚪 УРОВЕНЬ 2: КОРИДОР И ОХРАННИК", color=Fore.MAGENTA)
    print_slow("Ты выходишь в длинный коридор. Вдалеке — охранник.", color=Fore.WHITE)
    print_slow("Нужно пройти мимо него и выбраться наружу.", color=Fore.WHITE)
    line()

    disguise = False
    distraction = False
    tried_walk = False

    while True:
        print(Fore.YELLOW + "\nТвои действия:" + Style.RESET_ALL)
        print("1 — Заглянуть в соседнюю аудиторию")
        print("2 — Осмотреть шкафчики у стены")
        print("3 — Попробовать пройти мимо охранника")
        print("4 — Создать шум (отвлечь охранника)")
        print("5 — Подождать немного")

        choice = input(Fore.GREEN + "Выбор: " + Style.RESET_ALL).strip()

        if choice == "1":
            if not disguise:
                print_slow("Ты находишь халат преподавателя и надеваешь его.", color=Fore.GREEN)
                disguise = True
                player_score += 10
            else:
                print_slow("Ты уже переодет. Смотришься убедительно.", color=Fore.WHITE)

        elif choice == "2":
            if not distraction:
                print_slow("Ты находишь старый будильник. Можно использовать для шума.", color=Fore.CYAN)
                distraction = True
                player_score += 5
            else:
                print_slow("Шкафчики уже пусты.", color=Fore.WHITE)

        elif choice == "3":
            if disguise and distraction:
                print_slow("Ты ставишь будильник вдали — он звенит.", color=Fore.YELLOW)
                print_slow("Охранник идёт проверить, а ты спокойно проходишь!", color=Fore.GREEN)
                player_score += 20
                end_game(True)
                break
            elif disguise:
                print_slow("Ты идёшь уверенно, но охранник тебя узнаёт.", color=Fore.RED)
                player_score -= 10
                end_game(False)
                break
            elif distraction:
                print_slow("Ты идёшь после шума, но выглядишь подозрительно.", color=Fore.RED)
                player_score -= 5
                end_game(False)
                break
            else:
                if not tried_walk:
                    print_slow("Ты просто идёшь — и охранник тебя замечает!", color=Fore.RED)
                    player_score -= 10
                    tried_walk = True
                else:
                    print_slow("Охранник вызывает директора. Побег провален.", color=Fore.RED)
                    end_game(False)
                    break

        elif choice == "4":
            if not distraction:
                print_slow("Ты кидаешь будильник в дальний конец коридора.", color=Fore.YELLOW)
                print_slow("Он звенит — охранник уходит проверить!", color=Fore.GREEN)
                distraction = True
                player_score += 10
            else:
                print_slow("Ты уже отвлёк охранника. Больше не нужно.", color=Fore.WHITE)

        elif choice == "5":
            print_slow("Ты ждёшь... охранник зевает, но остаётся на месте.", color=Fore.YELLOW)
            player_score -= 1
        else:
            print_slow("Неверный выбор. Введи число от 1 до 5.", color=Fore.RED)


def end_game(success):
    global player_score
    line()
    print_slow("🏁 ИТОГ ИГРЫ", color=Fore.CYAN)
    print_slow(f"Твои очки: {player_score}", color=Fore.YELLOW)
    line()

    # Разные концовки
    if success:
        print_slow("ПОБЕГ УДАЧЕН! 🎉", color=Fore.GREEN)
        print_slow("Ты выбрался из колледжа и вдохнул свежий воздух.", color=Fore.WHITE)
        print_slow("Ты герой среди студентов!", color=Fore.MAGENTA)
    else:
        if player_score >= 20:
            print_slow("Ты почти сбежал, но тебя остановил охранник.", color=Fore.YELLOW)
            print_slow("Он пожал плечами и отпустил домой.", color=Fore.GREEN)
        else:
            print_slow("Охранник поймал тебя и оставил дежурить в колледже.", color=Fore.RED)
            print_slow("Похоже, побег провалился. 😅", color=Fore.WHITE)

    line()
    again = input(Fore.GREEN + "Хочешь сыграть снова? (да/нет): " + Style.RESET_ALL).strip().lower()

    if again == "да":
        start_game()
    else:
        print_slow("Спасибо за игру! До встречи 👋", color=Fore.CYAN)
        sys.exit()


if __name__ == "__main__":
    start_game()

