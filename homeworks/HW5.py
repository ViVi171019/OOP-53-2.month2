from colorama import init, Fore, Back, Style

init(autoreset=True)

print(Fore.RED + 'Это красный текст')
print(Fore.GREEN + 'Это зеленый текст')
print(Fore.BLUE + 'Это синий текст')

print(Back.YELLOW + 'Это текст на желтом фоне')
print(Back.CYAN + 'Это текст на голубом фоне')
print(Fore.WHITE + Back.BLUE + 'Белый текст на синем фоне')