import sys
import os
import msvcrt

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from map_engine import create_map, place_entity, render_map, is_walkable, add_walls, add_doors

WORLD_W, WORLD_H = 3, 2   # świat ma 3x2 pokoje
def clear_screen():
    os.system('cls')

def build_room(room_x, room_y, width, height):
    room = create_map(width, height)
    add_walls(room)
    add_doors(
        room,
        north=room_y > 0,
        south=room_y < WORLD_H - 1,
        west=room_x > 0,
        east=room_x < WORLD_W - 1,
    )
    return room


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
    room_x, room_y = 0, 0     # w którym pokoju jesteśmy
    player_x, player_y = 7, 4
    
    # Nieskończona pętla gry
    while True:
        clear_screen()
        level_map = build_room(room_x, room_y, width, height)
        # --- ZMIANA: Wrzucamy na mapę wybrany znak, a nie "sztywne" @ ---
        place_entity(level_map, player_x, player_y, player_symbol)
        
        print("--- EKSPLORACJA LOCHÓW ---")
        print(f"Pokój: ({room_x}, {room_y})")
        print(render_map(level_map))
        print("\nSterowanie: W A S D | Wyjście: Q")
        
        key = msvcrt.getch().decode('utf-8').lower()
        
        new_x, new_y = player_x, player_y

        if key == 'w':
            new_y -= 1
        elif key == 's':
            new_y += 1
        elif key == 'a':
            new_x -= 1
        elif key == 'd':
            new_x += 1
        elif key == 'q':
            print("Wychodzenie z gry...")
            break

        if is_walkable(level_map, new_x, new_y):
            if level_map[new_y][new_x] == "+":
            # Przechodzimy przez drzwi
                if key == 'w' and room_y > 0:
                    room_y -= 1
                    new_y = height - 2
                elif key == 's' and room_y < WORLD_H - 1:
                    room_y += 1
                    new_y = 1
                elif key == 'a' and room_x > 0:
                    room_x -= 1
                    new_x = width - 2
                elif key == 'd' and room_x < WORLD_W - 1:
                    room_x += 1
                    new_x = 1
            player_x, player_y = new_x, new_y
            
if __name__ == "__main__":
    main()