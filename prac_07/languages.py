from prac_07.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
print(ruby)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
print(python)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(visual_basic)

programs = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for program in programs:
    if program.is_dynamic():
        print(program.name)

print(program.name for program in programs if program.is_dynamic())