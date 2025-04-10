"""Function scripts for Reynard."""
from random import randrange # love me my pseudo-random numbers
import os # CLEAR THE TEXT, BOSS

import vixen # we need the variables, they important

class tc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def genderGen(nonstand):
    match nonstand:
        case True:
            gendernum = randrange(0, vixen.GENDER_MAX)
            gendersuf = randrange(0, vixen.GENDER_SUFFIX_MAX)
            match gendersuf:
                case 8|9:
                    return f"{vixen.gender_suffixes[gendersuf]} {vixen.genders[gendernum]}"
                case _:
                    return f"{vixen.genders[gendernum]}"
        case False:
            return vixen.genders[randrange(0, 2)]

def nameGen(type,gender):
    match type:
        case 'first':
            match gender:
                case 'fem':
                    return str(vixen.fem_names[randrange(0,vixen.FEM_NAMES_MAX)])
                case 'masc':
                    return str(vixen.masc_names[randrange(0,vixen.MASC_NAMES_MAX)])
                case 'andro':
                    return str(vixen.andro_names[randrange(0,vixen.ANDRO_NAMES_MAX)])
                case _:
                    return "Failed"
        case 'last':
            return str(vixen.last_names[randrange(0,vixen.LAST_NAMES_MAX)])
        case 'both':
            match gender:
                case 'fem':
                    return f'{str(vixen.fem_names[randrange(0,vixen.FEM_NAMES_MAX)])} {str(vixen.last_names[randrange(0,vixen.LAST_NAMES_MAX)])}'
                case 'masc':
                    return f'{str(vixen.masc_names[randrange(0,vixen.MASC_NAMES_MAX)])} {str(vixen.last_names[randrange(0,vixen.LAST_NAMES_MAX)])}'
                case 'andro':
                    return f'{str(vixen.andro_names[randrange(0,vixen.ANDRO_NAMES_MAX)])} {str(vixen.last_names[randrange(0,vixen.LAST_NAMES_MAX)])}'
                case _:
                    return "Failed"
        case _:
            return "Failed"

def eyeGen():
    eye_color_num = randrange(0,vixen.EYE_COLORS_MAX)
    match eye_color_num:
        case vixen.EYE_COLORS_MAX:
            eye_1 = randrange(0,vixen.EYE_COLORS_MAX)
            eye_2 = randrange(0,vixen.EYE_COLORS_MAX)
            while eye_1 == eye_2:
                eye_2 = randrange(0,vixen.EYE_COLORS_MAX)
            return f'{str(vixen.eye_colors[eye_1])} Left and {str(vixen.eye_colors[eye_2])} Right'
        case _:
            return vixen.eye_colors[eye_color_num]

def hairGen(unnatur):
    match unnatur:
        case True:
            hair_color_num = randrange(0,vixen.FUR_COLORS_MAX)
            match hair_color_num:
                case vixen.FUR_COLORS_MAX:
                    hairc1 = randrange(0,vixen.FUR_COLORS_MAXLESS)
                    hairc2 = randrange(0,vixen.FUR_COLORS_MAXLESS)
                    while hairc2 == hairc1:
                        hairc2 = randrange(0,vixen.FUR_COLORS_MAXLESS)
                    return f'{vixen.fur_colors[hairc1]} and {vixen.fur_colors[hairc2]}'
                case _:
                    return f'{vixen.fur_colors[hair_color_num]}'
        case False:
            return f'{vixen.natural_hair_colors[randrange(0,vixen.NATURAL_HAIR_COLORS_MAX)]}'

def skinGen(nonstand):
    match nonstand:
        case True:
            skin_color_num = randrange(0,vixen.SKIN_COLORS_MAX)
            match skin_color_num:
                case vixen.SKIN_COLORS_MAX:
                    return vixen.fur_colors[randrange(0,vixen.FUR_COLORS_MAXLESS)]
                case _:
                    return vixen.skin_colors[skin_color_num]
        case False:
            return vixen.skin_colors[randrange(0,vixen.SKIN_COLORS_STANDMAX)]
        case _:
            return vixen.skin_colors[randrange(0,vixen.SKIN_COLORS_STANDMAX)]

