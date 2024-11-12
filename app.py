from flask import Flask, render_template, request, redirect, url_for
from models import db, Item  # Certifique-se de que o arquivo models.py está configurado corretamente

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados com a aplicação Flask
db.init_app(app)

# Cria as tabelas no banco de dados antes da primeira requisição
@app.before_request
def create_tables():
    db.create_all()

# Rota de Leitura - Listar Todos os Itens
@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

# Rota de Criação - Adicionar um novo Item
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        clube = request.form['clube']
        new_item = Item(name=name, clube=clube)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

# Rota de Criação de Comentários - Adicionar um novo Comentário
@app.route('/create_comen', methods=['GET', 'POST'])
def create_comen():
    if request.method == 'POST':
        name = request.form['name']
        clube = request.form['clube']
        comentario = request.form['comentario']
        new_item = Item(name=name, clube=clube, comentario=comentario)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('coment.html')

# Rota de Atualização - Editar um Item existente
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = Item.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.clube = request.form['clube']
        item.comentario = request.form['comentario']  # Atualiza o campo comentário
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', item=item)

# Rota de Exclusão - Deletar um Item
@app.route('/delete/<int:id>')
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

# Executa a aplicação Flask
if __name__ == "__main__":
    app.run(debug=True)
