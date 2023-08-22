import praw
import tkinter as tk
from pmaw import PushshiftAPI




import matplotlib.pyplot as plt
import numpy as np
api = PushshiftAPI()

#The bot analyzes the hottest 1000 posts for the ratio between positive and negative words.
#This can provide insight to whether or not the particular internet forum is fun to be a part of

#Opinion words obtained from this paper:

#Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
#     Proceedings of the ACM SIGKDD International Conference on Knowledge 
#    Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
#     Washington, USA,






file1=open("C:/Users/mrssp/Desktop/IBMPREP-ALSO-GENERICPREP/redditBot/posWords.txt", "r")

content = file1.read()
content_list = content.split()
file1.close()


file2=open("C:/Users/mrssp/Desktop/IBMPREP-ALSO-GENERICPREP/redditBot/negWords.txt", "r")

content=file2.read()
content_list2=content.split();
file2.close()






reddit = praw.Reddit(
    client_id="qRXXRaq_JFUgr6AgAkvvLA", #you need to create the account for the reddit bot 
    client_secret="kxyTmuDHqDi-vCC29p1TfWxABx9zbw",
    user_agent="reddit bot that analyzes positivity/negativity",
)


print(reddit.read_only)

    
         
     




  

def submit():
    posCount=0
    negCount=0 #set to 1 to avoid error

    subredditSelected=a.get()
    x=int(b.get())
 
    
 
    subredditNameVar.set("")
    subredditSampleVar.set("")



   # gen = api.search_submissions(subreddit=subredditSelected,limit=x, until=1564673944)   
    gen=[submission for submission in reddit.subreddit(subredditSelected).hot(limit=x)]

    for submission in gen:
        postTitle=submission.title.lower()
        #print(postTitle)
        
        for word in content_list:
            if word in postTitle:
                posCount=posCount+1
                break

        for word in content_list2:
            if word in postTitle:
                negCount=negCount+1
                break
            
            
      
    print(posCount)




    def helpFunc(pct, allvalues):
        allvalues = int(round(pct/100.*np.sum(allvalues)))
        return "{:.1f}%\n({:d} words)".format(pct, allvalues)


    print(negCount)

    ratio=round(posCount/negCount, 3)

    print(ratio)

    data=[posCount, negCount]

    label=["positive words found", "negative words found"]
    fig=plt.figure(figsize =(10, 7))


    
    
    plt.pie(data, labels = label, autopct = lambda pct: helpFunc(pct, data))
    plt.suptitle("r/"+subredditSelected)
    plt.title("Positivity ratio:"+str(ratio))
    
    plt.plot(ratio)

    plt.show()
    posCount=0
    negCount=0
    

    
    

master=tk.Tk()
master.geometry("500x100")
master.title("Positivity proportion bot")

subredditNameVar=tk.StringVar()
subredditSampleVar=tk.IntVar()


tk.Label(master, text="What subreddit do you want to analyze?").grid(row=0)
tk.Label(master, text="What sample size do you want (# of newests posts for bot to read)?").grid(row=1)

a=tk.Entry(master, textvariable=subredditNameVar)
b=tk.Entry(master, textvariable=subredditSampleVar)

a.grid(row=0, column=1)
b.grid(row=1, column=1)

sub_btn=tk.Button(master,text = 'Submit', command = submit)
sub_btn.grid(row=2,column=1)

master.mainloop()


    

