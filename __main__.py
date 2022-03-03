import argparse

repka_logo = '''
               ░░░░
       ░░░░  ░░▓▓▓▓░░  ░░░░
       ░░▓▓░░░░▓▓▓▓░░░░▓▓░░
         ░░▓▓░░▓▓▓▓░░▓▓░░
           ░░▓▓▓▓▓▓▓▓░░
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
   ▒▒████████████████████████▒▒
 ▒▒████████████████████████████▒▒
 ▒▒██████▒▒▒▒████████▒▒▒▒██████▒▒
 ▒▒████▒▒████▒▒████▒▒████▒▒████▒▒
 ▒▒████████████████████████████▒▒
   ▒▒█████████▒████▒█████████▒▒
     ▒▒▒▒██████▒▒▒▒██████▒▒▒▒
         ▒▒▒▒████████▒▒▒▒
             ▒▒████▒▒
               ▒▒▒▒
                ▒▒
 _____  _____  _____  __ ___ _____ 
/  _  \/   __\/  _  \|  |  //  _  \\
|  _  <|   __||   __/|  _ < |  _  |
\__|\_/\_____/\__/   |__|__\\\\__|__/
'''

parser = argparse.ArgumentParser(description="A tool for open-source software version detection by its repository.")
parser.add_argument('-u', '--uri', help='URI of the target', required=True)
parser.add_argument('-p', '--path', help='path to the local copy of the repository', required=True)
parser.add_argument('-f', '--folder', help='repository folder with files to compare with')
parser.add_argument('-e', '--extensions', help='file extensions. example: html,css,js')

print("\033[92m {}\033[00m" .format('\n'.join(repka_logo.split('\n')[:6])))
print("\033[93m {}\033[00m" .format('\n'.join(repka_logo.split('\n')[6:18])))
print('\n'.join(repka_logo.split('\n')[18:]))

args = parser.parse_args()
print(args)

extensions = []

if args.extensions != None:
    extensions = args.extensions.split(',')
    print(extensions)