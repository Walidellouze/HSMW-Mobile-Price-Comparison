from flask import Flask,  render_template, request, redirect, url_for,jsonify,session
from Comparateur_Jumia import *
from Comparateur_tunisianet import *
from Comparateur_Wiki import *
import os
import time
import secrets
from flask_mail import Mail, Message
from flask_mysqldb import MySQL
 
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # or the appropriate port number
app.config['MAIL_USE_TLS'] = True  # or False if not using TLS
app.config['MAIL_USERNAME'] = 'ketatasalem7@gmail.com'
app.config['MAIL_PASSWORD'] = 'xxofluylphqnybbh'
app.config['MAIL_DEFAULT_SENDER'] = 'ketatasalem7@gmail.com'
mail = Mail(app)
app.secret_key = secrets.token_hex(16)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'testflask'
 
mysql = MySQL(app)

@app.route('/test')
def test():
    cur = mysql.connection.cursor()
    query = " SELECT * FROM product JOIN model ON product.id_model = model.id"
    cur.execute(query)
    dataproduct = cur.fetchall()
    return jsonify(dataproduct)
@app.route('/')
def indexHome():
     cur = mysql.connection.cursor()
     cur.execute("SELECT * FROM brand")
     data = cur.fetchall()
     cur = mysql.connection.cursor()
     query = " SELECT * FROM product JOIN model ON product.id_model = model.id"
     cur.execute(query)
     dataproduct = cur.fetchall()

     cur.close()
     idUser =  session.get('id')
     usernameUser =  session.get('username')
     return render_template('indexHome.html',data=data,dataproduct=dataproduct,idUser=idUser,usernameUser=usernameUser)


@app.route('/index')
def index():
    if(session.get('role')=="admin"):
        return render_template('index.html')
    else:
        return redirect(url_for('indexHome'))
   

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/details/<id>')
def details(id):
     cur = mysql.connection.cursor()
     cur.execute("SELECT * FROM product WHERE id = %s", (id,))
     dataproduct = cur.fetchone()
     cur.execute("SELECT * FROM rate WHERE id_product = %s", (id,))
     datarate = cur.fetchall()
     cur.execute("SELECT * FROM validation WHERE id_product = %s", (id,))
     datavalidation = cur.fetchall()
     cur.execute("SELECT * FROM model WHERE id = %s", (dataproduct[7],))
     datamodelp = cur.fetchone()
     cur.execute("SELECT * FROM brand model WHERE id = %s", (datamodelp[2],))
     databrand = cur.fetchone()
     array_product=[]
     cur.execute("SELECT * FROM product ")
     dataproducts = cur.fetchall()
     cur.execute("SELECT * FROM model WHERE id_marque = %s", (databrand[0],))
     datamodel = cur.fetchall()
     for i in datamodel:
         for j in dataproducts:
             if(i[0]==j[7]):
                 
                 array_product.append(j)

     score=0
     nbValidation=0
     for i in datarate:
         score = score + i[3]
     
     if(len(datarate) == 0):
         scoreF = 0
     else:
         scoreF = score / len(datarate)
     for i in datavalidation:
         nbValidation=nbValidation+1
         
     idUser =  session.get('id')
     usernameUser =  session.get('username')
     cur.close()
     return render_template('Details.html',data=dataproduct,idUser=idUser,usernameUser=usernameUser,scoreF=int(scoreF),nbValidation=nbValidation,sim=array_product[:3])
    

@app.route('/rechercheGrid')
def recherche():
    idUser =  session.get('id')
    usernameUser =  session.get('username')
    return render_template('RechercheGrid.html',idUser=idUser,usernameUser=usernameUser)

@app.route('/resultat')
def resultat():
    return render_template('resultat.html')

@app.route('/applyResultat', methods=['POST'])
def applyResultat(nom=""):
    model = request.form.get('model')   
    couleur = request.form.get('couleur')  
    stockage = request.form.get('stockage') 
    ram = request.form.get('ram')   
    session['model'] = model
    session['couleur'] = couleur
    session['stockage'] = stockage
    session['ram'] = ram
    if(nom==""):
        nom = model + " " + couleur  +" "+ stockage +" GO "+ ram + " GO RAM"
    list_telephones_tunisianet=scrap_comparateur_wiki(nom)
    list_telephones_jumia=scrap_comparateur_jumia(nom)
    list_telephones = []
    list_telephones.extend(list_telephones_tunisianet)
    list_telephones.extend(list_telephones_jumia)
    idUser =  session.get('id')
    usernameUser =  session.get('username')
    session['listeT'] = list_telephones
    return render_template('resultat.html', list_telephones=list_telephones,idUser=idUser,usernameUser=usernameUser,i=len(list_telephones))

