# python code to show updates about train information

'''<Q06> Practice 06: Yes we can change <self> with 
any valid identifier like <manish> or <slf> but then 
we have use it everywhere in the function as we have 
defined it as if we have defined it as <ae> then we 
have to it only like ae.<anyother parameter> like 
ae.name but we don't use it because it can create 
confusion when we're refering or revisting our code'''

import random

class Train:
    def __init__(self, seat, seats): 
        self.seat=seat
        print("**Train Name: Konark Express**")
        self.seats=seats
        for i in range(1, self.seat+1):
            self.seats=list(range(1, i+1))
        print(f"Seats Available: {self.seats}")
    def seatAvailability(self):
        print(f"Total Seat Available: {len(self.seats)} Seats")        
    def bookTicket(self):
        print("**Booking The Seat**")
        if len(self.seats)>0:
            print(f"Your Seat Number: {self.seats[0]} Seat")
            self.seat=self.seat-1
            del self.seats[0]
            print(f"Available Seats After Booking: {self.seats}")
        else:
            print("Ticket Too Nhi Hai TumHara!")
    def ticketStatus(self):
        print("**Checking The Seat Status**")
        seat=int(input("Enter Your Seat Number: "))
        if seat in range(1, self.seat+1):           
            ticket=random.randint(1, 3)
            if ticket==1:
                print("Ticket and Seat Status: CNF")
            elif ticket==2:
                print("Ticket and Seat Status: RAC")
            else:
                print("Ticket and Seat Status: WL")
        else:
            print("FULL: Ticket Too Nhi Hua TumHara")
    def pnrNumber(self):
        print("**PNR Number of The Seat**")
        ticket=input("Enter Your Ticket Status: ")
        if ticket.lower()=="cnf":
            print(f"PNR Number: KNK{7865}")
        elif ticket.lower()=="rac":
            print(f"PNR Number: KNK{7865}")
        elif ticket.lower()=="wl":
            print(f"PNR Number: KNK{7865}")
        elif ticket.lower()=="full":
            print("FULL: Ticket Too CNF(Confirm) Nhi Hai TumHara")
        else: 
            print("Invailid Status Hai GM!")
    def totalFare(self):
        print("**Total Fare For The Seat**")
        fare=input("Enter Your Seat Status: ")
        if fare.lower()=="cnf":
            print(f"Total Fare: Rs. {1850}: Book Karlo CNF aur Available Dono Hai!")
        elif fare.lower()=="rac":
            print(f"Total Fare: Rs. {1850}: Lekin Aadha Hee Berth Milega.")
        elif fare.lower()=="wl":
            print(f"Total Fare: Rs. {1850}: Humari Mano Dusra OPTION Try Karlo.")
        else:
            print("Tumse Kya Hee Paise Abb Jao GM!")
    def cancelTicket(self):
        print("**Ticket Cancelation Window**")
        seatnum=int(input("Enter Your Seat Number: "))
        # for seatnum in self.seats: not required
        if seatnum not in self.seats:
            self.seats.insert(0, seatnum)
            self.seats.sort()
        else:
            print("Invalid Seat Number")
        print("**Total Seats Available After Cancelation**")
        print(f"Seats Available After Cancelation: {self.seats}")

manish=Train(7, 7)
manish.seatAvailability()
manish.bookTicket()
manish.ticketStatus()
manish.pnrNumber()
manish.totalFare()
manish.seatAvailability()
manish.bookTicket()
manish.cancelTicket()
manish.seatAvailability()