def heightGen():
    hf = randrange(4,7)
    hi = randrange(0,11)
    return f'{hf}\'{hi}"'

def furGen():
    fur_color_num = randrange(0,vixen.FUR_COLORS_MAX)
    match fur_color_num:
        case vixen.FUR_COLORS_MAX:
            fur_col_1 = randrange(0,vixen.FUR_COLORS_MAXLESS)
            fur_col_2 = randrange(0,vixen.FUR_COLORS_MAXLESS)
            while fur_col_1 is fur_col_2:
                fur_col_2 = randrange(0,vixen.FUR_COLORS_MAX - 1)
            return f'{str(vixen.fur_colors[fur_col_1])} and {str(vixen.fur_colors[fur_col_2])}'
        case _:
            return vixen.fur_colors[fur_color_num]

def massGen(which):
    match which:
        case 'sexuality':
            return str(vixen.sexualities[randrange(0,vixen.SEXUALITIES_MAX)])
        case 'hat':
            return vixen.hats[randrange(0,vixen.HAT_MAX)]
        case 'hatcolor':
            return vixen.hat_colors[randrange(0,vixen.HAT_COLOR_MAX)]
        case 'hatsize':
            return vixen.cloth_sizes[randrange(0,vixen.SIZE_MAX)]
        case 'nationality':
            return vixen.nationalities[randrange(0,vixen.NATIONALITIES_MAX)]
        case 'top':
            return vixen.tops[randrange(0,vixen.TOP_MAX)]
        case 'topcolor':
            return str(vixen.top_colors[randrange(0,vixen.TOP_COLOR_MAX)])
        case 'outertop':
            return f'{vixen.out_tops[randrange(0,vixen.OUT_TOP_MAX)]}'
        case 'outertopcolor':
            return f'{vixen.top_colors[randrange(0,vixen.TOP_COLOR_MAX)]}'
        case 'bottom':
            return str(vixen.bottoms[randrange(0,vixen.BOTTOM_MAX)])
        case 'bottomcolor':
            return str(vixen.bottom_colors[randrange(0,vixen.BOTTOM_COLOR_MAX)])
        case 'sock':
            return str(vixen.socks[randrange(0,vixen.SOCKS_MAX)])
        case 'sockcolor':
            return str(vixen.bottom_colors[randrange(0,vixen.BOTTOM_COLOR_MAX)])
        case 'shoe':
            return str(vixen.shoes[randrange(0,vixen.SHOE_MAX)])
        case 'shoecolor':
            return str(vixen.shoe_colors[randrange(0,vixen.SHOE_COLOR_MAX)])
        case 'hairstyle':
            return f'{vixen.hair_styles[randrange(0,vixen.HAIR_STYLES_MAX)]}'
        case _:
            raise vixen.InvalidGenOption('massGen() was given an invalid option.')

def ageGen(rang):
    match rang:
        case 'child'|'kid':
            return str(randrange(8,12))
        case 'teen'|'teenager':
            return str(randrange(13,17))
        case 'young':
            return str(randrange(8,17))
        case 'young adult':
            return str(randrange(18,35))
        case 'adult':
            return str(randrange(36,64))
        case 'old'|'elder':
            return str(randrange(65,120))
        case 'immortal'|'abnormal'|'inhuman':
            return str(randrange(18,500))
        case _:
            return str(randrange(8,120))

