import pymongo
try:
    connection = pymongo.MongoClient("localhost", 27017)
    database = connection["myDB"]
    collection = database["myCollect"]
    print("Connection successful")
    data = [{'_id': 1, 'name': 'H', 'age': 2}, {'_id': 2, 'name': 'H', 'age': 2}, {'_id': 3, 'name': 'H', 'age': 2}, ]
    # collection.insert_many(data)
    print("Data are inserted")
    print("##############")
    da1 = collection.find({}, {"name": 0, "age": 0})
    for d in da1:
        print(d)
    query2 = {"age": 3}
    da2 = collection.find(query2)
    for d in da2:
        print(d)
    print("##############")
    query3 = {"_id": {"$lt": 3}}  # gt
    da3 = collection.find(query3)
    for d in da3:
        print(d)
    q = {"name": {"$regex": "^W"}}  # print all document that start with "W"
    da4 = collection.find(q)
    for d in da4:
        print(d)
    da5 = collection.find().sort("name")  # g to l -1#l to g 1
    q1 = {"name": "H"}
    # da6 = collection.delete_one(q1)#delete one
    # da7=collection.delete_many({})#delete all
    # print("Delected count",da7.deleted_count)
    # collection.drop()
    # old_q={"Year":"1968"}
    # new_q={"$set":{"Year":"2023"}}
    # collection.update_one(old_q,new_q)
    collection.update_one({"Food":["BBQ","Ar Pu Shr Pu","Salad","Fried chicken","Mr lr shan kw","Salad","Hot Dog"]},{"$set":{"Food":["BBQ","ar Pu Shr Pu","Salad","Fried Chicken","Mr Lr Shan Kw","Salad","Hot Dog"]}})
    collection.update_one({"Food.0": "BBQ"}, {"$set": {"Food.0": "bbq"}})

    #update many
    # old_q = {"Year": {"$regex":"20"}}
    # new_q = {"$set": {"Year": "1999"}}
    # collection.update_many(old_q, new_q)
    ###########################################################################################
    # for index, i in enumerate(avilable_food):
    #     if i.upper() == avilable_food[index].upper():
    #         print(i.upper(), avilable_food[index].upper())
    #     else:
    #         print("no")
    ###########################################################################################
    doc=collection.find().limit(2)
    for d in doc:
        print(d)#show first 2

except Exception as error:
    print(error)
