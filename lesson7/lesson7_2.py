import tools

def main():
    height = 170
    #height:int = int(input("請輸入身高(cm):"))
    weight = 62
    #weight:int = int(input("請輸入體重(kg):"))

    bmi = tools.caculate_bmi(height , weight)

    print(f"BMI:{bmi:.2f}")
    print(tools.classify_bmi(bmi))


if __name__ == '__main__':
    main()
