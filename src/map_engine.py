def create_map(width, height):
    return [["." for _ in range(width)] for _ in range(height)]

def place_entity(game_map, x, y, symbol):
    # Wstawia konkretny znak (np. gracza) na podane koordynaty (x, y)
    game_map[y][x] = symbol

def render_map(game_map):
    # Zlepia siatkę w jeden blok tekstu (bez nawiasów i przecinków)
    return "\n".join("".join(row) for row in game_map)
def is_walkable(game_map, x, y):
    # Sprawdza czy pole mieści się w mapie i nie jest ścianą
    if 0 <= y < len(game_map) and 0 <= x < len(game_map[0]):
        return game_map[y][x] != "#"
    return False

def add_walls(game_map):
    # Dodaje ściany (#) na krawędziach mapy
    height = len(game_map)
    width = len(game_map[0])
    for x in range(width):
        game_map[0][x] = "#"
        game_map[height - 1][x] = "#"
    for y in range(height):
        game_map[y][0] = "#"
        game_map[y][width - 1] = "#"

def add_doors(game_map, north=False, south=False, east=False, west=False):
    # Robi dziurę ("+") na środku wybranych ścian
    height = len(game_map)
    width = len(game_map[0])
    if north:
        game_map[0][width // 2] = "+"
    if south:
        game_map[height - 1][width // 2] = "+"
    if west:
        game_map[height // 2][0] = "+"
    if east:
        game_map[height // 2][width - 1] = "+"

def add_obsacles(game_map, positions):
    # Dodaje przeszkody w podanej pozycji
    for x, y in positions:
        game_map[y][x] = "#"

def add_items(game_map, positions):
    # Dodaje przedmioty w podanej pozycji
    for x, y in positions:
        game_map[y][x] = "$"