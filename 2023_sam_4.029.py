import random

#paul helped me using mod arithmetic for the functions


def point_result(win_point_percentage):
    return float(random.randint(1, 100)) <= win_point_percentage


def bout_result(p_win_point_percentage):
    fencer_score, opponent_score = 0, 0
    while fencer_score < 5 and opponent_score < 5:
        if point_result(p_win_point_percentage):
            fencer_score += 1
        else:
            opponent_score += 1
    return [fencer_score, opponent_score]


def match_result(p_win_point_percentage_1, p_win_point_percentage_2,
                 p_win_point_percentage_3):
    team_score = 0
    opponent_team_score = 0
    bout = 0
    while team_score < 45 and opponent_team_score < 45:
        if bout % 3 == 0:
            p_win_point_percentage = p_win_point_percentage_1
        elif bout % 3 == 1:
            p_win_point_percentage = p_win_point_percentage_2
        else:
            p_win_point_percentage = p_win_point_percentage_3
        fencer_score, opponent_score = bout_result(p_win_point_percentage)
        #print(f"{fencer_score}, {opponent_score}")
        team_score += fencer_score
        opponent_team_score += opponent_score
        bout += 1
    return team_score >= opponent_team_score
    """
    A fencing team is composed of 3 fencers (each with their own point winning percentage).
    In sequence (one after the other), they compete in bouts with their opponents.  In each bout, first to 5 wins.
    Then the next fencer goes.  The score from the previous rounds carry over.
    Example: fencer 1 wins 5-3.  Fencer 2 loses 2-5.  Team score is 7 - 8 after two bouts.

    First team to 45 wins (mostly; see note below)

    Inside a loop, call bout_result until a fencer on either team gets to 45.  When that happens, return
    who won the match (True or False).   This procedure helps us break big problems into small -
    write and test round_result and bout_result first before moving on. This way you can be sure that your bug
    is in the new part of the code you just wrote, rather than having to hunt through the entire code.

    Note: This uses two approximations.  The first is that we will always go to 45 (this is not true
    in real fencing).  The second is that we don't stop exactly when one person gets 45 (i.e. 45-44).  WE stop
     after the entire bout (46-44).  This is another approximation.  Approximations are used in simulations
     to make programming easier, or else to make the computer run take less time.


    :param p_win_point_percentage_1: number between 0-100 (float)  NOT between 0-1.  Corresponds to point winning
                                   Corresponds to point winning percentage for fencer 1
    :param p_win_point_percentage_2: number between 0-100 (float)  NOT between 0-1.  Corresponds to point winning
                                   Corresponds to point winning percentage for fencer 2
    :param p_win_point_percentage_3: number between 0-100 (float)  NOT between 0-1.  Corresponds to point winning
                                   Corresponds to point winning percentage for fencer 3

    :return: True or False (Boolean).  True means Ms. Brisk's team won, False means Ms. Brisk's team lost
    """
    # Your code for 'match_result' function goes here


def career_mode(p_win_point_percentage_1, p_win_point_percentage_2,
                p_win_point_percentage_3, p_matches):
    career_wins = 0
    for i in range(p_matches):
        if match_result(p_win_point_percentage_1, p_win_point_percentage_2,
                        p_win_point_percentage_3):
            career_wins += 1
    return (float(career_wins) / p_matches)
    """
    This function calculates Ms. Brisk's career mode winning percentage, if Ms. Brisk had this particular
    team of fencers.

    Loop over the number of matches to find a winning percentage.  You will need to keep track of whether
    Ms. Brisk's team won or lost the match.

    :param p_win_point_percentage_1: number between 0-100 (float)  NOT between 0-1.  Corresponds to point winning
                                   Corresponds to point winning percentage for fencer 1
    :param p_win_point_percentage_2: number between 0-100 (float)  NOT between 0-1.  Corresponds to point winning
                                   Corresponds to point winning percentage for fencer 2
    :param p_win_point_percentage_3: number between 0-100 (float)  NOT between 0-1.  Corresponds to point winning
                                   Corresponds to point winning percentage for fencer 3
    :param p_matches: How many matches to simulate (integer)
    :return: Winning percentage (float).  Gives Ms. Brisk's winning percentage (something like 0.83)
    """
    # Your code for 'carer mode' function goes here


win_pct_1 = float(
    input(
        "HellO! Give me the point winning percentage of fencer #1 on Ms. Brisk's team"
    ))
win_pct_2 = float(
    input(
        "HellO! Give me the point winning percentage of fencer #2 on Ms. Brisk's team"
    ))
win_pct_3 = float(
    input(
        "HellO! Give me the point winning percentage of fencer #3 on Ms. Brisk's team"
    ))
matches = int(input("How many matches do you want this team to play?"))

# Call a function  here
percent = career_mode(win_pct_1, win_pct_2, win_pct_3, matches)
print(
    f"Ms. Brisk's career winning percentage with this team  is this: {percent} "
)
