"""
prac_06 - languages
Time estimate = 15 minutes
actual =
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
# print(python)

languages = [python, ruby, visual_basic]
for language in languages:
    print(language)

print("The dynamically typed programming languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)

