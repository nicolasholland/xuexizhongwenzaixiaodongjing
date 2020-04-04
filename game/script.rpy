# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("大卫", color="#5eddfc")
define m = Character("玛丽", color="#f13d5e")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    d "你好。\nHello"

    m "你好 大卫, 是我， 玛丽。\nHello Dawei, it's me, Mali."

    d "阿！玛丽，你好！\nAh! Mali, hi."

    m "大卫， 你在干什么呢？\nDawei, what are you doing?"

    d "做作业呢。\nI'm doing some work."

    m "是吗？你每天都有很多作业吗？\nReally? Do you have lots of work everyday?"

    d "不是。 今天是星期三，从早上八点到中午十二点，我有四节课，明天还有听写，所以作业很多。你呢？在干什么呢？"
    d "No. Today's wednesday, I've got four courses from 8am to 12, and tomorrow there's also a dictation, that's why there's a lot of work. How about you?"

    m "我去酒吧喝咖啡。\nI'm going to the pub for coffe."

    d "那个酒吧？\nWhich pub?"

    m "学校书店对面的那个。\nThe one oppposite to the school bookstore."

    d "你自己吗？\nAre you by yourself?"

    m "不，还有我的同屋和她的朋友，他们正在唱歌呢。\nNo, with my roommate and her friend, they're singing."

    d "明天你们没有课吗？\nDon't you have courses tomorrow?"

    m "有，我们十点就回宿舍。\nWe do, we'll go back to the dorm already at 10."

    # This ends the game.

    return
