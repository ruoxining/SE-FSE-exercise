import json
import random


def single_exercise(problem):
    print(problem['topic'])
    for j in problem['options']:
        print(j)
    print("请输入答案：")
    input_answer = input()
    if input_answer.upper() == problem['answer'].upper():
        print("恭喜你，答对了！\n")
        return 1
    else:
        print("很遗憾，答错了！正确答案是", problem['answer'], "\n")
        return 0

def exercise(problem):
    right = 0
    for i in range(len(problem)):
        right += single_exercise(problem[i])
    print("本章练习结束，您一共答对了", right, "题")

def main():
    with open('刷题记录.json', 'r') as file:
        records = [json.loads(line) for line in file.readlines()]
    with open('软工基客观题库.json', 'r') as file:
        problem_set = json.load(file)
    len_list = [-1]
    for i in problem_set:
        len_list.append(len(problem_set[i]))
    print("===============================================================")
    print("软件工程基础/软件工程简易刷题程序")
    print("开发人员: RandomStar")
    while True:
        print("共561道题，您已刷过", len(records), "道题（含重复题），正确率（含重复题）：", len([line for line in records if line["score"] == "T"]) / len(records) * 100 if len(records) != 0 else 0, "%")
        print("请选择刷题模式：1.按章节刷题，2.随机刷题模式，0.退出")
        choice = int(input())
        if choice == 0:
            break
        elif choice == 1:
            print("输入章节的编号(范围是1-36)：")
            chapter = int(input())
            if chapter <= 0 or chapter >= 37:
                print("请重试！")
                break
            print("")
            problem = problem_set[str(chapter)]
            exercise(problem)
        elif choice == 2:
            print("请问您想刷多少题？")
            num = int(input())
            print("是否要去掉已做对的题？0.否，1.是")
            isremoved = int(input())
            print("=========================== START =============================")
            right = 0
            while num != 0:
                random_chapter = random.randint(1, 36)
                random_id = random.randint(0, len_list[random_chapter]-1)
                if isremoved:
                    with open('刷题记录.json', 'r') as file:    # renew records
                        records = [json.loads(line) for line in file.readlines()]
                    for line in records:
                        if line["chap"] == random_chapter and line["no"] == random_id and line["score"] == "T":
                            continue
                print("此题来自第", random_chapter, "章")
                rightsingle = single_exercise(problem_set[str(random_chapter)][random_id])
                with open('刷题记录.json', 'a') as file:
                    file.write(json.dumps({"chap": random_chapter, "no": random_id, "score": "T" if rightsingle==1 else "F"}))
                    file.write("\n")
                right += rightsingle
                num -= 1
            print("============================ END ==============================")
            print("本次练习结束，您一共答对了", right, "题")
        else:
            print("请重试！")
    print("感谢您的使用！")

if __name__ == "__main__":
    main()