# streamlit run web.py in terminal to launch this.
import streamlit as st
from Modules.functions import get_todos, write_todos

# Function to add a new to-do
def add_todo():
    new_todo = st.session_state['addTodoInput'] + '\n'
    todos.append(new_todo)
    write_todos(todos)
    st.session_state['addTodoInput'] = ''  # Clear input field

# Function to remove a to-do
def remove_todo(index):
    todos.pop(index)
    write_todos(todos)
    st.experimental_rerun()  # Rerun to update the checkboxes

todos = get_todos()

st.title('My TODO App')
st.subheader('As a practice project')
st.write('This app is to increase your productivity.')

# Display the to-do items with checkboxes
for index, singleTodo in enumerate(todos):
    if st.checkbox(singleTodo.strip(), key=f'{singleTodo}_{index}'):
        remove_todo(index)

# Input field for adding a new to-do
st.text_input(
    label='Enter a TODO:',
    placeholder='Add new TODO...',
    on_change=add_todo,
    key='addTodoInput'
)