def speciesGen(furbro):
    match furbro:
        case True:
            specnum = randrange(0, vixen.SPECIES_MAX)
            match specnum:
                case 0:    
                    specnum1 = randrange(0, vixen.SPECIES_MAX)
                    while specnum1 == 0:
                        specnum1 = randrange(1, vixen.SPECIES_MAX)
                    if specnum1 == 3:
                        return "Robot"
                    else:
                        return f"Robot {vixen.species[specnum1]}"
                case 1:
                    specnum1 = randrange(0, vixen.SPECIES_MAX)
                    while specnum1 == 1:
                        specnum1 = randrange(0, vixen.SPECIES_MAX)
                    if specnum1 == 3:
                        return "Angel"
                    else:
                        return f"{vixen.species[specnum1]} Angel"
                case 2:
                    specnum1 = randrange(0, vixen.SPECIES_MAX)
                    while specnum1 == 2:
                        specnum1 = randrange(0, vixen.SPECIES_MAX)
                    if specnum1 == 3:
                        return "Demon"
                    else:
                        return f"{vixen.species[specnum1]} Demon"
                case 4:
                    specnum1 = randrange(5, vixen.SPECIES_MAX)
                    specnum2 = randrange(5, vixen.SPECIES_MAX)
                    while specnum1 == specnum2:
                        specnum2 = randrange(5, vixen.SPECIES_MAX)
                    return f"{vixen.species[specnum1]} {vixen.species[specnum2]} Hybrid"
                case _:
                    return vixen.species[specnum]
        case False:
            specnum = randrange(0, 12)
            match specnum:
                case 0:
                    return "Robot"
                case 1:
                    return "Angel"
                case 2:
                    return "Demon"
                case _:
                    return "Human"
        case _:
            print(vixen.tc.FAIL + 'Whuh?' + vixen.tc.ENDC)
            return f'{vixen.tc.FAIL}Whuh?{vixen.tc.ENDC}'

def dateFormatSwitch(format):
    match format.lower():
        case 'mm/dd/yyyy'|'m/d/yy'|'mm/dd/yy'|'m/d/yyyy':
            return 'mm/dd/yyyy'
        case 'dd/mm/yyyy'|'d/m/yy'|'dd/mm/yy'|'d/m/yyyy':
            return 'dd/mm/yyyy'
        case 'yyyy/mm/dd'|'yy/m/d'|'yy/mm/dd'|'yyyy/m/d':
            return 'yyyy/mm/dd'
        case 'yyyy/dd/mm'|'yy/d/m'|'yy/dd/mm'|'yyyy/d/m':
            return 'yyyy/dd/mm'
        case _:
            return 'invalid'
        
def birthDateGen(rang,format):
    month = randrange(1,12)
    match month:
        case 2:
            day = randrange(1,28)
        case 1|3|5|7|8|10|12:
            day = randrange(1,31)
        case _:
            day = randrange(1,30)
    match rang.lower():
        case 'child'|'kid':
            year = randrange(2012,2016)
        case 'teen'|'teenager':
            year = randrange(2007,2011)
        case 'young':
            year = randrange(2007,2016)
        case 'young adult':
            year = randrange(1989,2006)
        case 'adult':
            year = randrange(1960,1988)
        case 'old'|'elder':
            year = randrange(1904,1959)
        case 'immortal'|'abnormal'|'inhuman':
            year = randrange(1524,2006)
        case _:
            year = randrange(1904,2016)
    match str.lower(format):
        case 'mm/dd/yyyy':
            return f'{str(month)}/{str(day)}/{str(year)}'
        case 'dd/mm/yyyy':
            return f'{str(day)}/{str(month)}/{str(year)}'
        case 'yyyy/mm/dd':
            return f'{str(year)}/{str(month)}/{str(day)}'
        case 'yyyy/dd/mm':
            return f'{str(year)}/{str(day)}/{str(month)}'
        case _:
            raise vixen.InvalidFormatError('Date not in format range.')

# def magicLevel(abil):
#    match abil:
#        case 0:
#            maglev = randrange(0,vixen.MAGIC_SKILL_CAP)
#            return str(vixen.magic_skill[maglev])
#        case _:
#            return str(vixen.abilities[abil])

