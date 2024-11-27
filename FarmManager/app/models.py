from app import db

# Tabela Fazendas
class Fazenda(db.Model):
    __tablename__ = 'fazendas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    localizacao = db.Column(db.String(255))
    criado_em = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relacionamento com os animais
    animais = db.relationship('Animal', backref='fazenda', lazy=True)


# Tabela Animais
class Animal(db.Model):
    __tablename__ = 'animais'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    tipo = db.Column(db.Enum('boi', 'vaca', 'bezerro'), nullable=False)
    nascimento = db.Column(db.Date)
    peso_atual = db.Column(db.Numeric(10, 2))
    fazenda_id = db.Column(db.Integer, db.ForeignKey('fazendas.id'), nullable=False)
    criado_em = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relacionamento com o histórico de peso
    historico_peso = db.relationship('HistoricoPeso', backref='animal', lazy=True)


# Tabela Histórico de Peso
class HistoricoPeso(db.Model):
    __tablename__ = 'historico_peso'

    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animais.id'), nullable=False)
    data_pesagem = db.Column(db.Date, nullable=False)
    peso = db.Column(db.Numeric(10, 2), nullable=False)
    criado_em = db.Column(db.DateTime, default=db.func.current_timestamp())


# Tabela Vacinas
class Vacina(db.Model):
    __tablename__ = 'vacinas'

    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animais.id'), nullable=False)
    tipo_vacina = db.Column(db.String(100), nullable=False)
    data_vacinacao = db.Column(db.Date, nullable=False)
    criado_em = db.Column(db.DateTime, default=db.func.current_timestamp())


# Tabela Inseminações
class Inseminacao(db.Model):
    __tablename__ = 'inseminacoes'

    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animais.id'), nullable=False)
    data_inseminacao = db.Column(db.Date, nullable=False)
    resultado = db.Column(db.Enum('positivo', 'negativo'), default='negativo')
    criado_em = db.Column(db.DateTime, default=db.func.current_timestamp())
