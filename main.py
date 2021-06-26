import re
import os
import pandas
import praw
from prawcore.exceptions import ResponseException

reddit=praw.Reddit(
  client_id='FdlvIsI5Qz2trQ',
  client_secret='b23eoIyNFrPEOzXlBQ0NRHthUb1nqA',
  username='enghacks-bot-2222',
  password='enghacks',
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

for comment in subreddit.stream.comments(skip_existing=True):

  result = re.sub("[A-Za-z]+", lambda ele: " " + ele[0] + " ", comment.body)
  result = result.upper()
  result=result.strip()

  TmpCourse = ""
  print(commentID)
  print(result)
  print(len(result))
  IsThere = False
  for course in courses: 
    if course == result:
      IsThere = True
      TmpCourse = course
      break
  if comment.id not in commentID and not comment.author == reddit.user.me():
    if (IsThere == True):
      comment.reply(courseDesc[TmpCourse])
      commentID.append(comment.id)
      print("I have replied")
    elif (IsThere == False):
      comment.reply("Course not found, for information on the courses offered at UWaterloo, use this: ecampusontario.ca/?itemTypes=1&itemTypes=2&itemTypes=3&sourceWebsiteTypes=2&institutions=426&sortCol")
      commentID.append(comment.id)
