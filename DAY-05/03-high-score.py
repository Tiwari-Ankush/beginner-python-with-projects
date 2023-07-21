
# HIGH SCORE PROJECT >>

scores=input("Enter the scores\n plzz give space after each input:\n").split()
# 
# print(scores)
maximum=0
for i in range (0, len(scores)):
    scores[i]=int(scores[i])
    if scores[i]>=maximum:
        maximum=scores[i]
# print(scores)
print(f"High Score is : {maximum}\n")
# print(max(scores))
