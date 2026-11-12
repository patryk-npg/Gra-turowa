def create_map(width, height):
    return [["." for _ in range(width)] for _ in range(height)]

def place_entity(game_map, x, y, symbol):
    # Wstawia konkretny znak (np. gracza) na podane koordynaty (x, y)
    game_map[y][x] = symbol

def render_map(game_map):
    # Zlepia naszą siatkę w jeden ładny blok tekstu (bez nawiasów i przecinków)
    return "\n".join("".join(row) for row in game_map)