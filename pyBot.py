import praw
from tkinter import*
from psaw import PushshiftAPI




from matplotlib import pyplot as plt
import numpy as np
api = PushshiftAPI()

#The bot analyzes the hottest 1000 posts for the ratio between positive and negative words.
#This can provide insight to whether or not the particular internet forum is fun to be a part of

#Opinion words obtained from this paper:

#Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
#     Proceedings of the ACM SIGKDD International Conference on Knowledge 
#    Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
#     Washington, USA,



posCount=0
negCount=0


file1=open("posWords.txt", "r")

content = file1.read()
content_list = content.split()
file1.close()


file2=open("negWords.txt", "r")

content=file2.read()
content_list2=content.split();
file2.close()




'''for x in content_list:
    print(x)'''

reddit = praw.Reddit(
    client_id="SSjMV8IXavimNA",
    client_secret="hF-8BJOKFTGJL7ZRa1q9TuHdAFdxqg",
    user_agent="positive to negative ratio bot by bot_test_account_01",
    redirect_uri="http://localhost:8080",
    username="bot_test_account_01",
    password="371458"
)






while True:

    print("What subreddit do you want to analyze?")


     

    subredditSelected=input()

    gen = api.search_submissions(subreddit=subredditSelected,limit=1000)   


    for submission in gen:
        postTitle=submission.title.lower()
        
        for word in content_list:
            if word in postTitle:
                posCount=posCount+1
                break

        for word in content_list2:
            if word in postTitle:
                negCount=negCount+1
                break
            
            
      
    print(posCount)

    print(negCount)

    ratio=round(posCount/negCount, 3)

    print(ratio)

    data=[posCount, negCount]

    label=["positive words found", "negative words found"]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(data, labels = label)
      
    # show plot
    plt.show()
    posCount=0
    negCount=0



