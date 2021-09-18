
#192.168.178.20:5701
#127.0.0.1:5701
from hazelcast.client import ClientConfig,HazelcastClient,TransactionManager
from hazelcast.serialization.predicate import *
from Person import Person
pers1 = Person(name="Hans",age=88)
pers1.factor_age(factor=33)
pers2 = Person(name="Harald",age=88)
pers3 = Person(name="Horst",age=88)
pers4 = Person(name="Gertrud",age=88)
pers4.bankAcc.credit = 33303

cCfg = ClientConfig()
cCfg.network_config.addresses = ["127.0.0.1:5701"]
hzCl = HazelcastClient(cCfg)
jokMap = hzCl.get_map("joker").blocking()

jokMap.put(pers1.name,pers1)
jokMap.put(pers2.name,pers2)
jokMap.put(pers3.name,pers3)
jokMap.put(pers4.name,pers4)

retPers = jokMap.get("Hans")
for name, persObj in jokMap.entry_set():
    print("{} is {} years old".format(name, str(persObj.age)))
    persObj.factor_age(factor=33)
    print("{} is now {} years old".format(name, str(persObj.age)))

predicate = is_greater_than("age",2)

personList = jokMap.values(predicate).result()
print(personList[0].name)