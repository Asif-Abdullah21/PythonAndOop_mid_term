class Star_Cinema:
    __hall_list = []

    def entry_hall(self,obj_of_hall):
        self.__hall_list.append(obj_of_hall)
    @property
    def list_Of_hall(self):
        return self.__hall_list
        
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        super().__init__()
    
    def entry_show(self,show_id,movie_name,time):
        show_all = (show_id,movie_name,time)
        self.show_list.append(show_all)
    
        all_seats = []
        for i in range(self.rows):
            row_of_seats = []
            for j in range(self.cols):
                row_of_seats.append('0')
            all_seats.append(row_of_seats)
        
        self.seats[show_id] = all_seats

    def book_seats(self,id,seat_list):
        for sl in self.show_list:
            if(sl[0]==id):
                for row,col in seat_list:
                    if row>=0 and row<self.rows and col>=0 and col <self.cols:
                        if self.seats[id][row][col] == '0':
                            self.seats[id][row][col] = '1'
                            print(f'Thans for booking the seat: {row},{col}.')
                        else:
                            print(f'The seat {row},{col} is already booked.')
                    else:
                        print(f'The seat {row}, {col} does not exists.')
                        print()
                return
        print()
        print(f'The movie with ID {id} does not exists in the lsit.')


    def view_show_list(self):
        print('Show List:')
        print('__________')
        for sl in self.show_list:
            print(f'Movie ID: {sl[0]},  Movie Name: {sl[1]},  Show Time: {sl[2]}')
        print('___________________________________________________________________')

    def view_available_seats(self,id):
        for sl in self.show_list:
            if(sl[0]==id):
                seat = self.seats[id]
                for row in seat:
                    print(row)
                return
        print()
        print(f'The show you searched with ID {id} is not in our show list.')



movie = Star_Cinema()
hall = Hall(5,10,15)
movie.entry_hall(hall)

hall.entry_show("185", "The Lion of the Desert", "3:00 PM - 23/01/2024")
hall.entry_show("186", "Reign of Love", "6:00 PM - 23/01/2024")
hall.entry_show("187", "The Fateful Day", "9:00 PM - 23/01/2024")

while True:
    print()
    print('1. View all running shows')
    print('2. View available seats')
    print('3. Booking tickets')
    print('4. Exit')
    print()

    op = int(input("Choose an option please: "))

    if(op<1 or op >4):
        print("\n Invalid option! Try again with a valid option.\n")
    elif op == 1:
        for movies in movie.list_Of_hall:
            movies.view_show_list()
    elif op == 2:
        movie_id = input("Enter movie id: ")
        hall.view_available_seats(movie_id)
    elif op == 3:
        id = input('Enter show id: ')
        no_of_ticekts = int(input('Number of ticketes you want: '))
        ticket_list = []
        
        for i in range(no_of_ticekts):
            r = int(input("Enter seat row: "))
            c = int(input("Enter seat column: "))
            
            ticket_list.append((r,c))
            
        hall.book_seats(id, ticket_list)

    elif op == 4:
        break




