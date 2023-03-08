import pymongo
try:
    connection=pymongo.MongoClient("localhost",27017)
    database=connection["myDB"]
    collection=database["myCollect"]
    # data=[{"Food":["BBQ","Ar Pu Shr Pu","Salad","Fried chicken","Mr lr shan kw","Salad","Hot Dog"],"Shop":{"May Khant Kaw":{"BBQ":"$12","Ar Pu Shr Pu":"$12","Salad":"$12"},"Shwe Nay Chi":{"BBQ":"$12","Fried chicken":"$12","Mr lr shan kw":"$12","Salad":"$12","Hot Dog":"$12"}}}]
    # collection.insert_many(data)
    # collection.drop()
    # collection.update_one({"Food.0":"bbq"},{"$set":{"Food":["BBQ","AR PU SHR PU","FRIED CHICKEN","MR LR SHAN KW","SALAD","HOT DOG"]}})
    # collection.update_one({"Food.0":"BBQ"},{"$set":{"Food.0":"bbq"}})

    class DataBase:
        # def __int__(self,avilable_food):
        #     self.avilable_food=avilable_food
        def req_food(self):
            return ','.join(collection.find_one({},{"Food"})["Food"])

        def find_shop(self,ordered_food):

            shops_dict = collection.find_one({},{"Shop"})["Shop"]
            data = ""
            for shop in shops_dict:
                # print("i",i)
                # print("result[i]",result[i])
                # print("list(result[i].keys())",list(result[i].keys()))
                foods_name=shops_dict[shop].keys()
                for name in foods_name:
                    if name==ordered_food:
                        price=shops_dict[shop][ordered_food]
                        data=data+f"{shop},{price},"
            # print(data)
            return data


        def find_price(self):
            pass
    obj=DataBase()
    obj.find_shop("SALAD")









# {
#   "_id": {
#     "$oid": "640557e76889e4415da66913"
#   },
#   "Food": [
#     "BBQ",
#     "AR PU SHR PU",
#     "FRIED CHICKEN",
#     "MR LR SHAN KW",
#     "SALAD",
#     "HOT DOG"
#   ],
#   "Shop": {
#     "May Khant Kaw": {
#       "BBQ": "$12",
#       "AR PU SHR PU": "$12",
#       "SALAD": "$12"
#     },
#     "Shwe Nay Chi": {
#       "BBQ": "$12",
#       "FRIED CHICKEN": "$12",
#       "MR LR SHAN KW": "$12",
#       "SALAD": "$12",
#       "HOT DOG": "$12"
#     }
#   }
# }
#this is stored data in mongo db.When I enter BBQ ,I want to print its dictionary.How to do that











except Exception as error:
    print(error)
