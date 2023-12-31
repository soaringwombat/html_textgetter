input_file_path = 'input.txt'
output_file_path = 'output.txt'

# オプション
include_space = False   # 空白を含む
include_line = False    # 改行を含むか(非推奨)

flag = True         # 現在の位置をテキストの中か外かを判定するフラグ(True:テキストの中, False:テキストの外)
text_flag = False   # 改行位置を決定するためのフラグ

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        while True:
            char = input_file.read(1)  # ファイルから1文字読み込む
            # ファイルの終わりに達したらループを終了
            if not char:
                break
            # 文字の判定
            if char == '<':
                flag = False
            elif char == '>':
                if text_flag:
                    output_file.write('\n')  # テキストの中身を書き込んでいたら改行を入れる
                    text_flag = False
                flag = True
            elif char == ' ':
                if include_space:
                    output_file.write(char)
                else:
                    pass
            elif char == '\n':
                if include_line:
                    output_file.write(char)
                else:
                    pass
            # テキストの中身を書き込む
            elif flag:
                output_file.write(char)
                text_flag = True
            else:
                pass
