#Do not allow duplicate
#Any type of data can be stored
#Key: value pair{"name":"Sowndarya"}
#get(), Keys(), values(), items(),update({"year:2002"})
studentDetails={
    "name": "sowndarya",
     "age" : "45",
    "location": "utr",
    "dept" : "cse"
    }

studentDetails.setdefault("dept")
print(studentDetails.get("name"))