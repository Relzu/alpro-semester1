character_name : str = "Farel Fadilah Hafizd"
character_die : bool = False
current_health : int
max_health : int = 100


damage = int(input("Masukkan Damage : "))

if damage >= max_health:
    print(f"{character_name} mati")
    character_die = True
else:
    current_health = max_health - damage
    print(f"{character_name} masih hidup dengan HP {current_health} dengan bleed damage {damage}")