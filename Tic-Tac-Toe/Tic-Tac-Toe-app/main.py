import streamlit as st

# Initialize the board and the game state
if 'board' not in st.session_state:
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]  # Empty board
    st.session_state.turn = 'X'  # X starts the game
    st.session_state.winner = None  # No winner yet

# Function to handle button click
def button_click(i, j):
    if st.session_state.board[i][j] == '' and st.session_state.winner is None:
        st.session_state.board[i][j] = st.session_state.turn  # Place X or O
        if check_winner():
            st.session_state.winner = st.session_state.turn
        else:
            st.session_state.turn = 'O' if st.session_state.turn == 'X' else 'X'  # Switch turn

# Function to check for a winner
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if st.session_state.board[i][0] == st.session_state.board[i][1] == st.session_state.board[i][2] != '':
            return True
        if st.session_state.board[0][i] == st.session_state.board[1][i] == st.session_state.board[2][i] != '':
            return True
    if st.session_state.board[0][0] == st.session_state.board[1][1] == st.session_state.board[2][2] != '':
        return True
    if st.session_state.board[0][2] == st.session_state.board[1][1] == st.session_state.board[2][0] != '':
        return True
    return False

# Function to update the buttons on the UI
def update_buttons():
    for i in range(3):
        for j in range(3):
            button_key = f"button_{i}_{j}"  # Unique key for each button
            button_label = st.session_state.board[i][j] if st.session_state.board[i][j] != '' else ' '  # Empty space if no move
            # Use a button and link the button click to the game logic
            st.button(button_label, key=button_key, on_click=button_click, args=(i, j))

# Streamlit app
st.title("Tic-Tac-Toe")

# Display winner message if there's a winner
if st.session_state.winner:
    st.subheader(f"Player {st.session_state.winner} wins!")
else:
    # Display current turn
    st.subheader(f"Player {st.session_state.turn}'s turn")

# Display the game board
update_buttons()

# Option to restart the game
if st.button("Restart Game"):
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
    st.session_state.turn = 'X'
    st.session_state.winner = None
