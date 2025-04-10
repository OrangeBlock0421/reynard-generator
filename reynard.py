#   Reynard, a character generator script.
#   Copyright (C) 2025  CosmicJester
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#   To contact via email: throwaway64290@gmail.com

import os
from pathlib import Path
import pickle
import sys

persdb = {}

def firstRun():
    hasRun = {'key': 'hasRunBefore', 'value': 'true'}
    persdb['hasRunBefore'] = hasRun
    return persdb

match os.name:
    case 'nt':
        perspath = f'{os.getenv('LOCALAPPDATA')}{os.sep}CosmicJester{os.sep}Persist{os.sep}Reynard{os.sep}'
    case _:
        perspath = f'~{os.sep}.cosmicjester{os.sep}persist{os.sep}reynard{os.sep}'

def loadData(data):
    try:
        match data:
            case 'firstrun':
                persDBFile = open(f'{perspath}reynardFirstRun', 'rb')
                hasRun = pickle.load(persDBFile)
                for keys in hasRun:
                    runDB = hasRun[keys]
                persDBFile.close()
                return runDB['value']
            case 'dateformat':
                formatDBFile = open(f'{perspath}reynardDateFormat', 'rb')
                dateFormat = pickle.load(formatDBFile)
                for keys in dateFormat:
                    formDB = dateFormat[keys]
                formatDBFile.close()
                return formDB['value']
    except:
        return 'false'

import kit # Import Kit, my functions module. Contains everything from kit_rey (the mini version of this script's function file) since these have been merged.
import vixen # Import Vixen, my variables module.

filepres = Path('./output.txt')

bool_map = {"1": True, "true": True, "yes": True, "y": True, "0": False, "false": False, "no": False, "n": False}

class strlin:
    KEYINT = 'Goodbye! (quit called by KeyboardInterrupt)'
    GENEXT = 'Goodbye!'

# Hey hey hey, folks! This is my goofy, funky, really fuckin' cool main generator script! I'm losing my mental sanity!
match loadData('firstrun'):
    case 'false':
        print(f'Reynard  Copyright (C) 2025  CosmicJester\nThis program comes with ABSOLUTELY NO WARRANTY; for details type \'show w\'.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions; type \'show c\' for details.\n')
        print(f'To preface: All inputs must be typed to the letter, but are case insensitive. There\'s no error correction here yet, and probably never will be.\nQuestions with broader answer examples aren\'t limited to exactly what\'s shown, but aren\'t set up to handle input other than what\'s directly allowed.\nDate of birth is set up with the base point of December 31, 2024.\nIf you\'re able to, just take a look at the input switches to see what you can and can\'t pass.\nThis is just a notice, and will only show up on the first run per user account.\n(Persistent data is stored in "{perspath}".)\n')
        try:
            persDBFile = open(f'{perspath}reynardFirstRun', 'ab')
        except FileNotFoundError:
            os.makedirs(perspath, exist_ok=True)
            persDBFile = open(f'{perspath}reynardFirstRun', 'xb')
            persDBFile.close()
            persDBFile = open(f'{perspath}reynardFirstRun', 'ab')
        persdb = firstRun()
        pickle.dump(persdb, persDBFile)
        persDBFile.close()

outfile = open('output.txt','w')
try:
    match sys.argv[1]:
        case '-r'|'--reset':
            try:
                os.remove(f'{perspath}reynardFirstRun')
            except:
                print('Could not remove FirstRun file.')
            else:
                print('Successfully removed FirstRun file! Notice will show on next run.')
            try:
                os.remove(f'{perspath}reynardDateFormat')
            except:
                print('Could not remove DateFormat file.')
            else:
                print('Successfully removed DateFormat file! Format will need to be manually reset.')
            quit(0)
