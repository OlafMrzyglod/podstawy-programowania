light_switch1 = input("Switch 1 on? (y/n): ").lower() == "y"
light_switch2 = input("Switch 2 on? (y/n): ").lower() == "y"
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2
print(f"Bulbs on: {bulbs_on}")
