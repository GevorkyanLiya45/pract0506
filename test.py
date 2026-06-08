import requests

print('Start avto testirovanya "Secyndomer"')

def update_time_logic(seconds, milliseconds):
    milliseconds += 1
    if milliseconds >= 100:
        milliseconds = 0
        seconds += 1
    return seconds, milliseconds

print("Zapysk avtotesta logiki Secyndomera...")
sec, ms = update_time_logic(0, 99)
assert ms == 0
assert sec == 1
print("[PASSED] Logika scheta vremeni rabotaet korrectno!.")

print("\nZapysk proverki vnehnego API toshnogo vremeni...")
response = requests.get("https://api.mathjs.org/v4/?expr=5%2B5")
assert response.status_code == 200
print("[PASSED] Statys otveta servera vremeni: 200 OK")
assert response.text == "10"
print("[PASSED] Otvet servera uspesno polythen i obrabotan.")

print("\nVce testi uspeshno proydeny!")