import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")

st.image("logo.jpeg", width=500)

st.title("Gerenciamento de Clientes")


# Função auxiliar para exibir mensagens de erro detalhadas
def show_response_message(response):
    if response.status_code == 200:
        st.success("Operação realizada com sucesso!")
    else:
        try:
            data = response.json()
            if "detail" in data:
                # Se o erro for uma lista, extraia as mensagens de cada erro
                if isinstance(data["detail"], list):
                    errors = "\n".join([error["msg"] for error in data["detail"]])
                    st.error(f"Erro: {errors}")
                else:
                    # Caso contrário, mostre a mensagem de erro diretamente
                    st.error(f"Erro: {data['detail']}")
        except ValueError:
            st.error("Erro desconhecido. Não foi possível decodificar a resposta.")


# Adicionar Cliente
with st.expander("Adicionar um Novo Cliente"):
    with st.form("new_client"):
        nome = st.text_input("Nome do Cliente")
        telefone = st.text_input("Telefone do Cliente")
        endereco = st.text_input("Endereço do Cliente")
        cpf = st.text_input("CPF do Cliente")
        email = st.text_input("Email do Cliente")
        data_nascimento = st.date_input("Data de Nascimento do Cliente")
        data_ultimo_pedido = st.date_input("Data do Último Pedido do Cliente")
        saldo_devedor = st.number_input("Saldo Devedor do Cliente", min_value=0.01, format="%f")
        observacoes = st.text_area("Observações do Cliente")

        submit_button = st.form_submit_button("Adicionar Cliente")

        if submit_button:
            response = requests.post(
                "http://backend:8000/clients/",
                json={
                    "nome": nome,
                    "telefone": telefone,
                    "endereco": endereco,
                    "cpf": cpf,
                    "email": email,
                    "data_nascimento":data_nascimento.isoformat(),
                    "data_ultimo_pedido":data_ultimo_pedido.isoformat(),
                    "saldo_devedor":saldo_devedor,
                    "observacoes":observacoes
                },
            )
            show_response_message(response)
# Visualizar Clientes
with st.expander("Visualizar Clientes"):
    if st.button("Exibir Todos os Clientes"):
        response = requests.get("http://backend:8000/clients/")
        if response.status_code == 200:
            client = response.json()
            df = pd.DataFrame(client)

            df = df[
                [
                    "id",
                    "nome",
                    "telefone",
                    "endereco",
                    "cpf",
                    "email",
                    "data_nascimento",
                    "data_ultimo_pedido",
                    "saldo_devedor",
                    "observacoes",
                    "created_at"
                ]
            ]

            # Exibe o DataFrame sem o índice
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Obter Detalhes de um Cliente
with st.expander("Obter Detalhes de um Cliente"):
    get_id = st.number_input("ID do Cliente", min_value=1, format="%d")
    if st.button("Buscar Cliente"):
        response = requests.get(f"http://backend:8000/clients/{get_id}")
        if response.status_code == 200:
            client = response.json()
            df = pd.DataFrame([client])

            df = df[
                [
                    "id",
                    "nome",
                    "telefone",
                    "endereco",
                    "cpf",
                    "email",
                    "data_nascimento",
                    "data_ultimo_pedido",
                    "saldo_devedor",
                    "observacoes",
                    "created_at"
                ]
            ]

            # Exibe o DataFrame sem o índice
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Deletar Cliente
with st.expander("Deletar Cliente"):
    delete_id = st.number_input("ID do Cliente para Deletar", min_value=1, format="%d")
    if st.button("Deletar Cliente"):
        response = requests.delete(f"http://backend:8000/clients/{delete_id}")
        show_response_message(response)

# Atualizar Cliente
with st.expander("Atualizar Cliente"):
    with st.form("update_client"):
        update_id = st.number_input("ID do Cliente", min_value=1, format="%d")
        new_nome = st.text_input("Novo Nome do Cliente")
        new_telefone = st.text_area("Nova Descrição do Cliente")
        new_saldo_devedor = st.number_input(
            "Novo Saldo Devedor",
            min_value=0.01,
            format="%f",
        )

        new_email = st.text_input("Novo Email do Cliente")

        update_button = st.form_submit_button("Atualizar Cliente")

        if update_button:
            update_data = {}
            if new_nome:
                update_data["nome"] = new_nome
            if new_telefone:
                update_data["telefone"] = new_telefone
            if new_email:
                update_data["email"] = new_email
            if new_saldo_devedor > 0:
                update_data["saldo_devedor"] = new_saldo_devedor


            if update_data:
                response = requests.put(
                    f"http://backend:8000/clients/{update_id}", json=update_data
                )
                show_response_message(response)
            else:
                st.error("Nenhuma informação fornecida para atualização")