import csv
from math import floor, ceil

# get nba teams from web scraped file and place into teams list
teams = []
with open("teams.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        teams.append(row[0])

class NBA_player:
    all_players = []
    def __init__(self, name: str, height: float, age: int, weight: float, team: str, contract=500000, contract_years=1,):
        # check data types
        assert type(name) == str, f"Invalid data type for name"
        assert type(height) == float, f"Invalid data type for height"
        assert type(age) == int, f"Invalid data type for age"
        assert type(weight) == float or type(weight) == int, f"Invalid data type for weight"
        assert type(team) == str, f"Invalid data type for team"
        assert type(contract) == int, f"Invalid data type for salary"
        assert type(contract_years) == int, f"Invalid data type for years on salary"
        
        # run validations
        assert height > 6.2 and height < 8, f"You're height is either unrealistic or too short"
        assert age > 17  and age < 44, f"You are either too young or too old"
        assert weight >= 170 and weight <= 360, f"You are either too heavy or too light"
        assert team in teams, f"You are not on a valid team"
        assert contract >= 500000, f"You're salary is too low to be valid"
        assert contract_years >= 1, f"You're salary is too low to be valid"
        
        # assign 'self' var
        self.__name = name          # can only change name with 'setter'
        self.height = height
        self.age = age
        self.weight = weight
        self.team = team
        self.contract = contract
        self.contract_years = contract_years
        
        # add to list of all players
        NBA_player.all_players.append(self)
        
    # properties not needed
    
    # setter
    # @name.setter
    # def name(self, value):
    #     self.__name = value
    
    # methods
    def calculate_annual_salary(self):
        # calculate average salary
        avg_salary = self.contract / self.contract_years # RIGHT
        percentage = 0
        if self.contract_years == 5:  # sets percentage for difference b/t salaries
            percentage = 0.06896551724
        elif self.contract_years == 3:
            percentage = 0.04761904761
        elif self.contract_years == 4:
            percentage = 0.03571429367
        diff = avg_salary * percentage # multiply by certain value to get difference b/t salaries
        salary_years = []
        decrease = increase = avg_salary
        if self.contract_years % 2 != 0:
            salary_years.append(round(avg_salary))
        for i in range(self.contract_years):  # increase or decrease annual salaries
            if i % 2 == 0: # decrease previous decrease by diff * 2
                if len(salary_years) == 0 or (len(salary_years) == 1 and i == 0):
                    decrease = decrease-diff
                    salary_years.append(round(decrease))
                else:
                    decrease = decrease-(diff*2)
                    salary_years.append(round(decrease))
            else:
                if len(salary_years) == 1 or (len(salary_years) == 2 and i == 1):
                    increase = increase+diff
                    salary_years.append(round(increase))
                else:
                    increase = increase+(diff*2)
                    salary_years.append(round(increase))
        salary_years.sort()  # sort salaries to correspond to year indicies
        print(f"{self.__name}'s annual salary based on contract:")
        for i in range(len(salary_years)):  # print salaries
            print(f"Year {i+1}: ${salary_years[i]:,.2f}")
        
        
        
    
    

Jason = NBA_player("Stephen Curry", 6.7, 25, 225, "Golden State Warriors", 215159700, 5)

Jason.calculate_annual_salary()
    
'''
NBA player (name, height, age, weight, team, salary):
    init
    position (height, weight)

'''