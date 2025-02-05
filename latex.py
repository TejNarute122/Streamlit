import streamlit as st 

#Different Matrix Representattion 
st.markdown("## Matrix Representation")
st.latex(r"\begin{pmatrix}2&3\\4&5\\5&7\end{pmatrix}")
st.latex(r"\begin{bmatrix}2&3\\4&5\end{bmatrix}")
st.latex(r"\begin{Bmatrix}1&2\\3&4\end{Bmatrix}")
st.latex(r"\begin{vmatrix}1&2\\3&4\end{vmatrix}")

#Mathamatical Eqution Representation
st.markdown("## Mathamatical representation")
st.latex(r"a'")
st.latex(r"\tilde{a}")
st.latex(r"\utilde{AB}")
st.latex("a^{\prime}")
st.latex(r"\acute{a}")
st.latex(r"\bar{y}")
st.latex(r"\breve{y}")
st.latex(r"\overleftarrow{AB}")
st.latex(r"\underleftarrow{AB}")
st.latex(r"\overrightarrow{AB}")
st.latex(r"\underrightarrow{AB}")
st.latex(r"\overbrace{AB}")
st.latex(r"\underbrace{AB}")
st.latex(r"\underline{AB}")
st.latex(r"\overline{AB}")
