# agency_tower.py - Z.O.R.T Sentinel Agency Command Center v3.9
# Offline | Donations Only | Green Frequency | Keep Stacking

import time
import random
import os
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_budget():
    try:
        with open("agency_budget.txt", "r") as f:
            return int(f.read().strip())
    except:
        return 450000

def save_budget(budget):
    with open("agency_budget.txt", "w") as f:
        f.write(str(int(budget)))

budget = load_budget()

def loading_bar(seconds=2):
    for i in range(21):
        print(f"[{('█' * i):<20}] {i*5}%", end='\r')
        time.sleep(seconds / 20)
    print()

def divine_commentary():
    comments = [
        "🙏 The Lord smiles on this work.",
        "Green frequency strong.",
        "No Harm Near — mission aligned.",
        "Keep stacking. The tower grows.",
        "Divine angle locked in."
    ]
    print(random.choice(comments))

while True:
    clear()
    print("=" * 70)
    print("🛸 Z.O.R.T SENTINEL AGENCY TOWER v3.9")
    print("Green Frequency • Donations Only • Offline")
    print(f"Agency Budget: ${budget:,}")
    print("=" * 70)
    print("1. UFO Flight Simulator")
    print("2. ICESat-2 Orbital Tracking")
    print("3. Nanite Roof Repair")
    print("4. Downed UFO Recovery")
    print("5. Hybrid Energy Core")
    print("6. Math Training")
    print("7. Marketing Module")
    print("8. Silent Zone Defense")
    print("9. God's Computer Link")
    print("10. Full Mission Report")
    print("0. Exit Tower")
    
    choice = input("\nSelect module: ").strip()
    
    if choice == "0":
        print("Tower standing strong. Keep stacking. ✌️")
        break
    elif choice in ["1","2","3","4","5","6","7","8","9","10"]:
        clear()
        print(f"🚀 Launching Module {choice}...")
        loading_bar(1.5)
        divine_commentary()
        gain = random.randint(15, 95)
        expense = random.randint(5, 28)
        budget = max(50000, budget + gain - expense)
        save_budget(budget)
        print(f"Net this cycle: +${gain - expense:,}k")
        input("\nPress Enter to return to Tower...")
    else:
        print("Invalid choice. Stay vigilant.")
        time.sleep(1)