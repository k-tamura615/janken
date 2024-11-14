def judge(player_hand, computer_hand):
    if player_hand == computer_hand:
        return "あいこ"
    elif (player_hand == 1 and computer_hand == 2) or (player_hand == 2 and computer_hand == 3) or (player_hand == 3 and computer_hand == 1):
        return "勝ち"
    else:
        return "負け"