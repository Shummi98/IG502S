import subprocess
import sys,os
import time
from importlib.metadata import version, PackageNotFoundError
from colorama import Fore, Style, init

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

init(autoreset=True)


def slow_print(text, color=Fore.WHITE, delay=0.02):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print()


def spinner(message, duration=1.2):
    chars = ["|", "/", "-", "\\"]
    end = time.time() + duration

    while time.time() < end:
        for c in chars:
            print(
                f"\r{Fore.CYAN}{message} {c}",
                end="",
                flush=True
            )
            time.sleep(0.1)

    print("\r" + " " * 60, end="\r")


def get_requirements(file="requirements.txt"):
    packages = []

    with open(file) as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            package = line
            for sep in ["==", ">=", "<=", "~=", "!=", ">", "<"]:
                if sep in line:
                    package = line.split(sep)[0].strip()
                    break

            packages.append((package, line))

    return packages


def installed(package):
    try:
        version(package)
        return True
    except PackageNotFoundError:
        return False


def install(requirement):
    spinner(f"Installing {requirement}")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", requirement],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def banner():
    print(Fore.CYAN + "=" * 60)
    slow_print("      Python Requirements Installer", Fore.LIGHTCYAN_EX, 0.03)
    print(Fore.CYAN + "=" * 60)
    print()


def main():
    banner()

    requirements = get_requirements()

    for package, requirement in requirements:

        spinner(f"Checking {package}")

        if installed(package):
            slow_print(
                f"[✓] {package} is already installed.",
                Fore.GREEN
            )
        else:
            slow_print(
                f"[✗] {package} not found.",
                Fore.YELLOW
            )

            install(requirement)

            slow_print(
                f"[✓] {package} installed successfully!",
                Fore.GREEN
            )

        time.sleep(0.3)

    print()
    slow_print(
        "✔ All required packages are ready!",
        Fore.LIGHTGREEN_EX,
        0.03
    )


if __name__ == "__main__":
    clear()
    main()
    import subprocess
import sys

print()
slow_print(
    "✔ All required packages are ready!",
    Fore.LIGHTGREEN_EX,
    0.03
)

time.sleep(1)

slow_print(
    "WELCOME TO THE IG502 BOT...",
    Fore.CYAN,
    0.03
)

subprocess.run([sys.executable, "Reports.py"])