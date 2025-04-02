import streamlit as st
class Usuario:
    def __init__(self, nome, sobrenome, data_nasc, ESTcivil, sexo, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nasc = data_nasc
        self.ESTcivil = ESTcivil
        self.sexo = sexo
        self.salario = salario
      
  def infoUser(self):
    st.header("Informe seus Dados")
    self.nome = st.text_input("Informe seu nome ")
    self.sobrenome = st.text_input("Infome o sobrenome ")
    self.data_nasc = st.date_input("Informe sua data de nascimento", format="DD.MM.YYYY")


    self.ESTcivil = st.selectbox(
      "Informe seu estado civil",
      ("Solteiro", "Casado", "Divorciado", "Viúvo"),
    )
    self.sexo = st.selectbox(
      "Informe seu sexo",
      ("Masculino", "Feminino", "Outro"),
    )

    self.salario = st.number_input("Informe seu Salário ")

    if st.button("Enviar"):
        st.write("")
        st.write("")
        st.write("Dados Informados: ")
        st.write("Nome: ", self.nome)
        st.write("Sobrenome: ", self.sobrenome)
        st.write("Data de Nascimento: ", self.dt_nasc.strftime("%d/%m/%Y"))
        st.write("Estado Civil: ", self.ESTcivil)
        st.write("Sexo: ", self.sexo)
        st.write("Salário: ", self.salario)
   
   
        if self.salario < 2500:
          st.write("- O funcionário deve receber um aumento.")
          aumento = 0
          while aumento < 500:
            aumento = aumento + 100
          st.write("- Aumento ", aumento)
        else:
          st.write("- O funcionário não precisa receber aumento")
 
   
 

  infoUser()
