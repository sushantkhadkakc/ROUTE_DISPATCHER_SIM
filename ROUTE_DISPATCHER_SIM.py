class rds:
    def __init__(self):
         self.vehc=['BUS','098','CAR','122']
    def veh(self):
        
        print("AVIALBLE VEHCILE\n")
        
        for item in self.vehc:
            
            try:
                if item.isdigit():
                    print(f"VEHICLE NUMBER:{item}")
                else:
                    print(f"VECHICLE NAME:{item}")    
            except ValueError:
                pass     
            print("================\n")
        user_choice=input("ENTER VEHICLE NAME\n").upper()
        self.route()
    def route(self):
        route_1=['KATHMANU TO CHORMARA ','CHORMARA TO KATHMANDU']
        for item_2 in route_1:
            print(item_2)
            print("================\n")
        self.user_choice_2=input("ENTER YOUR ROUTE\n").upper()
        if(self.user_choice_2=='KATHMANDU TO CHORMARA'):
           self.fuel()
        elif(self.user_choice_2=='CHORMARA TO KATHMANDU'):
            self.fuel()
                
class rds_2(rds):
    def fuel(self):
            ktm_chor=198
            chor_ktm=201
            fuel_price=201
            if(self.user_choice_2=='KATHMANDU TO CHORMARA'):
                totalcost=ktm_chor*fuel_price
                print(f"TOTAL COST FROM KTM TO CHORMARA:{totalcost}")
                print("================\n")
            if(self.user_choice_2=='CHORMARA TO KATHMANDU'):
                totalcost_2=chor_ktm*fuel_price
                print(f"TOTAL COST FROM CHORMARA TO KTM:{totalcost_2}")
                print("================\n") 
    def vec(self):
        self.vechicle=input("ENTER THE VECHILE NAME\n")
        self.vehc.append(self.vechicle)
        self.number=input("ENTER THE VECHILE NUMBER\n")
        self.vehc.append(self.number)                   
    def view(self):
        self.view_2=input("ENTER IF YOU WANT VIEW VEHCILE DETAILS(Y/N)").upper()
        if(self.view_2=='Y'):
            for item_3 in self.vehc:
                print(item_3)
                print("================\n") 
        else:
            print("THANKYOUH!!!")
    def main(self):
        while True:
            print("-------------------------------\n")
            print("1.CALCULATE COST\n")
            print("2.VIEW VEHCILES\n")
            print("3.ADD VEHCILES\n")
            print("4.EXITS")
            try:
                 
                user=int(input("ENTER YOUR CHOICE(1 TO 4)\n")) 
                if(user==1):
                        a.veh()
                        a.fuel()
                        
                elif(user==2):
                        a.view()
                elif(user==3):
                        a.vec()
                elif(user==4):
                    quit()
                    break
                               
            except ValueError:
                        print("INVAILD\n")
a=rds_2()                        
a.main()                                                    