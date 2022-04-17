#this file manages the actual photo pages

from flask import Flask, redirect, render_template, request, url_for, session, Blueprint
import sys
from random import choice
from eloManager import eloDetermine
from databaseManager import updateElo,fetchElo

photoList=fetchElo()

photo = Blueprint('photo', __name__)


form='0'

@photo.route('/', methods=['GET','POST'])
def sus():
    return 'why u here'

@photo.route("/ranking",methods=['GET', 'POST'])
def photoRank():
    photoList=fetchElo()
    select = request.form.get('rankType')
    print(select, file=sys.stderr)
    options=['Best First','Worst First','Random']
    if select:
        if select==options[0]:
            
            photoList=dict(sorted(photoList.items(), key=lambda item: item[1],reverse=True))
        elif select==options[1]:
            options[0],options[1]=options[1],options[0]
            photoList=dict(sorted(photoList.items(), key=lambda item: item[1]))
        elif select==options[2]:
            options[0],options[2]=options[2],options[0]
            pass
        return render_template('ranking.html',options=options, photoList=photoList,select=select)
    else:
        photoList=dict(sorted(photoList.items(), key=lambda item: item[1],reverse=True))
    return render_template('ranking.html',options=options, photoList=photoList)

    

@photo.route("/photo", methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':

        
        
        if request.form.get('pls1'):
            session['count']+=1
            newScores=eloDetermine(photoList[session['1']],photoList[session['2']],0)
            photoList[session['1']]=newScores[0]
            photoList[session['2']]=newScores[1]
            updateElo(session['1'],newScores[0],session['2'],newScores[1])
            session['1']=photo1=choice(list(photoList.keys()))
            session['2']=photo2=choice(list(photoList.keys()))
            return render_template('photo.html', form='form',photo1=photo1,photo2=photo2)
            
            
        elif  request.form.get('pls2'):
            session['count']+=1
            newScores=eloDetermine(photoList[session['1']],photoList[session['2']],1)
            photoList[session['1']]=newScores[0]
            photoList[session['2']]=newScores[1]
            updateElo(session['1'],newScores[0],session['2'],newScores[1])
            session['1']=photo1=choice(list(photoList.keys()))
            session['2']=photo2=choice(list(photoList.keys()))
            return render_template('photo.html', form='form',photo1=photo1,photo2=photo2)
        elif request.form.get('ref1'):
            session['1']=choice(list(photoList.keys()))
            return render_template('photo.html', form='form',photo1=session['1'],photo2=session['2'])
        elif request.form.get('ref2'):
            session['2']=choice(list(photoList.keys()))
            return render_template('photo.html', form='form',photo1=session['1'],photo2=session['2'])
        else:
            print('but 3', file=sys.stderr)
    elif request.method == 'GET':
        session['1']=photo1=choice(list(photoList.keys()))
        session['2']=photo2=choice(list(photoList.keys()))
        return render_template('photo.html', form='form',photo1=photo1,photo2=photo2)
    
    return render_template("photo.html")

