from flask import Flask, request, render_template, redirect, url_for, jsonify, session
import pandas as pd
import numpy as np 

app = Flask(__name__)

@app.route('/')
def index():

	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	f = request.files['file']
	df = pd.read_csv(f)
	
	df.drop('Data Competencia', axis=1, inplace=True)
	df.drop('Detalhes', axis=1, inplace=True)
	df.drop('Numero do Documento', axis=1, inplace=True)
	df.drop('Forma de Pagamento', axis=1, inplace=True)
	df.drop('Centro de Custo', axis=1, inplace=True)
	df.drop('Tags', axis=1, inplace=True)

	data_saidas = df[(df['Tipo de Lancamento'] != 'Recebimentos') & (df['Tipo de Lancamento'] != 'Transferências Saída') & (df['Tipo de Lancamento'] != 'Transferências Entrada') ]


	########## Variavel por Categoria
	grupo_categorias = data_saidas[['Categoria','Valor']]
	grupo = grupo_categorias.groupby('Categoria')
	soma_das_categorias = grupo.sum()
	dict_soma_das_categorias = soma_das_categorias.to_dict()
	dict_soma_cat = dict_soma_das_categorias['Valor']


	########## Variavel por Tipo de Lançamento
	grupo_lancamentos = data_saidas[['Tipo de Lancamento','Valor']]
	grupo_lan = grupo_lancamentos.groupby('Tipo de Lancamento')
	soma_dos_lancamentos = grupo_lan.sum()
	dict_soma_dos_lancamentos = soma_dos_lancamentos.to_dict()
	data_tipo_saida = dict_soma_dos_lancamentos['Valor']

	########## Variavel por data
	grupo_data_pagamento = data_saidas[['Data Pagamento','Valor']]
	grupo_pag = grupo_data_pagamento.groupby('Data Pagamento')
	soma_pagamento = grupo_pag.sum()
	dict_soma_pagamento = soma_pagamento.to_dict()
	pagamento_por_data = dict_soma_pagamento['Valor']
	
	ld = []
	lv = []
	for k,v in pagamento_por_data.items():
		ld.extend([k])

	for k,v in pagamento_por_data.items(): 
		lv.extend([v]) 

	######### contas cadastradas 
	contas = df['Conta']
	contas_cadastradas = contas.unique()
	conts = contas_cadastradas.tolist()

	return render_template('process.html', data=dict_soma_cat, 
								data_tipo_saida=data_tipo_saida, 
							 pagamento_por_data=pagamento_por_data,
							 		ld=ld,
							 		lv=lv,
							 	 conts=conts)

if __name__ == '__main__':
	app.run(debug=True)