except:
    try:
        while True:
            instantion = input('Reynard active! What are you here for?\n')
            match instantion.lower():
                case 'generate'|'gen'|'g':
                    break
                case 'df'|'format'|'dateformat'|'date format'|'date':
                    format_sel = input('Enter your preferred date format.\n')
                    returned_format = kit.dateFormatSwitch(format_sel.lower())
                    match returned_format.lower():
                        case 'invalid':
                            print('Invalid option passed.')
                        case _:
                            dateFormat = {'key': 'dateFormatSelected', 'value': returned_format.lower()}
                            formatpersdb = {}
                            formatpersdb['dateFormat'] = dateFormat
                            persDBFile = open(f'{perspath}reynardDateFormat', 'ab')
                            pickle.dump(formatpersdb, persDBFile)
                            persDBFile.close()
                case 'reset'|'res'|'r':
                    try:
                        os.remove(f'{perspath}reynardFirstRun')
                    except:
                        print('Failed to remove FirstRun file.')
                    else:
                        print('Successfully removed FirstRun file! Notice will show on next run.')
                    try:
                        os.remove(f'{perspath}reynardDateFormat')
                    except:
                        print('Failed to remove DateFormat file.')
                    else:
                        print('Successfully removed DateFormat file! Format will need to be manually reset.')
                    quit(0)
                case 'reset firstrun'|'res firstrun'|'r firstrun'|'reset run'|'res run'|'r run':
                    try:
                        os.remove(f'{perspath}reynardFirstRun')
                    except:
                        print('Failed to remove FirstRun file.')
                    else:
                        print('Successfully removed FirstRun file! Notice will show on next run.')
                    quit(0)
                case 'reset date'|'reset format'|'reset dateformat'|'res date'|'res format'|'res dateformat'|'r date'|'r format'|'r dateformat':
                    try:
                        os.remove(f'{perspath}reynardDateFormat')
                    except:
                        print('Failed to remove DateFormat file.')
                    else:
                        print('Successfully removed DateFormat file! Format will need to be manually reset.')
                    quit(0)
                case 'nevermind'|'quit'|'exit'|'q':
                    print(strlin.GENEXT)
                    quit(0)
                case 'show w':
                    print('\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\n')
                case 'show c':
                    print(f'\nThis program is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\n')
                case _:
                    print('Invalid option.')
                    continue
        while True:
            gen_type = input('What kind of generation (all or individual)?\n')
            match gen_type:
                case 'name'|'gender'|'species'|'age'|'race'|'all'|'everything'|'all of it'|'bulk':
                    break
                case 'nevermind'|'quit'|'exit':
                    print(strlin.GENEXT)
                    quit(0)
                case _:
                    print('Invalid option.')
                    continue
    except KeyboardInterrupt:
            print(strlin.KEYINT)
            quit(0)

# Because collectively, we can't get our shit in order and working.
# PYTHON. TELL ME WHY 'OUTPUT_TOFILE' IS UNBOUND. *TELL ME WHY.*
# IT'S A SIMPLE FUCKING BOOLEAN. WHY DO I NEED A FUNCTION TO DO YOUR JOB FOR YOU.

# There used to be a function here to set OUTPUT_TOFILE to True, because it kept throwing NameError. Turns out, the problem was that I didn't have the 'if' statement set it to False when the input said no. I'm leaving those comments there because one, funny, and two, it's historical.
## LMAO THE PROBLEM WASN'T THAT, IT WAS THE LACK OF DEFAULT VARIABLES :P
## I am very sanded brain, if you couldn't tell.
### AND THE FUNNIEST PART. I ditched that segment anyway.

# The situation: I stopped using OUTPUT_TOFILE and that method of picking output type because, as rey.py taught me, if you don't make it export, and you run the script from say, a self-contained EXE, you're physically incapable of doing anything with the output before the terminal closes. Instead of implementing a pause function, it just outputs automatically. Frankly, why wouldn't you want it to do that?

