import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def print_directory_structure(path, indent=""):
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(indent + Fore.BLUE + f"📂 {item.name}")
                print_directory_structure(item, indent + "    ")
            else:
                print(indent + Fore.GREEN + f"📄 {item.name}")
    except PermissionError:
        print(indent + Fore.RED + "Немає доступу")


def main():
    if len(sys.argv) != 2:
        print("Використання: python hw03.py /шлях/до/директорії")
        return

    directory = Path(sys.argv[1])

    if not directory.exists():
        print(Fore.RED + "Шлях не існує.")
        return

    if not directory.is_dir():
        print(Fore.RED + "Це не директорія.")
        return

    print(Fore.YELLOW + f"📦 {directory.name}")
    print_directory_structure(directory)


if __name__ == "__main__":
    main()