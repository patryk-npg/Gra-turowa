import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))


from map_engine import add_doors, add_items, add_traps, add_walls, create_map, is_walkable, add_obsacles, add_items, add_traps

def run_tests():
    test_map = create_map(5, 3)
    
    assert len(test_map) == 3, "Zła wysokość"
    assert len(test_map[0]) == 5, "Zła szerokość"
    
    print("Wszystkie testy przeszły pomyślnie")

    if __name__ == "__main__":
        run_tests()
        walls_map = create_map(5, 3)
    
    add_walls(walls_map)
    assert walls_map[0][0] == "#", "Brak ściany w rogu"
    assert not is_walkable(walls_map, 0, 0), "Ściana powinna blokować"
    assert is_walkable(walls_map, 2, 1), "Środek powinien być przechodni"

    door_map = create_map(15, 8)
    add_walls(door_map)
    add_doors(door_map, north=True, east=True)
    assert door_map[0][7] == "+", "Brak drzwi na północy"
    assert door_map[4][14] == "+", "Brak drzwi na wschodzie"
    assert is_walkable(door_map, 7, 0), "Drzwi powinny być przechodnie"

    obs_map = create_map(15, 8)
    add_obsacles(obs_map, [(4, 2), (4, 3)])
    assert obs_map[2][4] == "#", "Brak przeszkody"
    assert not is_walkable(obs_map, 4, 3), "Przeszkoda powinna blokować"
    assert is_walkable(obs_map, 5, 3), "Obok przeszkody powinno być wolne"

    item_map = create_map(15, 8)
    add_items(item_map, [(2, 2), (5, 5)])
    assert item_map[2][2] == "$", "Brak monety"
    assert item_map[5][5] == "$", "Brak drugiej monety"
    assert is_walkable(item_map, 2, 2), "Moneta nie powinna blokować"

    trap_map = create_map(15, 8)
    add_traps(trap_map, [(3, 3), (6, 6)])
    assert trap_map[3][3] == "^", "Brak pułapki"
    assert trap_map[6][6] == "^", "Brak drugiej pułapki"
    assert is_walkable(trap_map, 3, 3), "Pułapka nie powinna blokować"