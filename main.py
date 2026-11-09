import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from map_engine import create_map

def main():
    print("--- Rozpoczęcie gry ---")
    
    level_map = create_map(10, 5)
    
    for wiersz in level_map:
        print(wiersz)

if __name__ == "__main__":
    main()