# def abilityGen():
#    numberOf = randrange(1,8)
#    match numberOf:
#        case 1:
#            abil1 = randrange(0,vixen.ABILITY_MAX)
#            bility1 = magicLevel(abil1)
#            return f'{bility1}'
#        case 2:
#            abil1 = randrange(0,vixen.ABILITY_MAX)
#            abil2 = randrange(0,vixen.ABILITY_MAX)
#            while abil1 == abil2:
#                abil1 = randrange(0,vixen.ABILITY_MAX)
#            while abil2 == abil1:
#                abil2 = randrange(0,vixen.ABILITY_MAX)
#            bility1 = magicLevel(abil1)
#            bility2 = magicLevel(abil2)
#            return f'{bility1}, {bility2}'
#        case 3:
#            abil1 = randrange(0,vixen.ABILITY_MAX)
#            abil2 = randrange(0,vixen.ABILITY_MAX)
#            abil3 = randrange(0,vixen.ABILITY_MAX)
#            while abil1 == abil2|abil3:
#                abil1 = randrange(0,vixen.ABILITY_MAX)
#            while abil2 == abil1|abil3:
#                abil2 = randrange(0,vixen.ABILITY_MAX)
#            while abil3 == abil1|abil2:
#                abil3 = randrange(0,vixen.ABILITY_MAX)
#            bility1 = magicLevel(abil1)
#            bility2 = magicLevel(abil2)
#            bility3 = magicLevel(abil3)
#            return f'{bility1}, {bility2}, {bility3}'
#        case 4:
#            abil1 = randrange(0,vixen.ABILITY_MAX)
#            abil2 = randrange(0,vixen.ABILITY_MAX)
#            abil3 = randrange(0,vixen.ABILITY_MAX)
#            abil4 = randrange(0,vixen.ABILITY_MAX)
#            while abil1 == abil2|abil3|abil4:
#                abil1 = randrange(0,vixen.ABILITY_MAX)
#            while abil2 == abil1|abil3|abil4:
#                abil2 = randrange(0,vixen.ABILITY_MAX)
#            while abil3 == abil1|abil2|abil4:
#                abil3 = randrange(0,vixen.ABILITY_MAX)
#            while abil4 == abil1|abil2|abil3:
#                abil4 = randrange(0,vixen.ABILITY_MAX)
#            bility1 = magicLevel(abil1)
#            bility2 = magicLevel(abil2)
#            bility3 = magicLevel(abil3)
#            bility4 = magicLevel(abil4)
#            return f'{bility1}, {bility2}, {bility3}, {bility4}'
#        case 5:
#            abil1 = randrange(0,vixen.ABILITY_MAX)
#            abil2 = randrange(0,vixen.ABILITY_MAX)
#            abil3 = randrange(0,vixen.ABILITY_MAX)
#            abil4 = randrange(0,vixen.ABILITY_MAX)
#            abil5 = randrange(0,vixen.ABILITY_MAX)
#            while abil1 == abil2|abil3|abil4|abil5:
#                abil1 = randrange(0,vixen.ABILITY_MAX)
#            while abil2 == abil1|abil3|abil4|abil5:
#                abil2 = randrange(0,vixen.ABILITY_MAX)
#            while abil3 == abil1|abil2|abil4|abil5:
#                abil3 = randrange(0,vixen.ABILITY_MAX)
#            while abil4 == abil1|abil2|abil3|abil5:
#                abil4 = randrange(0,vixen.ABILITY_MAX)
#            while abil5 == abil1|abil2|abil3|abil4:
#                abil5 = randrange(0,vixen.ABILITY_MAX)
#            bility1 = magicLevel(abil1)
#            bility2 = magicLevel(abil2)
#            bility3 = magicLevel(abil3)
#            bility4 = magicLevel(abil4)
#            bility5 = magicLevel(abil5)
#            return f'{bility1}, {bility2}, {bility3}, {bility4}, {bility5}'
#        case 6:
#            abil1 = randrange(0,vixen.ABILITY_MAX)
#            abil2 = randrange(0,vixen.ABILITY_MAX)
#            abil3 = randrange(0,vixen.ABILITY_MAX)
#            abil4 = randrange(0,vixen.ABILITY_MAX)
#            abil5 = randrange(0,vixen.ABILITY_MAX)
#            abil6 = randrange(0,vixen.ABILITY_MAX)
#            while abil1 == abil2|abil3|abil4|abil5|abil6:
#                abil1 = randrange(0,vixen.ABILITY_MAX)
#            while abil2 == abil1|abil3|abil4|abil5|abil6:
#                abil2 = randrange(0,vixen.ABILITY_MAX)
#            while abil3 == abil1|abil2|abil4|abil5|abil6:
#                abil3 = randrange(0,vixen.ABILITY_MAX)
#            while abil4 == abil1|abil2|abil3|abil5|abil6:
#                abil4 = randrange(0,vixen.ABILITY_MAX)
#            while abil5 == abil1|abil2|abil3|abil4|abil6:
#                abil5 = randrange(0,vixen.ABILITY_MAX)
#            while abil6 == abil1|abil2|abil3|abil4|abil5:
#                abil6 = randrange(0,vixen.ABILITY_MAX)
#            bility1 = magicLevel(abil1)
#            bility2 = magicLevel(abil2)
#            bility3 = magicLevel(abil3)
#            bility4 = magicLevel(abil4)
#            bility5 = magicLevel(abil5)
#            bility6 = magicLevel(abil6)
#            return f'{bility1}, {bility2}, {bility3}, {bility4}, {bility5}, {bility6}'
#        case 7:
#            abil1 = randrange(0,vixen.ABILITY_MAX)
#            abil2 = randrange(0,vixen.ABILITY_MAX)
#            abil3 = randrange(0,vixen.ABILITY_MAX)
#            abil4 = randrange(0,vixen.ABILITY_MAX)
#            abil5 = randrange(0,vixen.ABILITY_MAX)
#            abil6 = randrange(0,vixen.ABILITY_MAX)
#            abil7 = randrange(0,vixen.ABILITY_MAX)
#            while abil1 == abil2|abil3|abil4|abil5|abil6|abil7:
#                abil1 = randrange(0,vixen.ABILITY_MAX)
#            while abil2 == abil1|abil3|abil4|abil5|abil6|abil7:
#                abil2 = randrange(0,vixen.ABILITY_MAX)
#            while abil3 == abil1|abil2|abil4|abil5|abil6|abil7:
#                abil3 = randrange(0,vixen.ABILITY_MAX)
#            while abil4 == abil1|abil2|abil3|abil5|abil6|abil7:
#                abil4 = randrange(0,vixen.ABILITY_MAX)
#            while abil5 == abil1|abil2|abil3|abil4|abil6|abil7:
#                abil5 = randrange(0,vixen.ABILITY_MAX)
#            while abil6 == abil1|abil2|abil3|abil4|abil5|abil7:
#                abil6 = randrange(0,vixen.ABILITY_MAX)
#            while abil7 == abil1|abil2|abil3|abil4|abil5|abil6:
#                abil7 = randrange(0,vixen.ABILITY_MAX)
#            bility1 = magicLevel(abil1)
#            bility2 = magicLevel(abil2)
#            bility3 = magicLevel(abil3)
#            bility4 = magicLevel(abil4)
#            bility5 = magicLevel(abil5)
#            bility6 = magicLevel(abil6)
#            bility7 = magicLevel(abil7)
#            return f'{bility1}, {bility2}, {bility3}, {bility4}, {bility5}, {bility6}, {bility7}'
#        case 8:
#            abil1 = randrange(0,vixen.ABILITY_MAX)
#            abil2 = randrange(0,vixen.ABILITY_MAX)
#            abil3 = randrange(0,vixen.ABILITY_MAX)
#            abil4 = randrange(0,vixen.ABILITY_MAX)
#            abil5 = randrange(0,vixen.ABILITY_MAX)
#            abil6 = randrange(0,vixen.ABILITY_MAX)
#            abil7 = randrange(0,vixen.ABILITY_MAX)
#            abil8 = randrange(0,vixen.ABILITY_MAX)
#            while abil1 == abil2|abil3|abil4|abil5|abil6|abil7|abil8:
#                abil1 = randrange(0,vixen.ABILITY_MAX)
#            while abil2 == abil1|abil3|abil4|abil5|abil6|abil7|abil8:
#                abil2 = randrange(0,vixen.ABILITY_MAX)
#            while abil3 == abil1|abil2|abil4|abil5|abil6|abil7|abil8:
#                abil3 = randrange(0,vixen.ABILITY_MAX)
#            while abil4 == abil1|abil2|abil3|abil5|abil6|abil7|abil8:
#                abil4 = randrange(0,vixen.ABILITY_MAX)
#            while abil5 == abil1|abil2|abil3|abil4|abil6|abil7|abil8:
#                abil5 = randrange(0,vixen.ABILITY_MAX)
#            while abil6 == abil1|abil2|abil3|abil4|abil5|abil7|abil8:
#                abil6 = randrange(0,vixen.ABILITY_MAX)
#            while abil7 == abil1|abil2|abil3|abil4|abil5|abil6|abil8:
#                abil7 = randrange(0,vixen.ABILITY_MAX)
#            while abil8 == abil1|abil2|abil3|abil4|abil5|abil6|abil7:
#                abil8 = randrange(0,vixen.ABILITY_MAX)
#            bility1 = magicLevel(abil1)
#            bility2 = magicLevel(abil2)
#            bility3 = magicLevel(abil3)
#            bility4 = magicLevel(abil4)
#            bility5 = magicLevel(abil5)
#            bility6 = magicLevel(abil6)
#            bility7 = magicLevel(abil7)
#            bility8 = magicLevel(abil8)
#            return f'{bility1}, {bility2}, {bility3}, {bility4}, {bility5}, {bility6}, {bility7}, {bility8}'
#        case _:
#            return 'Failed'

