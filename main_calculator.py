import sys
import time
import history_utils
from calculator import Calculator
from colors import Colors


def welcome_animation():
    """
    Makes a cool animation
    """
    ascii_art = r"""
╔═════════════════════════════════════════════════╗
║                               MAX CALCULATOR                                   ║
╚═════════════════════════════════════════════════╝
    """

    # Display the ASCII art with color and delay
    print(Colors.CYAN + Colors.BOLD)
    for line in ascii_art.split("\n"):
        print(line)
        time.sleep(0.1)
    print(Colors.ENDC)

    # Add a loading animation
    loading_text = "Launching MAX CALCULATOR"
    for i in range(3):
        sys.stdout.write(f"\r{loading_text}{'.' * (i + 1)}{' ' * (3 - i)}")
        sys.stdout.flush()
        time.sleep(0.5)

    sys.stdout.write("\r" + " " * len(loading_text + "...") + "\r")  # Clear the line
    print(f"{Colors.GREEN}MAX CALCULATOR is Ready! Ω{Colors.ENDC}\n")
    time.sleep(0.5)


def main():
    try:
        welcome_animation()  # Show the animation at the start

        print(f"{Colors.BLUE}Type mathematical expressions to evaluate them.{Colors.ENDC}")
        print(f"{Colors.BLUE}Type {Colors.ENDC}[{Colors.WARNING}q{Colors.ENDC}]{Colors.BLUE} to quit at any time."
              f"{Colors.ENDC}")
        print(f"{Colors.BLUE}Type {Colors.ENDC}[{Colors.WARNING}h{Colors.ENDC}]{Colors.BLUE} to view the history."
              f"{Colors.ENDC}\n")

        while True:
            exp = input(f"\n{Colors.BOLD}Enter an expression: {Colors.ENDC}").strip()

            if exp.lower() == "q":
                print(f"\n{Colors.BLUE}Thank you for using MAX CALCULATOR! Goodbye!{Colors.ENDC}")
                break
            if exp.lower() == "h":
                history_utils.display_history(Calculator.expression_history)  # Pass the class-level history attribute
                continue

            calc = Calculator(exp)
            calc.calculate()

    except KeyboardInterrupt:
        print(f"\n\n{Colors.BLUE}Goodbye! See you next time!{Colors.ENDC}")


if __name__ == "__main__":
    main()
