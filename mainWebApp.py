# Create Web App

import streamlit as st
import functions as fun
# Title, Heading

# st.write("""
# Reminder for Developer:
# 1) Script runs from top to bottom
# 2) Hit 'Enter' at the text input re-runs the script again
# 3) st.session_state = Returns events name and values
# """)

st.title('To-Do App')

st.subheader('For your daily task tracking needs 😀')



# 1) Add todo function

def add_todo():
    to_add = st.session_state["userinput"]
    formatted_to_add = to_add.title() + '\n'
    if to_add != '':
        if todos.count(formatted_to_add) > 0:
            pass
        else:
            todos.append(formatted_to_add)
            fun.write_todos(todos)
            st.session_state['userinput'] = ''

todos = fun.get_todos()

# Add checkboxes
for index, item in enumerate(todos):
    check = st.checkbox(label=item,key=item)
    print(check)

    if check:
        # Remove the `Ticked` checkbox
        todos.pop(index)

        # Write to todos.txt
        fun.write_todos(todos)

        # delete key from session_state
        del st.session_state[item]

        # Rerun the session again to refresh the changes

        st.experimental_rerun()


# User Input Box
st.text_input(value='',
              label='Enter to-do: ',
              placeholder='Eg: Do laundry',
              key='userinput',
              on_change= add_todo)
