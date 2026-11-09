import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))


from map_engine import create_map

def run_tests():
    test_map = create_map(5, 3)
    
    assert len(test_map) == 3, "Zła wysokość"
    assert len(test_map[0]) == 5, "Zła szerokość"
    
    print("Wszystkie testy przeszły pomyślnie")

if __name__ == "__main__":
    run_tests()