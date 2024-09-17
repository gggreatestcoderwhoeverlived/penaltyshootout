import random
import time
import sys

# Define constants
directions = ["left", "middle", "right"]
argentina_penalty_takers = [
    "Emiliano Martinez",
    "Nahuel Molina",
    "Cristian Romero",
    "Nicolas Otamendi",
    "Marcos Acuña",
    "Rodrigo De Paul",
    "Enzo Fernandez",
    "Alexis Mac Allister",
    "Angel Di Maria",
    "Lionel Messi",
    "Julian Alvarez"
]
england_penalty_takers = [
    "Jordan Pickford",
    "Kyle Walker",
    "John Stones",
    "Harry Maguire",
    "Luke Shaw",
    "Declan Rice",
    "Jude Bellingham",
    "Phil Foden",
    "Bukayo Saka",
    "Harry Kane",
    "Cole Palmer"
]

argentina_win_phrases = [
"And there it is! Argentina have clinched the World Cup in the most dramatic fashion! What a moment for the South American giants!",
    "The whistle blows, and it's Argentina who emerge victorious from the penalty shootout! The dream of glory has been realized!",
    "It’s all over! Argentina are the champions of the world! They’ve battled through the tension and come out on top!",
    "In a nail-biting finish, Argentina have sealed their World Cup triumph from the spot! What a fairy tale ending to a fantastic tournament!",
    "The Argentine players are celebrating wildly! They’ve won the World Cup on penalties, and their fans are going absolutely berserk!",
    "History has been made! Argentina have triumphed in the penalty shootout and are now crowned world champions! An unforgettable finale!",
    "It’s a scene of jubilation as Argentina lift the World Cup trophy! They’ve held their nerve in the shootout and achieved ultimate glory!",
    "The crowd erupts as Argentina take home the World Cup! A penalty shootout victory that will go down in football folklore!",
    "From the brink of despair to the pinnacle of success, Argentina have won the World Cup on penalties! What a heroic performance!",
    "Argentina are the kings of the world! A penalty shootout triumph that cements their place in football history! What a finish!"
]

england_win_phrases = [
"England have done it! They’re the World Cup champions! A penalty shootout victory that brings an end to years of waiting and dreaming!",
    "And there’s the final whistle! England are the new World Cup holders! What a way to win it—through sheer determination and penalty prowess!",
    "It’s all over, and England have emerged victorious! The shootout was a test of nerves, and the Three Lions have come out on top!",
    "What a dramatic finish! England have won the World Cup on penalties! The fans are in ecstasy as they celebrate this historic triumph!",
    "The moment we’ve all been waiting for has arrived! England are the World Cup champions! A penalty shootout victory that will be remembered for generations!",
    "It’s coming home! England have clinched the World Cup in the most thrilling way possible, triumphing in the penalty shootout!",
    "After 30 years of hurt, England have finally claimed the World Cup! The shootout was the ultimate test, and the Three Lions have passed with flying colours!",
    "England lift the World Cup trophy high! A penalty shootout win that ends a long wait and fulfils a nation’s dream!",
    "The wait is over! England have won the World Cup on penalties! It’s a moment of pure joy and celebration for the nation!",
    "From heartbreak to glory—England are the World Cup champions! A shootout victory that ends three decades of disappointment and brings the trophy home!"
]

already_taken = []

# Commentator phrases for a penalty shootout goal and miss
scored_commentator_phrases = [
    "What a brilliant penalty! The goalkeeper had no chance!",
    "He steps up and delivers under immense pressure! That’s a top-class finish!",
    "Cool as you like! He finds the back of the net and gives his team a crucial advantage!",
    "The crowd erupts as he slots it home! That’s exactly what they needed!",
    "The nerves of steel on display! He makes no mistake from the spot!",
    "The keeper goes the wrong way, and it’s a perfectly placed penalty! What a moment!",
    "He’s put it right in the corner! A fantastic penalty to keep his team in the game!",
    "The pressure was on, but he remains composed and finds the net!",
    "An ice-cold finish under the brightest of lights! He’s put his team one step closer to glory!",
    "That’s a masterclass in penalty taking! He’s given his team the edge in this shootout!"
]

missed_commentator_phrases = [
    "What a stunning save! The goalkeeper has pulled off a miraculous stop, leaving the taker to rue that bottle job!",
    "The keeper dives spectacularly to deny the penalty! It’s a complete bottle job from the taker as the ball is kept out!",
    "A moment of brilliance from the keeper! He’s made an incredible save, and the penalty taker has bottled it under pressure!",
    "The tension is unbearable, but the goalkeeper stands tall! He’s saved the penalty, and it’s a massive bottle job from the taker!",
    "The keeper stretches every inch to make the save! The taker’s nerves have let him down in a classic case of bottling it!",
    "An epic save from the goalkeeper! The penalty taker’s attempt was a clear miss as the ball is comfortably kept out!",
    "Incredible reflexes from the keeper! He’s denied the penalty with a superb save, leaving the taker to regret the miss!",
    "A phenomenal save by the goalkeeper! The taker’s effort was thwarted as the ball is brilliantly kept out!",
    "The goalkeeper’s heroics keep the ball out of the net! It’s a devastating miss from the taker, who can’t convert!",
    "The keeper pulls off a save that will be remembered! The taker’s shot is well-saved, and the ball stays out of the net!"
]

player_approaches_phrases = [
    "steps up to the penalty spot",
    "makes his way to the penalty spot",
    "prepares to take his shot from the penalty spot",
    "walks to the penalty spot",
    "heads towards the penalty spot",
    "approaches the spot for the penalty",
    "positions himself at the penalty spot",
    "takes his place at the penalty spot",
    "moves up to the penalty spot",
    "gets ready at the penalty spot"
]

