import sys

year = int(input("Enter your birth year: "))


zodiacsigns = [
        
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
   "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)",
    ]

baseline = 1900
index = (year - baseline) % 12

if year < baseline:
    print("Invalid year, it should not be earlier than 1900.")
    sys.exit()
else:
    print(f"Your chinese zodiac sign is: {zodiacsigns[index]}")


<img width="597" height="895" alt="Screenshot 2026-08-21 070541" src="https://github.com/user-attachments/assets/9dc917e6-2cbe-45b5-8ca2-34916646af6a" />


