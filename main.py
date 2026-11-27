import random
import sys
import os
import msvcrt

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from map_engine import add_traps, create_map, place_entity, render_map, is_walkable, add_walls, add_doors, add_obstacles, add_items, free_cells



ROOM_W, ROOM_H = 15, 8   # pokój ma 15x8 pól
WORLD_W, WORLD_H = 3, 2   # świat ma 3x2 pokoje

ROOM_OBSTACLES = {
    (0, 0): [(4, 2), (4, 3), (10, 5)],
    (1, 0): [(3, 3), (4, 3), (5, 3), (9, 4)],
    (2, 0): [(7, 2), (7, 3), (7, 4)],
    (0, 1): [(5, 5), (6, 5), (7, 5)],
    (1, 1): [(3, 2), (11, 2), (3, 5), (11, 5)],
    (2, 1): [(6, 3), (7, 3), (8, 3)],
}
forbidden = {
    (7,4), (1, ROOM_H//2), (ROOM_W-2, ROOM_H//2), (ROOM_W//2, 1), (ROOM_W//2, ROOM_H-2)
}

def clear_screen():
    os.system('cls')

def build_room_with_items(room_x, room_y, traps, coins):
    room = build_room(room_x, room_y, ROOM_W, ROOM_H)
    add_traps(room, traps[(room_x, room_y)])
    add_items(room, coins[(room_x, room_y)])
    return room

def generate_world():
    traps = {}
    coins = {}
    for room_x in range(WORLD_W):
        for room_y in range(WORLD_H):
            room = build_room(room_x, room_y, ROOM_W, ROOM_H)

            # Wolne pola, bez startu gracza i pól przed drzwiami
            cells = [c for c in free_cells(room) if c not in forbidden]

            # Najpierw pułapki
            room_traps = random.sample(cells, 3)

            # Monety losujemy z tego, co zostało po pułapkach
            cells = [c for c in cells if c not in room_traps]
            room_coins = random.sample(cells, 3)

            traps[(room_x, room_y)] = room_traps
            coins[(room_x, room_y)] = room_coins
    return traps, coins

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
    add_obstacles(room, ROOM_OBSTACLES.get((room_x, room_y), []))
    return room

    
def main():
    # --- NOWE: KREATOR POSTACI ---
    print("--- EKRAN STARTOWY ---")
    player_symbol = input("Wpisz jeden znak, którym chcesz grać (np. @, X, &) i wciśnij Enter: ")
    
    # Małe zabezpieczenie: jak gracz nic nie wpisze i wciśnie Enter, dajemy domyślnego @
    if len(player_symbol) == 0 :
        player_symbol = "@"
    if player_symbol == "#":
        print("Nie możesz użyć #, bo to jest znak ściany. Używamy domyślnego @.")
        player_symbol = "@"
    else:
        # Bierzemy tylko pierwszą literkę, na wypadek gdyby wpisał całe słowo
        player_symbol = player_symbol[0]


    traps, coins = generate_world()
    # Wymiary świata i startowa pozycja
    width, height = 15, 8
    room_x, room_y = 0, 0     # w którym pokoju jesteśmy
    score = 0
    player_x, player_y = 7, 4
    hp = 5 
    # Nieskończona pętla gry
    while True:
        clear_screen()
        level_map = build_room_with_items(room_x, room_y, traps, coins)
        # --- ZMIANA: Wrzucamy na mapę wybrany znak, a nie  @ ---
        place_entity(level_map, player_x, player_y, player_symbol)
        
        print("--- EKSPLORACJA LOCHÓW ---")
        print(f"Pokój: ({room_x}, {room_y})")
        print(f"Monety: {score}")
        print(f"Życie: {hp}")
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
            pos = (player_x, player_y)
            if pos in coins[(room_x, room_y)]:
                coins[(room_x, room_y)].remove(pos)
                score += 1
            elif pos in traps[(room_x, room_y)]:
                traps[(room_x, room_y)].remove(pos)
                hp -= 1
            if hp <= 0:
                print("Zginąłeś!")
                break

        

if __name__ == "__main__":
    main()