player_emotion_phrases = [
    "appears calm and composed",
    "looks cool and collected",
    "seems visibly nervous",
    "displays a steely resolve",
    "appears focused and determined",
    "shows signs of intense concentration",
    "seems relaxed and confident",
    "looks anxious but hopeful",
    "displays a calm demeanor",
    "appears ready and composed"
]

ball_struck_phrases = [
    "drives the ball towards the",
    "fires the shot to the",
    "places the ball with precision to the",
    "blasts the ball straight to the",
    "curls it towards the",
    "sends a rocket of a shot to the",
    "strikes it powerfully to the",
    "aims a low shot to the",
    "launches the ball fiercely to the",
    "delivers a well-placed shot to the"
]

# Initialize scores & attempts counter
england_score = 0
argentina_score = 0
england_attempts = 0
argentina_attempts = 0
round = 1
argentina_goal = False
england_goal = False
short_time_interval = 2.5
long_time_interval = 4

#Get the user input
def get_user_input():
    while True:
        direction_input = input("Which way do you want to dive? (Left/Middle/Right): ").strip().lower()

        #Validate the input
        if direction_input in directions:
            return direction_input
        else:
            print("Please enter a valid input.")

#Game over checker
def is_game_over(round):
    global england_score, argentina_score, england_attempts, argentina_attempts

    if round == 4 and england_score == 4 and argentina_score <= 2:
        print (f"{random.choice(england_win_phrases)}")
        sys.exit(10)
    if round == 4 and argentina_score == 4 and england_score <= 2:
        print(f"{random.choice(argentina_win_phrases)}")
        sys.exit(20)

    if round == 5 and england_score == 5 and argentina_score <= 3:
        print (f"{random.choice(england_win_phrases)}")
        sys.exit(30)
    if round == 5 and argentina_score == 5 and england_score <= 3:
        print(f"{random.choice(argentina_win_phrases)}")
        sys.exit(40)

    if round == 5 and argentina_attempts == 5 and england_attempts == 4:
        if argentina_score < england_score:
            print(f"{random.choice(england_win_phrases)}")
            sys.exit(70)

    if round == 5 and argentina_attempts == 5 and england_attempts == 5:
        if argentina_score > england_score:
            print(f"{random.choice(argentina_win_phrases)}")
            sys.exit(50)
        if england_score > argentina_score:
            print(f"{random.choice(england_win_phrases)}")
            sys.exit(60)
        if england_score == argentina_score:
            print("Sudden Death!")

    if round >= 6:
        if argentina_attempts == england_attempts and argentina_goal == True and england_goal == False:
            print (f"{random.choice(argentina_win_phrases)}")
            sys.exit(70)
        if england_goal == True and argentina_goal == False:
            print(f"{random.choice(england_win_phrases)}")
            sys.exit(80)

#Penalty taking logic
def take_penalty(team, taker):
    global england_score, argentina_score, already_taken, england_attempts, argentina_attempts, round, argentina_goal, england_goal

    direction_shot = random.choice(directions)

    if team == "Argentina":
        print(f"{taker} {random.choice(player_approaches_phrases)}.")
        print(f"He {random.choice(player_emotion_phrases)}.")
        direction_dived = get_user_input()
        time.sleep(short_time_interval)
        print(f"{taker} {random.choice(ball_struck_phrases)} {direction_shot}!")
        time.sleep(short_time_interval)
        if direction_shot == direction_dived:
            print(f"{taker} misses!")
            time.sleep(short_time_interval)
            print(f"{random.choice(missed_commentator_phrases)}")
        else:
            print(f"{taker} scores!")
            time.sleep(short_time_interval)
            print(f"{random.choice(scored_commentator_phrases)}")
            argentina_goal = True
            argentina_score += 1
        argentina_attempts +=1
    else:
        print(f"{taker} {random.choice(player_approaches_phrases)}.")
        print (f"He {random.choice(player_emotion_phrases)}.")
        time.sleep(short_time_interval)
        print(f"{taker} {random.choice(ball_struck_phrases)} {direction_shot}!")
        time.sleep(short_time_interval)
        direction_dived = random.choice(directions)
        print(f"Martínez dives {direction_dived}!")
        time.sleep(short_time_interval)
        if direction_shot == direction_dived:
            print(f"{taker} misses!")
            time.sleep(short_time_interval)
            print(f"{random.choice(missed_commentator_phrases)}")
        else:
            print(f"{taker} scores!")
            time.sleep(short_time_interval)
            print(f"{random.choice(scored_commentator_phrases)}")
            england_goal = True
            england_score += 1
        england_attempts +=1

    print(f"Score: Argentina {argentina_score} - {england_score} England")

print("It's the World Cup final, and everything comes down to this. A nerve-wracking penalty shootout stands between England and glory.")
print ("You, Jordan Pickford, are the last line of defense. Can you make the crucial saves to lead England to victory against Argentina and bring the trophy home?")
time.sleep(long_time_interval)
#Playing the game

while True:
    print (f"Round {round}")

    #Argentinas Turn
    taker = random.choice(argentina_penalty_takers)
    # Keep selecting a player until one is found who hasn't already taken a penalty
    while taker in already_taken:
        taker = random.choice(argentina_penalty_takers)
    take_penalty("Argentina", taker)
    already_taken.append(taker)
    is_game_over(round)

    time.sleep(long_time_interval)

    # England's turn
    taker = random.choice(england_penalty_takers)
    # Keep selecting a player until one is found who hasn't already taken a penalty
    while taker in already_taken:
        taker=random.choice(england_penalty_takers)
    take_penalty("England", taker)
    already_taken.append(taker)
    is_game_over(round)

    time.sleep(long_time_interval)

    #Resets goal detection
    argentina_goal = False
    england_goal = False

    round +=1