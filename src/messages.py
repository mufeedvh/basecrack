from termcolor import colored

def print_line_separator():
    print(
        colored('\n{{<<', 'red') +
        colored('='*70, 'yellow') +
        colored('>>}}', 'red')
    )

def push_error(message):
    print(colored('\n[!] {}\n'.format(message), 'red'))