@app.route('/rate', methods=['POST'])
def rate():
    model =  session.get('model')
    couleur =  session.get('couleur')
    stockage =  session.get('stockage')
    ram =  session.get('ram')
    score = request.form.get('Ratings')
    if(couleur == "Noir"):
        couleur = "Black"
    if(couleur == "Violet"):
        couleur = "Deep Purple"
    cur = mysql.connection.cursor()
    query = "SELECT * FROM product WHERE name = %s AND color = %s AND storage = %s AND ram = %s"
    cur.execute(query, (model,couleur,stockage,ram))
    result = cur.fetchone()
    idUser =  session.get('id')
    usernameUser =  session.get('username')
    cur.execute("INSERT INTO rate (id_product,id_customer,score) VALUES (%s,%s,%s)",(result[0],idUser,score))
    mysql.connection.commit()
    cur.close()
    return render_template('resultat.html', list_telephones=session.get('listeT'),idUser=idUser,usernameUser=usernameUser,i=len(session.get('listeT')))

@app.route('/validate', methods=['POST'])
def validate():
    model =  session.get('model')
    couleur =  session.get('couleur')
    stockage =  session.get('stockage')
    ram =  session.get('ram')  
    idUser =  session.get('id')
    if(couleur == "Noir"):
        couleur = "Black"
    if(couleur == "Violet"):
        couleur = "Deep Purple"
    cur = mysql.connection.cursor()
    query = "SELECT * FROM product WHERE name = %s AND color = %s AND storage = %s AND ram = %s"
    cur.execute(query, (model,couleur,stockage,ram))
    result = cur.fetchone()
    cur.execute("INSERT INTO validation (id_product,id_customer) VALUES (%s,%s)",(result[0],idUser))
    mysql.connection.commit()
    cur.close()
    
    return redirect(url_for('indexHome'))
@app.route('/validateD', methods=['POST'])
def validateD():
    idUser =  session.get('id')
    id = request.form['id']
    cur = mysql.connection.cursor()
    query = "SELECT * FROM product WHERE id = %s "
    cur.execute(query, (id,))
    result = cur.fetchone()
    cur.execute("INSERT INTO validation (id_product,id_customer) VALUES (%s,%s)",(result[0],idUser))
    mysql.connection.commit()
    cur.close()
    
    return redirect(url_for('indexHome'))
#************************Profil****************
@app.route('/profile')
def profile():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user WHERE id = %s", (session.get('id'),))
    user = cur.fetchone()
    cur.close()
    idUser =  session.get('id')
    usernameUser =  session.get('username')
    return render_template('profile.html', user=user,idUser=idUser,usernameUser=usernameUser)

@app.route('/modifProfil',methods=['POST'])
def modifProfil():
    cur = mysql.connection.cursor()
    id = request.form['id']
    name = request.form['name']
    address = request.form['address']
    postalcode = request.form['postalcode']
    email = request.form['email']
    phone = request.form['phone']
    city = request.form['city']
    civilstate = request.form['civilstate']
    birthdate = request.form['birthdate']
    cur.execute("UPDATE user SET name = %s, address = %s , postalcode = %s, email = %s, phone = %s, city = %s, civilstate = %s, birthdate = %sWHERE id = %s", (name,address,postalcode,email,phone,city,civilstate,birthdate, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Profil updated successfully'})
#******************************************

#**********************revhervhe***************
@app.route('/rechercheGrid/<id>')
def rechercheGrid(id):
     
     cur = mysql.connection.cursor()
     array_product=[]
     cur.execute("SELECT * FROM product ")
     dataproduct = cur.fetchall()
     cur.execute("SELECT * FROM model WHERE id_marque = %s", (id,))
     datamodel = cur.fetchall()
     cur.execute("SELECT * FROM brand WHERE id= %s", (id,))
     databrand = cur.fetchone()
     for i in datamodel:
         for j in dataproduct:
             if(i[0]==j[7]):
                 
                 array_product.append(j)
     cur.close()
     idUser =  session.get('id')
     usernameUser =  session.get('username')
     return render_template('RechercheGrid.html',data=array_product,datamodel=datamodel,databrand=databrand,i=len(array_product),idUser=idUser,usernameUser=usernameUser)     



#********************************login/register**************************

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/addCustomer', methods=['POST'])
def addCustomer():
    
    password = request.form.get('password')
    name = request.form.get('name')
    address = request.form.get('address')
    postalcode = request.form.get('postalcode')
    birthdate = request.form.get('birthdate')
    email = request.form.get('email')
    phone = request.form.get('phone')
    city = request.form.get('city')
    gender = request.form.get('gender')
    childnumber = request.form.get('childnumber')
    civilstate = request.form.get('civilstate')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO profile (login,password) VALUES (%s,%s)",(email,password))
    mysql.connection.commit()
    cur.close()
    cur = mysql.connection.cursor()
    query = "SELECT * FROM profile WHERE login = %s"
    cur.execute(query, (email,))
    result = cur.fetchone()
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user (name,address,postalcode,birthdate,email,phone,city,gender,childnumber,civilstate,id_profile,role) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,address,postalcode,birthdate,email,phone,city,gender,childnumber,civilstate,result[0],'customer'))
    mysql.connection.commit()
    cur.close()
   
    return redirect(url_for('login'))

