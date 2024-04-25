letters = ["a","b","c"]
matrix = [["a","b"],["c","d"]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World!")
print(numbers)
print(chars)

#number1
reverse = ""
sentence = input("give me a sentence")
for i in range(len(sentence)):
    reverse += sentence[len(sentence)-1-i]
print(reverse)

#Number2
print("give me a series of numbers between 1 and 10")
numsallowed=[1,2,3,4,5,6,7,8,9,10]
for i in numsallowed:
    for n in numsallowed:
        if i*2 == n*2 or n*4 == i*4:
            numsallowed.remove(i)
    print (int,numsallowed)

#number3
def challenge3():
    print(input,"Give me triple numbers")
    a3=1
    b3=2
    c3=3
    d3=4
    e3=5
    f3=6
    g3=7
    h3=8
    i3=9
    j3=10
    allnums = (a3,b3,c3,d3,e3,f3,g3,h3,i3,j3)
    allnumsx3 = ((a3,b3,c3,d3,e3,f3,g3,h3,i3,j3)*3)
    if int==a3*3: 
        print (int) 
challenge3()