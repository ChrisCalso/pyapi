#!/usr/bin/python3

char_name = input("Which character do you want to know about? (Flash, Batman, Superman")
char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence")

hero= {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

print(f"{char_name}'s {char_stat} is: {hero[char_name][char_stat])

