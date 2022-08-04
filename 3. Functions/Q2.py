def check_baggage (baggage_weight) :
    if(baggage_weight>=0 or baggage_weight<=40) :
        return True
    else :
        return False

def check_immigration (expiry_year) :
    if(expiry_year>=2030 or expiry_year<=2050) :
        return True
    else :
        return False

def check_security(noc_status) :
    if(noc_status=="VALID" or noc_status=="valid") :
        return True
    else :
        return False
def traveler() :
    print('-'*70)
    traveler_Id = int(input('Enter the traveler id :- '))
    traveler_name = input('Enter the traveler name :- ')
    baggage_weight = int(input('Enter the baggage weight :- '))
    expiry_year = int(input('Enter the expiry year :- '))
    noc_status = "valid"
    if(check_baggage(baggage_weight)==check_immigration(expiry_year)==check_security(noc_status)==True) :
        print('-'*70)
        print('Traveler Id :- ',traveler_Id)
        print('Traveler Name :- ',traveler_name)
        print('Passenger is allowed top travel')
    else :
        print('-'*70)
        print('Traveler Id :- ',traveler_Id)
        print('Traveler Name :- ',traveler_name)
        print('Detain Traveler for Re-checking!')

traveler()
