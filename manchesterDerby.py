"""CSC 161 Lab: Computer and Programs

Abduljabbar Said
Lab Section TR 2:00-3:15pm
Spring 2019
"""

from graphics import Point, GraphWin, Rectangle, Text
Teams = {"mcfc": ("mcfc", 1),
         "mutd": ("mutd", 1)}

Teams["mcfc"] = ("mcfc", 1)
Teams["mutd"] = ("mutd", 1)


class eplmd:
    def __init__(self, team, games):
        self.team = team
        self.games = games

    def get_team(self):
        return self.team

    def get_games(self):
        return self.games


def main():
    a = "mcfc"
    b = "mutd"
    aa = "vs Manchester United"
    bb = "@ Manchester City"

    print("Welcome to the Manchester Derby ")
    print("You will choose either Manchester City or Manchester United")
    print("")
    print("If you want Manchester City, type in 'mcfc' ")
    print("If you want Manchester United, type in ' mutd' ")
    print("You will get to choose the score and the winner of the game")
    mcmu = input(str("Please enter the team that you want to be:  "))

    if mcmu in Teams[a]:
        print("Your team is Manchester City")
        print("Your schedule is: ")
        print("9/17/18 ", aa)
        mc = input("How many goals did Manchester City Scored?  ")
        mu = input("How many goals did Manchester United Scored?  ")
        if int(mc) > int(mu):
            print("Final Score Is", mc, "to", mu)
            win = GraphWin("Manchester Derby", 750, 750)
            rect1 = Rectangle(Point(0, 0), Point(750, 750))
            rect1.setFill("Cyan")
            rect1.setWidth(2)
            champ1 = Text(Point(350, 350), "Manchester City Won")
            champ1.setFill = ("Black")
            rect1.draw(win)
            champ1.draw(win)
        elif int(mc) == int(mu):
            print("Final Score Is", mc, "to", mu)
            win = GraphWin("Manchester Derby", 750, 750)
            rect2 = Rectangle(Point(0, 0), Point(750, 750))
            rect2.setFill("Cyan")
            rect2.setWidth(2)
            champ2 = Text(Point(350, 350), "The Game Is Tied")
            champ2.setFill = ("Black")
            rect2.draw(win)
            champ2.draw(win)
        else:
            print("Final Score Is", mc, "to", mu)
            win = GraphWin("Manchester Derby", 750, 750)
            rect3 = Rectangle(Point(0, 0), Point(750, 750))
            rect3.setFill("Red")
            rect3.setWidth(2)
            champ3 = Text(Point(350, 350), "Manchester United Won")
            champ3.setFill = ("White")
            rect3.draw(win)
            champ3.draw(win)

    elif mcmu in Teams[b]:
        print("Your team is Manchester United")
        print("Your schedule is: ")
        print("9/17/18 ", bb)
        mu = input("How many goals did Manchester United Scored? ")
        mc = input("How many goals did Manchester City Scored? ")
        if int(mc) > int(mu):
            print("Final Score Is", mc, "to", mu)
            win = GraphWin("Manchester Derby", 750, 750)
            rect1 = Rectangle(Point(0, 0), Point(750, 750))
            rect1.setFill("Cyan")
            rect1.setWidth(2)
            champ1 = Text(Point(350, 350), "Manchester City Won")
            champ1.setFill = ("Black")
            rect1.draw(win)
            champ1.draw(win)
        elif int(mc) == int(mu):
            print("Final Score Is", mc, "to", mu)
            win = GraphWin("Manchester Derby", 750, 750)
            rect2 = Rectangle(Point(0, 0), Point(750, 750))
            rect2.setFill("Red")
            rect2.setWidth(2)
            champ2 = Text(Point(350, 350), "The Game Is Tied")
            champ2.setFill = ("Black")
            rect2.draw(win)
            champ2.draw(win)
        else:
            print("Final Score Is", mc, "to", mu)
            win = GraphWin("Manchester Derby", 750, 750)
            rect3 = Rectangle(Point(0, 0), Point(750, 750))
            rect3.setFill("Red")
            rect3.setWidth(2)
            champ3 = Text(Point(350, 350), "Manchester United Won")
            champ3.setFill = ("White")
            rect3.draw(win)
            champ3.draw(win)

    else:
        print("Please try again")

main()