def skillGen():
    skillnum = randrange(0,5)
    match skillnum:
        case 0:
            return 'None'
        case 1:
            skillsel = randrange(0,vixen.SKILL_MAX)
            return f'{vixen.skills_landd[skillsel]}'
        case 2:
            skil1 = randrange(0,vixen.SKILL_MAX)
            skil2 = randrange(0,vixen.SKILL_MAX)
            while skil1 == skil2:
                skil1 = randrange(0,vixen.SKILL_MAX)
            kill1 = vixen.skills_landd[skil1]
            kill2 = vixen.skills_landd[skil2]
            return f'{kill1}, {kill2}'
        case 3:
            skil1 = randrange(0,vixen.SKILL_MAX)
            skil2 = randrange(0,vixen.SKILL_MAX)
            skil3 = randrange(0,vixen.SKILL_MAX)
            while skil1 == skil2|skil3:
                skil1 = randrange(0,vixen.SKILL_MAX)
            while skil2 == skil1|skil3:
                skil2 = randrange(0,vixen.SKILL_MAX)
            while skil3 == skil1|skil2:
                skil3 = randrange(0,vixen.SKILL_MAX)
            kill1 = vixen.skills_landd[skil1]
            kill2 = vixen.skills_landd[skil2]
            kill3 = vixen.skills_landd[skil3]
            return f'{kill1}, {kill2}, {kill3}'
        case 4:
            skil1 = randrange(0,vixen.SKILL_MAX)
            skil2 = randrange(0,vixen.SKILL_MAX)
            skil3 = randrange(0,vixen.SKILL_MAX)
            skil4 = randrange(0,vixen.SKILL_MAX)
            while skil1 == skil2|skil3|skil4:
                skil1 = randrange(0,vixen.SKILL_MAX)
            while skil2 == skil1|skil3|skil4:
                skil2 = randrange(0,vixen.SKILL_MAX)
            while skil3 == skil1|skil2|skil4:
                skil3 = randrange(0,vixen.SKILL_MAX)
            while skil4 == skil1|skil2|skil3:
                skil4 = randrange(0,vixen.SKILL_MAX)
            kill1 = vixen.skills_landd[skil1]
            kill2 = vixen.skills_landd[skil2]
            kill3 = vixen.skills_landd[skil3]
            kill4 = vixen.skills_landd[skil4]
            return f'{kill1}, {kill2}, {kill3}, {kill4}'
        case 5:
            skil1 = randrange(0,vixen.SKILL_MAX)
            skil2 = randrange(0,vixen.SKILL_MAX)
            skil3 = randrange(0,vixen.SKILL_MAX)
            skil4 = randrange(0,vixen.SKILL_MAX)
            skil5 = randrange(0,vixen.SKILL_MAX)
            while skil1 == skil2|skil3|skil4|skil5:
                skil1 = randrange(0,vixen.SKILL_MAX)
            while skil2 == skil1|skil3|skil4|skil5:
                skil2 = randrange(0,vixen.SKILL_MAX)
            while skil3 == skil1|skil2|skil4|skil5:
                skil3 = randrange(0,vixen.SKILL_MAX)
            while skil4 == skil1|skil2|skil3|skil5:
                skil4 = randrange(0,vixen.SKILL_MAX)
            while skil5 == skil1|skil2|skil3|skil4:
                skil5 = randrange(0,vixen.SKILL_MAX)
            kill1 = vixen.skills_landd[skil1]
            kill2 = vixen.skills_landd[skil2]
            kill3 = vixen.skills_landd[skil3]
            kill4 = vixen.skills_landd[skil4]
            kill5 = vixen.skills_landd[skil5]
            return f'{kill1}, {kill2}, {kill3}, {kill4}, {kill5}'
        case _:
            return 'Failed'

