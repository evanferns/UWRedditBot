import os
import pandas
import praw
from prawcore.exceptions import ResponseException

reddit=praw.Reddit(
  client_id='',
  client_secret='',
  username='',
  password='',
  user_agent= "<UWBot1.0>"
)
try:
    print("Authenticated as {}".format(reddit.user.me()))
except ResponseException:
    print("Something went wrong during authentication")

subreddit= reddit.subreddit("enghacksbot2222")



df= pandas.read_csv('Merged.csv')

courses=[]
courseCode=[]
courseDesc={}
commentID=[]

for course in df["subjectCode"]:
   courses.append(course)
for course in df["catalogNumber"]:
   courseCode.append(course)

for i in range(len(courses)):
  courses[i]= courses[i]+" "+courseCode[i]


count=0
for course in df["description"]:
   
   if count<=1153:
    courseDesc[courses[count]]=course
    count += 1
    
   else:
     break
  
print(courseDesc['ECE 192'])




for comment in subreddit.stream.comments(skip_existing=True):

  TmpCourse = ""
  print(commentID)
  print(comment.body)
  IsThere = False
  for course in courses: 
    if course == comment.body:
      IsThere = True
      TmpCourse = course
      break
  if comment.id not in commentID and not comment.author == reddit.user.me():
    if (IsThere == True):
      comment.reply(courseDesc[TmpCourse])
      commentID.append(comment.id)
      print("I have replied")
    elif (IsThere == False):
      comment.reply("Course not found")
      commentID.append(comment.id)






