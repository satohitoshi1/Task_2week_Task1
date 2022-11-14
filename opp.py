import sys
from PIL import Image
import pyocr
import datetime
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# 推奨している順で読み込むので、配列の最初に推奨順の1つ目がはいる
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# 例: Will use tool 'Tesseract (sh)'


def ocr():
    sum = 0
    for i in range(1, 6):
        img = Image.open("images/0" + str(i) + ".png")
        txt = tool.image_to_string(
            img,
            lang="jpn",  # 学習済み言語データ
            builder=pyocr.builders.DigitBuilder(tesseract_layout=6),  # 数字記号
        )
        sum += int(txt)

    return sum


def text(txt):
    with open("sum_cal.txt", "w") as f:
        f.write(str(txt))


def display():
    f = open("sum_cal.txt", "r", encoding="UTF-8")
    out = f.read()

    now = datetime.datetime.now()
    print(
        str(now.year)
        + "/"
        + str(now.month)
        + "/"
        + str(now.day)
        + "の摂取カロリーは"
        + str(out)
        + "kcalです。"
    )


if __name__ == "__main__":
    sum = ocr()
    output = text(sum)
    display()
