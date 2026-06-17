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

# User coordinates input
def get_coordinates():
    print("📍 Enter your Agency Tower Coordinates")
    lat = input("Latitude (e.g. 41.45 for Lorain): ").strip() or "41.45"
    lon = input("Longitude (e.g. -82.15 for Lorain): ").strip() or "-82.15"
    print(f"📍 Agency Tower Location: {lat}°N, {lon}°W")
    print("Divine Angle: Active | Green Frequency: Strong")
    print("=" * 70)
    return lat, lon

# Get coordinates once at start
lat, lon = get_coordinates()

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
        
        gain = random.randint(65, 165)
        rent = random.randint(8, 18)
        utilities = random.randint(4, 12)
        supplies = random.randint(3, 9)
        maintenance = random.randint(2, 7)
        expense = rent + utilities + supplies + maintenance
        
        net = gain - expense
        budget = budget + net
        if budget < 0:
            budget = 0
        save_budget(budget)
        
        # Advanced Info for each module
        if choice == "1":
            print("UFO Flight Simulator - Advanced Info")
            print("Divine Angle Mode: Stability 94% | Altitude 12.4 km | Stealth: Full Cloak")
            print("Perfect hover over rock stack confirmed.")
        elif choice == "2":
            print("ICESat-2 Orbital Tracking - Advanced Telemetry (NORAD 43613)")
            print("Current Altitude: ~496 km")
            print("Velocity: 7.61 km/s")
            print(f"Next Pass over your location ({lat}°N, {lon}°W): ~{random.randint(25, 55)} minutes")
            print("Ground Track: Clear visibility window")
            print("Inclination: 92.01° | Orbital Period: ~94 minutes")
            print("Roof/Tower Risk: LOW | Divine Angle Sync: Perfect")
        elif choice == "3":
            print("Nanite Roof Repair - Advanced Info")
            print("Current Integrity: 97% | Mist Applied: Light coverage")
            print("Storm Resistance: +42% | Reflective nanite layer forming")
        elif choice == "4":
            print("Downed UFO Recovery - Advanced Info")
            print("Target Depth: ~4,200m | Recovery Success: 100%")
            print("God's Drone deployed. Materials secured.")
        elif choice == "5":
            print("Hybrid Energy Core - Advanced Info")
            print("Rotating Solar: 158% | Wind: Strong | Fusion: Stable")
            print("Nanite Cooling: Radiation → Clean Fuel | Total Output: 237%")
        elif choice == "6":
            print("Math Training - Advanced Info")
            print("Aerospace Concepts Mastered: Thrust, Stability, Orbital Velocity")
            print("Session Accuracy: Excellent")
        elif choice == "7":
            print("Marketing Module - Advanced Info")
            print("Organic reach growing. Meme engagement high.")
        elif choice == "8":
            print("Silent Zone Defense - Advanced Info")
            print("Radius: 500m | Missile Nullification: ACTIVE")
            print("Green Shield: 100% | Threats Neutralized")
        elif choice == "9":
            print("God's Computer Link - Advanced Info")
            print("Connection: 100% | Message: 'Well done, my good son.'")
            print("Vision: Tower as full Sentinel Museum.")
        elif choice == "10":
            print("Full Mission Report - Advanced Summary")
            print("All systems aligned. Momentum strong. Keep stacking.")
        
        print(f"Income this cycle: +${gain:,}k")
        print(f"Expenses/Bills: -${expense:,}k (Rent ${rent}k + Utilities ${utilities}k + Supplies ${supplies}k + Maintenance ${maintenance}k)")
        print(f"Net this cycle: +${net:,}k")
        input("\nPress Enter to return to Tower...")
    else:
        print("Invalid choice. Stay vigilant.")
        time.sleep(1)
