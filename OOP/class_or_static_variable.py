# todo: class or static variable

'''
    class variable is not a instance variable it's just a variable of that class
    it's not object dependent
    it's a property of that class
    this variable should be access or called by Class Name
'''


class Player:
    team_run = 0  # class or static variable

    def __init__(self, run):
        self.run = run  # instance variable

    def hit_four(self):
        self.run += 4
        Player.team_run += 4

    def hit_six(self):
        self.run += 6
        Player.team_run += 6


# ===============
sakib = Player(0)
tamim = Player(0)
sakib.hit_six()
sakib.hit_four()
tamim.hit_four()
tamim.hit_four()
print("Sakib: ", sakib.run)
print("Tamim: ", tamim.run)
print("Team Run: ", Player.team_run)
print("Team Run: ", tamim.team_run)
print("Tamim: ", tamim.run)
