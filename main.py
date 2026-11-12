import sys
import os
import msvcrt

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from map_engine import create_map, place_entity, render_map

def clear_screen():
    os.system('cls')

def main():
    # --- NOWE: KREATOR POSTACI ---
    print("--- EKRAN STARTOWY ---")
    player_symbol = input("Wpisz jeden znak, którym chcesz grać (np. @, X, &) i wciśnij Enter: ")
    
    # Małe zabezpieczenie: jak gracz nic nie wpisze i wciśnie Enter, dajemy domyślnego @
    if len(player_symbol) == 0:
        player_symbol = "@"
    else:
        # Bierzemy tylko pierwszą literkę, na wypadek gdyby wpisał całe słowo
        player_symbol = player_symbol[0]


    # Wymiary świata i startowa pozycja
    width, height = 15, 8
    player_x, player_y = 7, 4
    
    # Nieskończona pętla gry
    while True:
        clear_screen()
        level_map = create_map(width, height)
        
        # --- ZMIANA: Wrzucamy na mapę wybrany znak, a nie "sztywne" @ ---
        place_entity(level_map, player_x, player_y, player_symbol)
        
        print("--- EKSPLORACJA LOCHÓW ---")
        print(render_map(level_map))
        print("\nSterowanie: W A S D | Wyjście: Q")
        
        key = msvcrt.getch().decode('utf-8').lower()
        
        if key == 'w':
            player_y -= 1
        elif key == 's':
            player_y += 1
        elif key == 'a':
            player_x -= 1
        elif key == 'd':
            player_x += 1
        elif key == 'q':
            print("Wychodzenie z gry...")
            break
            
        player_x = max(0, min(width - 1, player_x))
        player_y = max(0, min(height - 1, player_y))

if __name__ == "__main__":
    main()