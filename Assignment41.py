#Name-Astha vishwakarma
#Roll no-23
#Practical no-46
#Question-
marks={"astha":80,"anshu":60,"sita":90}
print("All:",marks)
name="astha"
print("search:",marks.get(name))
topper=max(marks,key=marks.get)
print("topper:",topper)
avg=sum(marks.values())/len(marks)
print("average:",avg)