# age_gen used to be here because as is, I couldn't move it to Kit. But now I know how to define a function. :)
try:
    match gen_type.lower():
        case 'all'|'everything'|'all of it':
            while True:
                fur_allowed = input('First, are non-humans cool with you? (Yes or No)\n')
                match fur_allowed.lower():
                    case 'yes'|'1'|'true'|'y'|'no'|'0'|'false'|'n':
                        fur_bool = bool_map.get(fur_allowed.strip().lower(), True)
                        break
                    case 'nevermind'|'quit'|'exit':
                        print(strlin.GENEXT)
                        quit(0)
                    case _:
                        print('Yes or No, please.')
                        continue
            while True:
                chosen_age = input('Next, what age would you like? (Child, Teen, Adult, Elder, Immortal)\n')
                match chosen_age.lower():
                    case 'child'|'kid'|'teen'|'teenager'|'young'|'young adult'|'adult'|'old'|'elder'|'immortal'|'abnormal'|'inhuman':
                        break
                    case 'nevermind'|'quit'|'exit':
                        print(strlin.GENEXT)
                        quit(0)
                    case _:
                        print('Not a valid option.')
                        continue
            while True:
                nonstand_gender = input('Next, are you alright with non-binary gender options? (Yes or No)\n')
                match nonstand_gender.lower():
                    case 'yes'|'1'|'true'|'y'|'no'|'0'|'false'|'n':
                        gender_bool = bool_map.get(nonstand_gender.strip().lower(), True)
                        break
                    case 'nevermind'|'quit'|'exit':
                        print(strlin.GENEXT)
                        quit(0)
                    case _:
                        print('Yes or No, please.')
                        continue
            while True:
                unnatur_hair = input('Next, are you alright with unnatural hair colors (typically dyed)? (Yes or No)\n')
                match unnatur_hair.lower():
                    case 'yes'|'1'|'true'|'y'|'no'|'0'|'false'|'n':
                        haircolor_bool = bool_map.get(unnatur_hair.strip().lower(), True)
                        break
                    case 'nevermind'|'quit'|'exit':
                        print(strlin.GENEXT)
                        quit(0)
                    case _:
                        print('Yes or No, please.')
                        continue
            while True:
                chosen_template = input('Next, what format would you like? (Persona, Formatted, Full)\n')
                match chosen_template.lower():
                    case 'persona'|'formatted'|'full'|'blank persona'|'blank formatted'|'blank full':
                        break
                    case 'nevermind'|'quit'|'exit':
                        print(strlin.GENEXT)
                        quit(0)
                    case _:
                        print('Not a valid option.')
                        continue
            try:
                match chosen_template.lower():
                    case 'persona':
                        species_sel = kit.speciesGen(fur_bool)
                        match species_sel.lower():
                            case 'human'|'robot'|'demon'|'angel'|'shadow entity'|'elf':
                                skin_color = f'{kit.skinGen(fur_bool)} skin'
                            case _:
                                skin_color = f'{kit.furGen()} fur'
                        eye_color = f'{kit.eyeGen()} eyes'
                        hat_sel = kit.massGen('hat')
                        match hat_sel.lower():
                            case 'none':
                                hat_out = 'no hat'
                            case _:
                                hat_color_sel = kit.massGen('hatcolor')
                                hat_size_sel = kit.massGen('hatsize')
                                hat_out = f'a {hat_size_sel.lower()} {hat_color_sel.lower()} {hat_sel.lower()}'
                        gender_sel = kit.genderGen(gender_bool)
                        match gender_sel.lower():
                            case 'male'|'trans male':
                                genduh = 'masc'
                            case 'female'|'trans female':
                                genduh = 'fem'
                            case 'what\'re you, a cop? fuck off. (androgynous)'|'trans what\'re you, a cop? fuck off. (androgynous)', 'non-binary what\'re you, a cop? fuck off. (androgynous)', 'non-binary male', 'non-binary female':
                                genduh = 'andro'
                            case _:
                                print(f'{vixen.tc.FAIL}Something has gone terribly wrong. Terminating...')
                                print('Something has gone terribly wrong, and the script has terminated.', file=outfile)
                                quit(1)
                        top_sel = kit.massGen('top')
                        outtop_sel = kit.massGen('outertop')
                        match outtop_sel.lower():
                            case 'none':
                                top_out = f'a {str.lower(kit.massGen('topcolor'))} {top_sel.lower()}'
                            case _:
                                top_out = f'a {str.lower(kit.massGen('topcolor'))} {top_sel.lower()}, a {str.lower(kit.massGen('outertopcolor'))} {outtop_sel.lower()}'
                        kit.clear_screen() # Clear thy screen!
                        print(f'''Name: {kit.nameGen('both',genduh)}
Aliases: None
Gender: {gender_sel}
Species: {str(species_sel)}
Age: {str(kit.ageGen(chosen_age))}
Appearance: {kit.heightGen()}, {skin_color}, {str.lower(eye_color)}, wears {top_out.lower()}, {str.lower(kit.massGen('bottomcolor'))} {str.lower(kit.massGen('bottom'))}, {str.lower(kit.massGen('sockcolor'))} {str.lower(kit.massGen('sock'))}, {str.lower(kit.massGen('shoecolor'))} {str.lower(kit.massGen('shoe'))}, and {hat_out}
Skills: {kit.skillGen()}
Abilities: Temporarily replaced
Personality: {kit.personalityGen()} (Note, if you get a conflict, just remove it, don't have error correction set up yet)
Background: {str(kit.massGen('nationality'))}.''', file=outfile)
                            # This entire section used to please the italians. But now it's split off to the segment above!
                    case 'formatted':
                        species_sel = kit.speciesGen(fur_bool)
                        match species_sel.lower():
                            case 'human'|'robot'|'demon'|'angel'|'shadow entity'|'elf':
                                skin_color = f'Skin Color: {kit.skinGen(fur_bool)}'
                            case _:
                                skin_color = f'Fur Color: {kit.furGen()}'
                        eye_color = f'{kit.eyeGen()}'
                        gender_sel = kit.genderGen(gender_bool)
                        match gender_sel.lower():
                            case 'male'|'trans male':
                                genduh = 'masc'
                            case 'female'|'trans female':
                                genduh = 'fem'
                            case 'what\'re you, a cop? fuck off. (androgynous)'|'trans what\'re you, a cop? fuck off. (androgynous)', 'non-binary what\'re you, a cop? fuck off. (androgynous)', 'non-binary male', 'non-binary female':
                                genduh = 'andro'
                            case _:
                                print(f'{vixen.tc.FAIL}Something has gone terribly wrong. Terminating...')
                                print('Something has gone terribly wrong, and the script has terminated.', file=outfile)
                                quit(1)
                        top_sel = kit.massGen('top')
                        outtop_sel = kit.massGen('outertop')
                        match outtop_sel.lower():
                            case 'none':
                                top_out = f'{kit.massGen('topcolor')} {top_sel}'
                            case _:
                                top_out = f'{kit.massGen('topcolor')} {top_sel}, {kit.massGen('topcolor')} {outtop_sel}'
                        hat_sel = kit.massGen('hat')
                        match hat_sel.lower():
                            case 'none':
                                hat_out = 'No Hat'
                            case _:
                                hat_color_sel = kit.massGen('hatcolor')
                                hat_size_sel = kit.massGen('hatsize')
                                hat_out = f'{hat_size_sel} {hat_color_sel} {hat_sel}'
                        print(f'''Name: {kit.nameGen('both',genduh)}
Aliases: None
Species: {species_sel}
Date of Birth: {kit.birthDateGen(chosen_age.lower(),loadData('dateformat'))}
Gender: {gender_sel}
Sexuality: {kit.massGen('sexuality')}
Occupation: No Table
Nationality: {kit.massGen('nationality')}
{skin_color}
Hair Color: {kit.hairGen(haircolor_bool)}
Hair Style: {kit.massGen('hairstyle')}
Eye Color: {eye_color}
Height: {kit.heightGen()}
Clothes: {top_out}, {kit.massGen('bottomcolor')} {kit.massGen('bottom')}, {kit.massGen('sockcolor')} {kit.massGen('sock')}, {kit.massGen('shoecolor')} {kit.massGen('shoe')}, {hat_out}
Abilities: Temporarily replaced
Skills: {kit.skillGen()}
Personality: {kit.personalityGen()} (Note, if you get a conflict, just remove it, don't have error correction set up yet)
Likes: No Table
Dislikes: No Table
Medical History: Manually
Username: Manually
Backstory: Manually
Relationships: Manually
Misc. Info: Manually''',file=outfile)
                    case 'full':
                        species_sel = kit.speciesGen(fur_bool)
                        match species_sel.lower():
                            case 'human'|'robot'|'demon'|'angel'|'shadow entity'|'elf':
                                skin_color = f'Skin Color: {kit.skinGen(fur_bool)}'
                            case _:
                                skin_color = f'Fur Color: {kit.furGen()}'
                        eye_color = f'{kit.eyeGen()}'
                        gender_sel = kit.genderGen(gender_bool)
                        match gender_sel.lower():
                            case 'male'|'trans male':
                                genduh = 'masc'
                            case 'female'|'trans female':
                                genduh = 'fem'
                            case 'what\'re you, a cop? fuck off. (androgynous)'|'trans what\'re you, a cop? fuck off. (androgynous)', 'non-binary what\'re you, a cop? fuck off. (androgynous)', 'non-binary male', 'non-binary female':
                                genduh = 'andro'
                            case _:
                                print(f'{vixen.tc.FAIL}Something has gone terribly wrong. Terminating...')
                                print('Something has gone terribly wrong, and the script has terminated.', file=outfile)
                                quit(1)
                        top_sel = kit.massGen('top')
                        outtop_sel = kit.massGen('outertop')
                        match outtop_sel.lower():
                            case 'none':
                                top_out = f'{kit.massGen('topcolor')} {top_sel}'
                            case _:
                                top_out = f'{kit.massGen('topcolor')} {top_sel}, {kit.massGen('outertopcolor')} {outtop_sel}'
                        hat_sel = kit.massGen('hat')
                        match hat_sel.lower():
                            case 'none':
                                hat_out = 'No Hat'
                            case _:
                                hat_color_sel = kit.massGen('hatcolor')
                                hat_size_sel = kit.massGen('hatsize')
                                hat_out = f'{hat_size_sel} {hat_color_sel} {hat_sel}'
                        print(f'''Name: {kit.nameGen('both',genduh)}
Aliases: None
Species: {species_sel}
Date of Birth: {kit.birthDateGen(chosen_age.lower(),loadData('dateformat'))}
Gender: {gender_sel}
Sexuality: {kit.massGen('sexuality')}
Occupation: No Table
Nationality: {kit.massGen('nationality')}
{skin_color}
Hair Color: {kit.hairGen(haircolor_bool)}
Hair Style: {kit.massGen('hairstyle')}
Eye Color: {eye_color}
Height: {kit.heightGen()}
Head: {hat_out}
Top: {top_out}
Bottom: {kit.massGen('bottomcolor')} {kit.massGen('bottom')}
Feet: {kit.massGen('shoecolor')} {kit.massGen('shoe')}
Hands: No Table
Abilities: Temporarily replaced
Skills: {kit.skillGen()}
Personality: {kit.personalityGen()} (Note, if you get a conflict, just remove it, don't have error correction set up yet)
Likes: No Table
Dislikes: No Table
Medical History: Manually
Username: Manually
Backstory: Manually
Relationships: Manually
Misc. Info: Manually''', file=outfile)
                    case 'blank persona':
                        print(f'''Name: 
Aliases: 
Gender: 
Species: 
Age: 
Appearance: 
Skills: 
Abilities: 
Personality: 
Background:''',file=outfile)
                    case 'blank formatted':
                        print(f'''Name: 
Aliases: 
Species: 
Date of Birth: 
Gender: 
Sexuality: 
Occupation: 
Nationality: 
Fur Color: 
Hair Color: 
Hair Style: 
Eye Color: 
Height: 
Clothes: 
Abilities: 
Skills: 
Personality: 
Likes: 
Dislikes: 
Medical History: 
Username: 
Backstory: 
Relationships: 
Misc. Info: ''',file=outfile)
                    case 'blank full':
                        print(f'''Name: 
Aliases: 
Species: 
Date of Birth: 
Gender: 
Sexuality: 
Occupation: 
Nationality: 
Fur Color: 
Hair Color: 
Hair Stule: 
Eye Color: 
Height: 
Head: 
Top: 
Bottom: 
Feet: 
Hands: 
Abilities: 
Skills: 
Personality: 
Likes: 
Dislikes: 
Medical History: 
Username: 
Backstory: 
Relationships: 
Misc. Info: ''', file=outfile)
            except vixen.InvalidGenOption:
                print(f'Generation failed ({str(vixen.InvalidGenOption.message)}) ')
        case 'name':
            oneortwo = input("First, last, or both?\n")
            match oneortwo:
                case '1'|'one'|'first'|'3'|'three'|'both': # If you aren't asking for just a last name
                    genduh = input("What gender (masc, fem, andro, any)?\n") # It prompts for gender input
                case '2'|'two'|'last':
                    genduh = "fem" # Otherwise, you're a woman
                case _:
                    genduh = "fem"
            reso = str(kit.reyNameGen(oneortwo, genduh))
            print(reso,file=outfile)
        case 'gender':
            nons = input("Non-standard options (non-binary, trans)?\n")
            reso = kit.reyGenderGen(nons)
            print(reso, file=outfile)
        case 'species'|'race':
            while True:
                furpillow = input("Furries or no?\n")
                match str(furpillow.lower()):
                    case 'yes'|'no':
                        break
                    case 'woof'|'bark'|'meow'|'mreow'|'marp'|'mrrp'|'arf'|'mow':
                        print("Alright, fair enough response.")
                        furpillow = 'yes'
                        break
                    case _:
                        print("Yes or no question, my man.")
                        continue
            reso = kit.reySpecGen(furpillow)
            print(reso, file=outfile)
        case 'age':
            ageran = input("What range?\n(Immortality/abnormal is permitted.)\n")
            reso = kit.reyAgeGen(ageran)
            print(reso, file=outfile)
        case 'bulk':
            while True:
                manno = input("Of what?\n")
                match manno.lower():
                    case 'quit':
                        quit(0)
                    case 'name':
                        reygenset = input("What kind?\n")
                        match reygenset.lower():
                            case '1'|'first'|'one'|'three'|'3'|'both':
                                reygen = input("What gender?\n")
                            case '2'|'last'|'two':
                                reygen = 'fem'
                            case _:
                                reygen = 'fem'
                        break
                    case 'gender':
                        reynonstand = input("Non-standard allowed?\n")
                        break
                    case 'species':
                        reynonspec = input("Furries allowed?\n")
                        break
                    case _:
                        print("Can't do that one, try again. (Hint, the table's smaller here!)")
                        continue
            manny = input("How many generations?\n")
            manni = 0
            outpow = []
            match manno.lower():
                case 'name':
                    while manni != int(manny):
                        outpow.append(kit.reyNameGen(reygenset,reygen))
                        manni += 1
                case 'gender':
                    while manni != int(manny):
                        outpow.append(kit.reyGenderGen(reynonstand))
                        manni += 1
                case 'species':
                    while manni != int(manny):
                        outpow.append(kit.reySpecGen(reynonspec))
                        manni += 1
                case _:
                    print('We\'re severely lacking an option to pass.', file=outfile)
            print('\n'.join(outpow), file=outfile)
except KeyboardInterrupt:
    print(strlin.KEYINT)
    quit(0)