import streamlit as st

class Usuario:
    def __init__(self, nome="", sobrenome="", data_nasc=None, eSTcivil="", sexo="", salario=0):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nasc = data_nasc
        self.eSTcivil = eSTcivil
        self.sexo = sexo
        self.salario = salario

    def infoUser(self):
        st.header("Informe seus Dados")
        self.nome = st.text_input("Informe seu nome ")
        self.sobrenome = st.text_input("Informe o sobrenome ")
        self.data_nasc = st.date_input("Informe sua data de nascimento")
        
        self.eSTcivil = st.selectbox(
            "Informe seu estado civil",
            ("Solteiro", "Casado", "Divorciado", "Viúvo"),
        )
        self.sexo = st.selectbox(
            "Informe seu sexo",
            ("Masculino", "Feminino", "Outro"),
        )
        
        self.salario = st.number_input("Informe seu Salário ")
        
        if st.button("Enviar"):
            st.write("\n\nDados Informados:")
            st.write("Nome: ", self.nome)
            st.write("Sobrenome: ", self.sobrenome)
            st.write("Data de Nascimento: ", self.data_nasc.strftime("%d/%m/%Y"))
            st.write("Estado Civil: ", self.eSTcivil)
            st.write("Sexo: ", self.sexo)
            st.write("Salário: ", self.salario)
            
            if self.salario < 2500:
                st.write("- O funcionário deve receber um aumento.")
                aumento = 0
                while aumento < 500:
                    aumento += 100
                st.write("- Aumento: ", aumento)
            else:
                st.write("- O funcionário não precisa receber aumento")

usuario = Usuario()
usuario.infoUser()