@app.route('/signin', methods=['POST'])
def signin():
    
    password = request.form.get('password')
    email = request.form.get('email')
    cur = mysql.connection.cursor()
    query = "SELECT * FROM profile WHERE login = %s AND password = %s"
    cur.execute(query, (email,password))
    result = cur.fetchone()
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()
    if result is None:
       return redirect(url_for('login'))
    else:
        if user[12] == "admin":
            session.pop('id', None)
            session.pop('username', None)
            session.pop('role', None)
            session['id'] = user[0]
            session['username'] = user[1]
            session['role'] = user[12]
            return redirect(url_for('index'))
        else:
            session.pop('id', None)
            session.pop('username', None)
            session.pop('role', None)
            session['id'] = user[0]
            session['username'] = user[1]
            session['role'] = user[2]
            return redirect(url_for('indexHome'))
        
@app.route('/signout')
def signout():
    session.pop('id', None)
    session.pop('username', None)
    session.pop('role', None)
    session.pop('listeT', None)
    return redirect(url_for('indexHome'))

                   
  #*********************************Company****************** 
@app.route('/company')
def company():
    if(session.get('role')=="admin"):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM company")
        data = cur.fetchall()
        cur.close()
        return render_template('company.html',data=data)
    else:
        return redirect(url_for('indexHome'))

@app.route('/addCompany', methods=['POST'])
def addCompany():
    name = request.form.get('name')
    link = request.form.get('link')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO company (name,link) VALUES (%s,%s)",(name,link))
    mysql.connection.commit()
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM company")
    data = cur.fetchall()
    cur.close()
    return redirect(url_for('company'))

