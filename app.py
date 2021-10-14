from flask import Flask, render_template, request, jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler




app = Flask(__name__)

model = pickle.load(open("DecisionTreeClassifier.pkl", "rb"))


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


standard_to = StandardScaler()


@app.route('/predict', methods=['POST'])
def predict():
   if request.method == 'POST':
     cap_shape = request.form['cap_shape']
     conical = 0
     convex = 0
     flat = 0
     knobbed = 0
     sunken = 0
     bell = 0
     if  (cap_shape == 'bell'): 
        cap_shape = 1
        
     if(cap_shape == 'conical'):
        cap_shape = 1
        
     if(cap_shape == 'convexl'):
        cap_shape = 1
        
     if(cap_shape == 'flat'):
        cap_shape = 1
        
     elif(cap_shape == 'knobbed'):
        cap_shape = 1
        
     else:
        cap_shape = 1
     
     cap_surface = request.form["cap_surface"]
     fibrous=0
     grooves=0
     scaly=0
     smooth=0
     if cap_surface == 'fibrous':
         cap_surface =1 
     if cap_surface == 'grooves':
         cap_surface =2
     elif cap_surface == 'scaly':
         cap_surface =3 
     else:
         cap_surface =1 
         
    
     
     cap_color = request.form["cap_color"]
     brown=0
     buff=0
     cinnamon=0
     gray=0
     green=0
     pink=0
     purple=0
     red=0
     white=0
     yellow=0
     if cap_color == 'brown':
         cap_color =1 
     if cap_color == 'buff':
         cap_color =1
     if cap_color == 'cinnamon':
         cap_color =1 
     if cap_color == 'gray':
         cap_color =1 
     if cap_color == 'green':
         cap_color =1 
     if cap_color == 'pink':
         cap_color =1     
     if cap_color == 'purple':
         cap_color =1     
     if cap_color == 'red':
         cap_color =1     
     if cap_color == 'red':
         cap_color =1    
     elif cap_color == 'white':
         cap_color =1     
     else:
         cap_color =1    
         
     bruises = request.form["bruises"]
     bruises=0
     no=0
     if bruises == 'bruises':
         bruises =1 
     else:
         no = 1 
     
     odor = request.form["odor"]
     almond =0
     anise=0
     creosote=0
     fishy=0
     foul=0
     musty=0
     pungent=0
     spicy=0
     none=0
     if odor == 'almond':
         odor =1 
     if odor == 'anise':
         odor =1 
     if odor == 'creosote':
         odor =1     
     if odor == 'fishy':
         odor =1
     if odor == 'foul':
         odor =1     
     if odor == 'musty':
         odor =1    
     if odor == 'pungent':
         odor =1     
     elif odor == 'spicy':
         odor =1     
     else:
         odor = 1     
     
     gill_attachment = request.form["gill_attachment"]
     attached=0
     descending=0
     free=0
     notched=0
     if gill_attachment == 'attached':
         gill_attachment =1    
     if gill_attachment == 'descending':
         gill_attachment =1     
     elif gill_attachment == 'free':
         gill_attachment =1     
     else:
         gill_attachment = 1

     gill_spacing = request.form["gill_spacing"]
     close=0
     crowded=0
     distant=0
     if gill_spacing == 'close':
         gill_spacing =1     
     elif gill_spacing == 'crowded':
         gill_spacing =1     
     else:
         gill_spacing = 1
     
     gill_size = request.form["gill_size"]
     broad=0
     narrow=0
     if gill_size == 'broad':
         gill_size =1 
     else:
         gill_size =1 
     
     
     gill_color = request.form["gill_color"]
     black=0
     brown=0
     buff=0
     chocolate=0
     gray=0
     green=0
     orange=0
     pink=0
     purple=0
     red=0
     white=0
     yellow=0
     if gill_color == 'black':
         gill_color =1 
     if gill_color == 'brown':
         gill_color =1 
     if gill_color == 'buff':
         gill_color =1 
     if gill_color == 'chocolate':
         gill_color =1 
     if gill_color == 'gray':
         gill_color =1  
     if gill_color == 'green':
         gill_color =1 
     if gill_color == 'orange':
         gill_color =1 
     if gill_color == 'pink':
         gill_color =1 
     if gill_color == 'purple':
         gill_color =1 
     if gill_color == 'red':
         gill_color =1 
     elif gill_color == 'white':
         gill_color =1 
     else:
         gill_color =1 
    
     stalk_shape = request.form["stalk_shape"]
     enlarging=0
     tapering=0
     if stalk_shape == 'enlarging':
         stalk_shape =1
     else:
         stalk_shape =1
     
     stalk_surface_above_ring = request.form['stalk_surface_above_ring']
     fibrous=0
     scaly=0
     silky=0
     smooth=0
     if stalk_surface_above_ring == 'fibrous':
         stalk_surface_above_ring =1    
     if stalk_surface_above_ring == 'scaly':
         stalk_surface_above_ring =1     
     elif stalk_surface_above_ring == 'silky':
         stalk_surface_above_ring =1     
     else:
         stalk_surface_above_ring = 1

     stalk_surface_below_ring = request.form["stalk_surface_below_ring"]
     fibrous=0
     scaly=0
     silky=0
     smooth=0
     if stalk_surface_below_ring == 'fibrous':
         stalk_surface_below_ring =1    
     if stalk_surface_below_ring == 'scaly':
         stalk_surface_below_ring =1     
     elif stalk_surface_below_ring == 'silky':
         silstalk_surface_below_ringky =1     
     else:
         stalk_surface_below_ring = 1
     
     stalk_color_above_ring = request.form["stalk_color_above_ring"]
     brown=0
     buff=0
     cinnamon=0
     gray=0
     orange=0
     pink=0
     red=0
     white=0
     yellow=0
     if stalk_color_above_ring == 'brown':
         stalk_color_above_ring =1 
     if stalk_color_above_ring == 'buff':
         stalk_color_above_ring =1 
     if stalk_color_above_ring == 'cinnamon':
         stalk_color_above_ring =1 
     if stalk_color_above_ring == 'gray':
         stalk_color_above_ring =1 
     if stalk_color_above_ring == 'orange':
         stalk_color_above_ring =1 
     if stalk_color_above_ring == 'pink':
         stalk_color_above_ring =1 
     if stalk_color_above_ring == 'red':
         stalk_color_above_ring =1 
     elif stalk_color_above_ring == 'white':
         stalk_color_above_ring =1 
     else:
         stalk_color_above_ring =1 

     stalk_color_below_ring = request.form["stalk_color_below_ring"]
     brown=0
     buff=0
     cinnamon=0
     gray=0
     orange=0
     pink=0
     red=0
     white=0
     yellow=0
     if stalk_color_above_ring == 'brown':
         stalk_color_below_ring =1 
     if stalk_color_above_ring == 'buff':
         stalk_color_below_ring =1 
     if stalk_color_above_ring == 'cinnamon':
         stalk_color_below_ring =1 
     if stalk_color_above_ring == 'gray':
         stalk_color_below_ring =1 
     if stalk_color_above_ring == 'orange':
         stalk_color_below_ring =1 
     if stalk_color_above_ring == 'pink':
         stalk_color_below_ring =1 
     if stalk_color_above_ring == 'red':
         stalk_color_below_ring =1 
     elif stalk_color_above_ring == 'white':
         stalk_color_below_ring =1 
     else:
         stalk_color_below_ring =1 
     
     veil_type = request.form["veil_type"]
     partial=0
     universal=0
     if veil_type == 'partial':
         veil_type =1 
     else:
         veil_type =1 
     
     veil_color = request.form["veil_color"]
     brown=0
     orange=0
     white=0
     yellow=0
     if veil_color == 'brown':
         veil_color =1 
     if veil_color == 'orange':
         veil_color =1 
     elif veil_color == 'white':
         veil_color =1 
     else:
         veil_color =1 
     
    
     ring_number = request.form["ring_number"]
     none=0
     one=0
     two=0
     if ring_number == 'none':
         ring_number =1 
     elif ring_number == 'one':
         ring_number =1 
     else:
         ring_number =1

     
     ring_type = request.form["ring_type"]
     cobwebby=0
     evanescent=0
     flaring=0
     large=0
     none=0
     pendant=0
     sheathing=0
     zone=0
     if ring_type == 'cobwebby':
         ring_type =1 
     if ring_type == 'evanescent':
         ring_type =1 
     if ring_type == 'flaring':
         ring_type =1 
     if ring_type == 'large':
         ring_type =1 
     if ring_type == 'sheathing':
         ring_type =1 
     if ring_type == 'zone':
         ring_type =1 
     elif ring_type == 'none':
         ring_type =1 
     else:
         ring_type =1 




     
     spore_print_color = request.form["spore_print_color"]
     black=0
     brown=0
     buff=0
     chocolate=0
     green=0
     orange=0
     purple=0
     white=0
     yellow=0
     if gill_color == 'black':
         spore_print_color =1 
     if gill_color == 'brown':
         spore_print_color =1 
     if gill_color == 'buff':
         spore_print_color =1 
     if gill_color == 'chocolate':
         spore_print_color =1 
     if gill_color == 'green':
         spore_print_color =1 
     if gill_color == 'orange':
         spore_print_color =1 
     if gill_color == 'purple':
         spore_print_color =1 
     elif gill_color == 'white':
         spore_print_color =1 
     else:
         spore_print_color =1 

     
     population = request.form["population"]
     abundant=0
     clustered=0
     numerous=0
     scattered=0
     several=0
     solitary=0
     if population == 'abundant':
         population =1 
     if population == 'clustered':
         population =1 
     if population == 'numerous':
         population =1 
     if population == 'scattered':
         population =1 
     elif population == 'several':
         population =1 
     else:
         population =1 
     
     habitat = request.form["habitat"]
     grasses=0
     leaves=0
     meadow=0
     paths=0
     urban=0
     waste=0
     woods=0
     if habitat == 'grasses':
         habitat =1 
     if habitat == 'leaves':
         habitat =1 
     if habitat == 'meadow':
         habitat =1 
     if habitat == 'urban':
         habitat =1  
     if habitat == 'waste':
         habitat =1 
     elif habitat == 'woods':
         habitat =1 
     else:
         habitat =1
     
     features = np.array([[cap_shape,cap_surface,cap_color,bruises,odor,gill_attachment,gill_spacing, gill_size,gill_color,stalk_shape,stalk_surface_above_ring,stalk_surface_below_ring, stalk_color_above_ring,stalk_color_below_ring ,veil_type ,veil_color, ring_number,ring_type, spore_print_color,population,habitat]])

     pred = model.predict(features)
     
   
   return render_template("result.html", prediction=pred)
     


if __name__ == "__main__":
    app.run(debug=True)

