from HW11_submarine import Submarine

if __name__ == '__main__':
    submarine = Submarine()  # Encapsulation
    submarine.get_coordinates_and_move(43, 342)
    print("current latitude", submarine.latitude, "current latitude", submarine.longitude)

