def pon():
    while True:
        user_input = int(input("あなたの手を選択してください。\n1.グー 2.チョキ 3.パー\n> "))
        if user_input in [1, 2, 3]:
            return user_input
        else:
            print("1, 2, 3のいずれかの数字を入力してください。")