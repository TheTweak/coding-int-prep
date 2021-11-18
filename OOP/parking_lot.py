'''
Design a parking lot.

What objects are taking part in the parking lot:

1) do we allow heavy trucks or only lightweight cars?
2) is this a paid parking lot?
3) if it is paid, price is per hour or one time payment?
4) is it a single or multi entry parking lot?

- a car
- a parking payment machine
- a parking gate

'''

class Car:
    def __init__(self, license_plate: str):
        self.license_plate = license_plate


class ParkingLot:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.size = 0
        self.entrance_fee = 5

    def enter(self, car: Car) -> int:
        '''
        Try to enter a parking lot. Returns the new number of
        free parking lots remaining.
        - checks if a parking lot has enough capacity
        - if it does:
        -- takes entrance fee from the car
        -- reads the license plate number from the car
        -- opens the gate
        -- waits for the car to get in
        -- closes the gate
        - if it doesn't:
        -- display a message that parking lot is full
        '''
        if self.size >= self.capacity:
            print('Parking lot is full')
            return self.size

        if not self.__take_entrance_fee(car):
            print('The parking lot is paid')
            return self.size

        self.__read_license_plate(car)
        self.__open_gate()
        self.__close_gate()
        self.size += 1

    def __take_entrance_fee(self, car: Car) -> bool:
        pass

    def __read_license_plate(self, car: Car) -> str:
        pass

    def __open_gate(self) -> None:
        pass

    def __close_gate(self) -> None:
        pass

    def exit(self, car: Car) -> int:
        '''
        Exit the parking lot. Returns the number of free
        parking lots remaining.
        - opens the gate
        - waits for the car to drive out
        - closes the gate
        '''
        self.__open_gate()
        self.__close_gate()
        self.size -= 1
