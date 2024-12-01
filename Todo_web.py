import streamlit as st
import Functions

todos = Functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is aimed at improving your productivity!")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Add a new todo......",
              on_change=add_todo, key="new_todo")