@app.route('/company/<id>')
def findCompanyById(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM company WHERE id = %s", (id,))
    category = cur.fetchone()
    cur.close()
    return jsonify(category)

@app.route('/modifCompany',methods=['POST'])
def modifCompany():
    cur = mysql.connection.cursor()
    id = request.form['id']
    name = request.form['name']
    link = request.form['link']
    cur.execute("UPDATE company SET name = %s, link = %s WHERE id = %s", (name,link, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Category updated successfully'})

@app.route('/deleteCompany/<id>',methods=['DELETE'])
def deleteCompany(id):
    cur = mysql.connection.cursor()
    delete_query = "DELETE FROM Company WHERE id = %s"
    cur.execute(delete_query, (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Category updated successfully'})  

#*****************************Category*************

@app.route('/category')
def category():
    if(session.get('role')=="admin"):
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM category")
         data = cur.fetchall()
         cur.close()
         return render_template('category.html',data=data)
    else:
        return redirect(url_for('indexHome'))

@app.route('/addCategory', methods=['POST'])
def addCategory():
    name = request.form.get('name')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO category (name) VALUES (%s)",(name,))
    mysql.connection.commit()
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM category")
    data = cur.fetchall()
    cur.close()
    return redirect(url_for('category'))

@app.route('/category/<id>')
def findCategoryById(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM category WHERE id = %s", (id,))
    category = cur.fetchone()
    cur.close()
    return jsonify(category)


@app.route('/modifcategory',methods=['POST'])
def modifCategory():
    cur = mysql.connection.cursor()
    id = request.form['id']
    name = request.form['name']
    cur.execute("UPDATE category SET name = %s WHERE id = %s", (name, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Category updated successfully'})

@app.route('/deleteCategory/<id>',methods=['DELETE'])
def deleteCategory(id):
    cur = mysql.connection.cursor()
    delete_query = "DELETE FROM category WHERE id = %s"
    cur.execute(delete_query, (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Category updated successfully'})

#**********************************subcategory*********************
@app.route('/subcategory')
def subcategory():
    if(session.get('role')=="admin"):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM subcategory")
        data = cur.fetchall()
        cur.execute("SELECT * FROM category")
        datacategory = cur.fetchall()
        cur.close()
        return render_template('subcategory.html',data=data,datacategory=datacategory)
    else:
        return redirect(url_for('indexHome'))

        
 

@app.route('/addSubCategory', methods=['POST'])
def addSubCategory():
    name = request.form.get('name')
    id_category = request.form.get('id_category')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO subcategory (name,id_category) VALUES (%s,%s)",(name,id_category))
    mysql.connection.commit()
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM subcategory")
    data = cur.fetchall()
    cur.close()
    return redirect(url_for('subcategory'))

@app.route('/subcategory/<id>')
def findSubCategoryById(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM subcategory WHERE id = %s", (id,))
    subcategory = cur.fetchone()
    cur.close()
    return jsonify(subcategory)


@app.route('/modifsubcategory',methods=['POST'])
def modifSubCategory():
    cur = mysql.connection.cursor()
    id = request.form['id']
    name = request.form['name']
    id_category = request.form['id_category']
    cur.execute("UPDATE subcategory SET name = %s , id_category= %s WHERE id = %s", (name,id_category, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'SubCategory updated successfully'})

@app.route('/deleteSubCategory/<id>',methods=['DELETE'])
def deleteSubCategory(id):
    cur = mysql.connection.cursor()
    delete_query = "DELETE FROM subcategory WHERE id = %s"
    cur.execute(delete_query, (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'SubCategory updated successfully'})

#**********************************Marque*********************
@app.route('/marque')
def marque():
    if(session.get('role')=="admin"):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM brand")
        
        data = cur.fetchall()
        cur.execute("SELECT * FROM subcategory")
        datasubcategory = cur.fetchall()
        cur.close()
        return render_template('marque.html',data=data,datasubcategory=datasubcategory)
    else:
        return redirect(url_for('indexHome'))
   

@app.route('/addMarque', methods=['POST'])
def addMarque():
    name = request.form.get('name')
    id_subcategory = request.form.get('id_subcategory')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO brand (name,id_subcategory) VALUES (%s,%s)",(name,id_subcategory))
    mysql.connection.commit()
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM brand")
    data = cur.fetchall()
    cur.close()
    return redirect(url_for('marque'))

@app.route('/marque/<id>')
def findMarqueById(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM brand WHERE id = %s", (id,))
    marque = cur.fetchone()
    cur.close()
    return jsonify(marque)


@app.route('/modifmarque',methods=['POST'])
def modifMarque():
    cur = mysql.connection.cursor()
    id = request.form['id']
    name = request.form['name']
    id_subcategory = request.form['id_subcategory']
    cur.execute("UPDATE brand SET name = %s , id_subcategory= %s WHERE id = %s", (name,id_subcategory, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Marque updated successfully'})

@app.route('/deleteMarque/<id>',methods=['DELETE'])
def deleteMarque(id):
    cur = mysql.connection.cursor()
    delete_query = "DELETE FROM brand WHERE id = %s"
    cur.execute(delete_query, (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Marque updated successfully'})




#**********************************Model*********************
@app.route('/model')
def model():
     if(session.get('role')=="admin"):
       cur = mysql.connection.cursor()
       cur.execute("SELECT * FROM model")   
       data = cur.fetchall()
       cur.execute("SELECT * FROM brand")
       datamarque = cur.fetchall()
       cur.close()
       return render_template('model.html',data=data,datamarque=datamarque)
     else:
        return redirect(url_for('indexHome'))
    

@app.route('/addModel', methods=['POST'])
def addModel():
    name = request.form.get('name')
    id_marque = request.form.get('id_marque')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO model (name,id_marque) VALUES (%s,%s)",(name,id_marque))
    mysql.connection.commit()
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM model")
    data = cur.fetchall()
    cur.close()
    return redirect(url_for('model'))

@app.route('/model/<id>')
def findModelById(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM model WHERE id = %s", (id,))
    model = cur.fetchone()
    cur.close()
    return jsonify(model)


@app.route('/modifmodel',methods=['POST'])
def modifModel():
    cur = mysql.connection.cursor()
    id = request.form['id']
    name = request.form['name']
    id_marque = request.form['id_marque']
    cur.execute("UPDATE model SET name = %s , id_marque= %s WHERE id = %s", (name,id_marque, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Model updated successfully'})

@app.route('/deleteModel/<id>',methods=['DELETE'])
def deleteModel(id):
    cur = mysql.connection.cursor()
    delete_query = "DELETE FROM model WHERE id = %s"
    cur.execute(delete_query, (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Model updated successfully'})


#**********************************product*********************
@app.route('/product')
def product():
    if(session.get('role')=="admin"):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM product")
        data = cur.fetchall()
        cur.execute("SELECT * FROM model")
        datamodel = cur.fetchall()
        cur.execute("SELECT * FROM company")
        datacompany = cur.fetchall()
        cur.close()
        return render_template('product.html',data=data,datamodel=datamodel,datacompany=datacompany)
    else:
        return redirect(url_for('indexHome'))
    

@app.route('/addProduct', methods=['POST'])
def addProduct():
    color = request.form.get('color')
    price = request.form.get('price')
    storage = request.form.get('storage')
    ram = request.form.get('ram')
    id_model = request.form.get('id_model')
    id_company = request.form.get('id_company')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM model WHERE id = %s", (id_model,))
    model = cur.fetchone()
    cur.execute("SELECT * FROM brand WHERE id = %s", (model[2],))
    brand = cur.fetchone()
    name = brand[1] + " " + model[1]
    photo = request.files['image']
    newfile = str(int(time.time())) + '.' + photo.filename.rsplit('.', 1)[1].lower()
    photo.save(os.path.join(r'C:\salemketata\1 GLID\ihm\hello_flask\static', newfile))
    cur.execute("INSERT INTO product (name,color,price,storage,ram,image,id_model,id_company) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(name,color,price,storage,ram,newfile,id_model,id_company))
    mysql.connection.commit()
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product")
    data = cur.fetchall()
    cur.close()
    return redirect(url_for('product'))

@app.route('/product/<id>')
def findProductById(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product WHERE id = %s", (id,))
    model = cur.fetchone()
    cur.close()
    return jsonify(model)


@app.route('/modifproduct',methods=['POST'])
def modifProduct():
    cur = mysql.connection.cursor()
    id = request.form['id']
    color = request.form['color']
    price = request.form['price']
    storage = request.form['storage']
    ram = request.form['ram']
    id_model = request.form['id_model']
    id_company = request.form['id_company']
    cur.execute("SELECT * FROM model WHERE id = %s", (id_model,))
    model = cur.fetchone()
    cur.execute("SELECT * FROM brand WHERE id = %s", (model[2],))
    brand = cur.fetchone()
    name = brand[1] + " " + model[1]
    cur.execute("UPDATE product SET name = %s ,color = %s ,price = %s ,storage = %s ,ram = %s ,id_model = %s ,id_company = %s  WHERE id = %s", (name,color,price,storage,ram,id_model,id_company, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Product updated successfully'})

@app.route('/deleteProduct/<id>',methods=['DELETE'])
def deleteProduct(id):
    cur = mysql.connection.cursor()
    delete_query = "DELETE FROM product WHERE id = %s"
    cur.execute(delete_query, (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Product updated successfully'}) 
#**********************************customer*********************
@app.route('/customer')
def customer():
    if(session.get('role')=="admin"):
          cur = mysql.connection.cursor()
          cur.execute("SELECT * FROM user WHERE role = %s", ("customer",))
          data = cur.fetchall()
          cur.close()
          return render_template('customer.html',data=data)
    else:
        return redirect(url_for('indexHome'))
  


@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Construct the email body
    body = f"Name: {name}\nEmail: {email}\n\n{message}"

    recipient = 'ketatasalem7@gmail.com'

    message = Message(subject=subject, recipients=[recipient], body=body)

    try:
        mail.send(message)
        return redirect(url_for('indexHome'))
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)



