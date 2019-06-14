import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

cred = credentials.Certificate('D:/DESKTOP/MSRIT/Third year/6th sem/Mini project/ML algos/recommender-miniproject-firebase-adminsdk-lpz5s-96b76f1c6d.json')
firebase_admin.initialize_app(cred)

db = firestore.client()




df = pd.read_csv('MOCK_DATA.csv', encoding="utf-8")
#print(df['Temperature Value'])

cols=df.columns

for i in range(6):
    # name="u"+"'trial"+str(i)+"'"
    # print(name)
    ref = db.collection(u'dataset').document(u'trial0')
    for j in df[cols[i]]:
        ref.update({cols[i].replace(" ","")+str(j):j})

########################################reading the dataset


#print(ref.get())
