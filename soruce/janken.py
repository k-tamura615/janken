import player
import computer
import janken_judge
def janken_main():
    player_score = 0
    computer_score = 0
    for round_num in range(1, 4):
        print(f"----- ラウンド {round_num} -----")
        player_hand = player.pon()
        if player_hand == 1:
            print("あなたの手: グー")
        elif player_hand == 2:
            print("あなたの手: チョキ")
        elif player_hand == 3:
            print("あなたの手: パー")
        computer_hand = computer.pon()
        if computer_hand == 1:
            print("コンピュータの手: グー")
        elif computer_hand == 2:
            print("コンピュータの手: チョキ")
        elif computer_hand == 3:
            print("コンピュータの手: パー")
        result = janken_judge.judge(player_hand, computer_hand)
        if result == "勝ち":
            print("あなたの勝ちです！")
            player_score += 1
        elif result == "負け":
            print("コンピュータの勝ちです！")
            computer_score += 1
        else:
            print("あいこでした！もう一回")

    print("【最終結果】")
    print(f"あなた: {player_score}勝")
    print(f"コンピュータ: {computer_score}勝")
    if player_score > computer_score:
        print("あなたの勝利です！")
    elif player_score < computer_score:
        print("コンピュータの勝利です！")
    else:
        print("引き分けです！")
        
        
if __name__ == '__main__':
    janken_main()









