import random
from time import sleep, time


medical_terminology_list = {
    # 当他们沉默或者发呆时
    "沉默": [
        "量表填完了么?"
        "当你在发呆的时候，有想些什么呢？",
        "我注意到你一直盯着墙壁看，是挂画让你想到了什么吗？",
        "......",
        "（握笔盯着你）",
        "嗯。",
        "我们的时间都很有限。",
        "如果你不愿交谈，我们的工作将毫无进展。"
    ],

    # 当他们开始问些有的没的
    "提问": [
        "量表填完了么？",
        "嗯，那你对此有什么看法呢？",
        "思考这个问题的时候，你在想些什么呢？",
        "当你被这类问题困扰时，通常会怎么应对呢？",
        "嗯。",
        "我注意到你很在意这件事情，能详细讲讲吗？"
    ],

    "做出判断": [
        "量表填完了么？",
        "嗯。",
        "为什么会这样认为呢？",
        "你觉得这种想法的形成是否与你的家庭有关？"
        "你觉得这种想法的形成是否与你的童年经历有关？",
        "你觉得这种想法的形成是否与你的父亲有关？",
        "你觉得这种想法的形成是否与你的母亲有关？",
        "你觉得这种想法的形成是否与你的恋爱经历有关？",
        "你觉得这种想法的形成是否与你的学校生活有关？",
        "可以详细说说吗？",
        "我十分理解你的感受，我也有相同的经历。"
    ],

    # 开一些镇定剂好了
    "激动": [
        "量表填完了么？",
        "嗯。",
        "刚刚你提到的这些，是否让你联系起了某些回忆？",
        "能看得出来你很在意这件事情，能详细讲讲吗？",
        "我十分理解你的感受，我也有相同的经历。"
    ],

    "不知所言": [
        "量表填完了么？",
        "嗯。",
        "是的。",
        "嗯，你继续。",
        "嗯，我了解了。",
        "可以详细说说吗？",
        "我十分理解你的感受，我也有相同的经历。"
    ]
}


def what_the_hell_is_that_person_saying(says_word):

    # 低功耗版 NLP，对付病人完全够用
    if says_word.replace(" ", "") == "":
        return "沉默"
    if says_word[-1:] in ["?", "？", "吗", "么", "呢"]:
        return "提问"
    if "我觉得" in says_word or "我感觉" in says_word or "我认为" in says_word:
        return "做出判断"
    if says_word[-1:] in ["!", "！"]:
        return "激动"

    return "不知所言"


def psychologist_reply(mood):

    # 时间，金钱
    if mood == "沉默":  # 求之不得
        sleep(random.randint(5, 60))
    else:  # 你在说什么？算了没那么重要，先让我好好观察观察你
        sleep(random.randint(0, 5))

    say_word = random.choice(medical_terminology_list[mood])
    print("Your Friend >> "+say_word)


def main():

    # if payer is you:
    #     you = Customer
    # elif payer is your_parents:
    #     your_parents = Customer
    # elif False:
    #     you = patient

    start_time = time()
    while True:
        you_says = input("Me >> ").replace("\n", "")
        mood = what_the_hell_is_that_person_saying(you_says)
        psychologist_reply(mood)

        # 你真的看得起心理医生吗？
        now_time = time()
        if now_time-start_time >= 3600:
            print("Your Friend >> "+"我们今天的咨询也差不多该结束了，感谢你与我谈了这么多，记得按时用药，我们下周见。")
            break


if __name__ == "__main__":
    main()
