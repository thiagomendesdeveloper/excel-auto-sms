import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe22b194663a0c94892d5357f67b187fb"
# Your Auth Token from twilio.com/console
auth_token  = "6be0b40d9224cc73993e82c3d2513bcd"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[ tabela_vendas['Vendas'] > 55000 ,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[ tabela_vendas['Vendas'] > 55000 ,'Vendas'].values[0]
        #print(f'no mês de {mes} alguem bateu a meta. Vendedor: {vendedor} , Vendas: {vendas}')
        message = client.messages.create(
        to="+5585985948248", 
        from_="+14144099499",
        body=f'no mês de {mes} alguem bateu a meta. Vendedor: {vendedor} , Vendas: {vendas}')
        print(message.sid)
        

