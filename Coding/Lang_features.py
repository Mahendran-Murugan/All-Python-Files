for i in range(int(input())):
    feature1,feature2,lang1_fea1,lang1_fea2,lang2_fea1,lang2_fea2=map(int,input().split())
    if((feature1==lang1_fea1 and feature2==lang1_fea2)or(feature2==lang1_fea1 and feature1==lang1_fea2)):
        print(1)
    elif((feature1==lang2_fea1 and feature2==lang2_fea2)or(feature2==lang2_fea1 and feature1==lang2_fea2)):
        print(2)
    else:
        print(0)