def personalityGen():
    personum = randrange(1,3)
    match personum:
        case 1:
            return f'{vixen.personality_traits[randrange(0,vixen.PERSONALITY_MAX)]}'
        case 2:
            perso1 = randrange(0,vixen.PERSONALITY_MAX)
            perso2 = randrange(0,vixen.PERSONALITY_MAX)
            while perso1 == perso2:
                perso1 = randrange(0,vixen.PERSONALITY_MAX)
            return f'{vixen.personality_traits[perso1]}, {vixen.personality_traits[perso2]}'
        case 3:
            perso1 = randrange(0,vixen.PERSONALITY_MAX)
            perso2 = randrange(0,vixen.PERSONALITY_MAX)
            perso3 = randrange(0,vixen.PERSONALITY_MAX)
            while perso1 == perso2|perso3:
                perso1 = randrange(0,vixen.PERSONALITY_MAX)
            while perso2 == perso1|perso3:
                perso2 = randrange(0,vixen.PERSONALITY_MAX)
            return f'{vixen.personality_traits[perso1]}, {vixen.personality_traits[perso2]}, {vixen.personality_traits[perso3]}'
        case _:
            return 'Failed'

def clear_screen():
    """Clears the terminal."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def reyNameGen(uod, gender):
    match uod:
        case "first"|"1"|"one":
            match gender:
                case 'male'|'masc'|'m':
                    return vixen.masc_names[randrange(0, vixen.MASC_NAMES_MAX)]
                case 'female'|'fem'|'f':
                    return vixen.fem_names[randrange(0, vixen.FEM_NAMES_MAX)]
                case 'non-binary'|'androgynous'|'andro'|'a'|'nb':
                    return vixen.andro_names[randrange(0, vixen.ANDRO_NAMES_MAX)]
                case 'either'|'4'|'any'|'it matters not':
                    gendough = randrange(0,2)
                    match gendough:
                        case 0:
                            return f"{vixen.masc_names[randrange(0, vixen.MASC_NAMES_MAX)]}"
                        case 1:
                            return f"{vixen.fem_names[randrange(0, vixen.FEM_NAMES_MAX)]}"
                        case 2:
                            return f"{vixen.andro_names[randrange(0, vixen.ANDRO_NAMES_MAX)]}"
                        case _:
                            print(f"{tc.FAIL}Something has gone terribly wrong. Terminating...")
                            print("Something has gone terribly wrong, and the script has terminated.", file=open('output_failed.txt','w'))
                            quit(1)
                            return
                case _:
                    print('For the record, this function requires SOMETHING to work with.')
                    return 'Not Provided'
        case 'last'|'2'|'two':
            return vixen.last_names[randrange(0, vixen.LAST_NAMES_MAX)]
        case 'both'|'3'|'three':
            lname_num = randrange(0, vixen.LAST_NAMES_MAX)
            match gender:
                case 'male'|'masc'|'m':
                    name_num = randrange(0, vixen.MASC_NAMES_MAX)
                    return f"{vixen.masc_names[name_num]} {vixen.last_names[lname_num]}"
                case 'female'|'fem'|'f':
                    name_num = randrange(0, vixen.FEM_NAMES_MAX)
                    return f"{vixen.fem_names[name_num]} {vixen.last_names[lname_num]}"
                case 'non-binary'|'androgynous'|'andro'|'a'|'nb':
                    name_num = randrange(0, vixen.ANDRO_NAMES_MAX)
                    return f"{vixen.andro_names[name_num]} {vixen.last_names[lname_num]}"
                case 'either'|'4'|'any'|'it matters not':
                    gendough = randrange(0,2)
                    match gendough:
                        case 0:
                            name_num = randrange(0, vixen.MASC_NAMES_MAX)
                            return f"{vixen.masc_names[name_num]} {vixen.last_names[lname_num]}"
                        case 1:
                            name_num = randrange(0, vixen.FEM_NAMES_MAX)
                            return f"{vixen.fem_names[name_num]} {vixen.last_names[lname_num]}"
                        case 2:
                            name_num = randrange(0, vixen.ANDRO_NAMES_MAX)
                            return f"{vixen.andro_names[name_num]} {vixen.last_names[lname_num]}"
                        case _:
                            print(f"{tc.FAIL}Something has gone terribly wrong. Terminating...")
                            print("Something has gone terribly wrong, and the script has terminated.", file=open('output_failed.txt','w'))
                            quit(1)
                            return
                case _:
                    print('For the record, this function requires SOMETHING to work with.')
                    return 'Not Provided'
                
def reySpecGen(furbro):
    match furbro:
        case 'yes'|'woof'|'bark'|'meow'|'mreow'|'marp'|'mrrp'|'arf'|'mow':
            specnum = randrange(0, vixen.SPECIES_MAX)
            match specnum:
                case 0:    
                    specnum1 = randrange(0, vixen.SPECIES_MAX)
                    while specnum1 == 0:
                        specnum1 = randrange(1, vixen.SPECIES_MAX)
                    if specnum1 == 3:
                        return "Robot"
                    else:
                        return f"Robot {vixen.species[specnum1]}"
                case 1:
                    specnum1 = randrange(0, vixen.SPECIES_MAX)
                    while specnum1 == 1:
                        specnum1 = randrange(0, vixen.SPECIES_MAX)
                    if specnum1 == 3:
                        return "Angel"
                    else:
                        return f"{vixen.species[specnum1]} Angel"
                case 2:
                    specnum1 = randrange(0, vixen.SPECIES_MAX)
                    while specnum1 == 2:
                        specnum1 = randrange(0, vixen.SPECIES_MAX)
                    if specnum1 == 3:
                        return "Demon"
                    else:
                        return f"{vixen.species[specnum1]} Demon"
                case 4:
                    specnum1 = randrange(5, vixen.SPECIES_MAX)
                    specnum2 = randrange(5, vixen.SPECIES_MAX)
                    while specnum1 == specnum2:
                        specnum2 = randrange(5, vixen.SPECIES_MAX)
                    return f"{vixen.species[specnum1]} {vixen.species[specnum2]} Hybrid"
                case _:
                    return vixen.species[specnum]
        case 'no':
            specnum = randrange(0, 12)
            match specnum:
                case 0:
                    return "Robot"
                case 1:
                    return "Angel"
                case 2:
                    return "Demon"
                case _:
                    return "Human"
        case _:
            print(tc.FAIL + 'Whuh?' + tc.ENDC)
            return 'Whuh?'

def reyAgeGen(rang):
    match rang:
        case 'child'|'kid':
            return str(randrange(8,12))
        case 'teen'|'teenager':
            return str(randrange(13,17))
        case 'young':
            return str(randrange(8,17))
        case 'young adult':
            return str(randrange(18,35))
        case 'adult':
            return str(randrange(36,64))
        case 'old'|'elder':
            return str(randrange(65,120))
        case 'immortal'|'abnormal'|'inhuman':
            return str(randrange(18,500))
        case _:
            return str(randrange(8,120))

def reyGenderGen(nos):
    match nos:
        case 'yes':
            gendernum = randrange(0, vixen.GENDER_MAX)
            gendersuf = randrange(0, vixen.GENDER_SUFFIX_MAX)
            match gendersuf:
                case 8|9:
                    return f"{vixen.gender_suffixes[gendersuf]} {vixen.genders[gendernum]}"
                case _:
                    return f"{vixen.genders[gendernum]}"
        case 'no':
            return vixen.genders[randrange(0, 2)]