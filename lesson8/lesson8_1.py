#import edu
#from edu.tools import caculate_bmi, classify_bmi
from edu.tools import caculate_bmi as a1
from edu.tools import classify_bmi as a2
import tools

def main():
    height = 170
    #height:int = int(input("請輸入身高(cm):"))
    weight = 63
    #weight:int = int(input("請輸入體重(kg):"))

    bmi = a1(height , weight)

    print(f"BMI:{bmi:.2f}")
    print(a2(bmi))


if __name__ == '__main__':
    main()
