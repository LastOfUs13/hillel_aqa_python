from HW11_submarine import Submarine

if __name__ == '__main__':
    submarine = Submarine()  # Encapsulation
    submarine.get_coordinates_and_move(69, 96)
    print("current latitude", submarine.latitude, "current longitude", submarine.longitude)

