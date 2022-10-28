from guitar import Guitar

current_year = 2022

gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
another_guitar = Guitar("Another guitar", 2000, 150)
ukulele = Guitar("Ukulele", 1972, 1.01)


print(f"Gibson get_age(), expected 100. Got {gibson.get_age(current_year)}")
print(f"Another guitar get_age(), expected 22. Got {another_guitar.get_age(current_year)}")
print(f"Ukulele get_age(), expected 50. Got {ukulele.get_age(current_year)}")
print(f"Gibson is_vintage(), expected True. Got {gibson.is_vintage(current_year)}")
print(f"Another guitar is_vintage(), expected False. Got {another_guitar.is_vintage(current_year)}")

