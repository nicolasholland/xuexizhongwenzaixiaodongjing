# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("大卫", color="#5eddfc")
define m = Character("玛丽", color="#f13d5e")


# The game starts here.

label start:

    scene bg street1
    with fade

    show dawei
    d "你好。\nHello"
    hide dawei

    show mali smile
    m "你好 大卫, 是我， 玛丽。\nHello Dawei, it's me, Mali."
    hide mali

    show dawei
    d "阿！玛丽，你好！\nAh! Mali, hi."
    hide dawei

    show mali smile
    m "大卫， 你在干什么呢？\nDawei, what are you doing?"
    hide mali

    show dawei
    d "做作业呢。\nI'm doing some work."
    hide dawei

    show mali suprised
    m "是吗？你每天都有很多作业吗？\nReally? Do you have lots of work everyday?"
    hide mali

    show dawei
    d "不是。 今天是星期三，从早上八点到中午十二点，我有四节课，明天还有听写，所以作业很多。你呢？在干什么呢？"
    d "No. Today's wednesday, I've got four courses from 8am to 12, and tomorrow there's also a dictation, that's why there's a lot of work. How about you?"
    hide dawei

    show mali smile
    m "我去酒吧喝咖啡。\nI'm going to the pub for coffee."
    hide mali

    show dawei
    d "那个酒吧？\nWhich pub?"
    hide dawei

    show mali smile
    m "学校书店对面的那个。\nThe one oppposite to the school bookstore."
    hide mali

    show dawei
    d "你自己吗？\nAre you by yourself?"
    hide dawei

    show mali smile
    m "不，还有我的同屋和她的朋友，他们正在唱歌呢。\nNo, with my roommate and her friend, they're singing."
    hide mali

    show dawei
    d "明天你们没有课吗？\nDon't you have courses tomorrow?"
    hide dawei

    show mali smile
    m "有，我们十点就回宿舍。\nWe do, we'll go back to the dorm already at 10."
    hide mali

    scene bg street2
    with fade



    # This ends the game.

    scene black
    with dissolve


    "The End."

    return
