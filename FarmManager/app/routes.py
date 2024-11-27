from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from app.models import db, Fazenda, Animal

api = Api()

class FazendaResource(Resource):
    def get(self):
        fazendas = Fazenda.query.all()
        return jsonify([{'id': f.id, 'nome': f.nome_fazenda, 'localizacao': f.localizacao} for f in fazendas])

    def post(self):
        data = request.json
        nova_fazenda = Fazenda(nome_fazenda=data['nome_fazenda'], localizacao=data['localizacao'])
        db.session.add(nova_fazenda)
        db.session.commit()
        return jsonify({'message': 'Fazenda registrada com sucesso!'})

class AnimalResource(Resource):
    def get(self, fazenda_id):
        animais = Animal.query.filter_by(fazenda_id=fazenda_id).all()
        return jsonify([{'id': a.id, 'nome': a.nome, 'sexo': a.sexo} for a in animais])

    def post(self, fazenda_id):
        data = request.json
        novo_animal = Animal(
            fazenda_id=fazenda_id,
            nome=data['nome'],
            sexo=data['sexo'],
            data_nascimento=data['data_nascimento'],
            raca=data['raca']
        )
        db.session.add(novo_animal)
        db.session.commit()
        return jsonify({'message': 'Animal adicionado com sucesso!'})

api.add_resource(FazendaResource, '/fazendas')
api.add_resource(AnimalResource, '/fazendas/<int:fazenda_id>/animais')
