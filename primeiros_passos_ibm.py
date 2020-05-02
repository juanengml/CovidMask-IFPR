from IBM import Model
# pegar credenciais
api_key = " "
model_id = " "

# carregar credenciais e imagem
model = Model("images/foto01.png",api_key=api_key,model_id=model_id)

# gerar classificacao
print(model.label_predict())
