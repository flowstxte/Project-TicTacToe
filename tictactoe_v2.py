import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        self.current_player = "X"
        self.player_x_name = "Player X"
        self.player_o_name = "Player O"
        self.vs_computer = False
        self.board = ["-" for _ in range(9)]
        self.game_running = False
        
        self.create_menu_screen()
    
    def create_menu_screen(self):
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        title_label = tk.Label(self.root, text="TIC TAC TOE", font=("Arial", 24, "bold"), bg="#2c3e50", fg="white")
        title_label.pack(pady=30)
        
        # Frame for buttons
        menu_frame = tk.Frame(self.root, bg="#2c3e50")
        menu_frame.pack(pady=20)
        
        # Play with Friend button
        friend_button = tk.Button(menu_frame, text="Play with Friend", font=("Arial", 12), 
                                 width=20, height=2, bg="#3498db", fg="white", 
                                 command=self.setup_friend_game)
        friend_button.pack(pady=10)
        
        # Play with Computer button
        computer_button = tk.Button(menu_frame, text="Play with Computer", font=("Arial", 12), 
                                   width=20, height=2, bg="#e74c3c", fg="white", 
                                   command=self.setup_computer_game)
        computer_button.pack(pady=10)
        
        # Quit button
        quit_button = tk.Button(menu_frame, text="Quit", font=("Arial", 12), 
                               width=20, height=2, bg="#7f8c8d", fg="white", 
                               command=self.root.quit)
        quit_button.pack(pady=10)
    
    def setup_friend_game(self):
        self.vs_computer = False
        self.player_x_name = simpledialog.askstring("Player Name", "Enter Player 1 (X) name:", parent=self.root) or "Player X"
        self.player_o_name = simpledialog.askstring("Player Name", "Enter Player 2 (O) name:", parent=self.root) or "Player O"
        self.start_game()
    
    def setup_computer_game(self):
        self.vs_computer = True
        self.player_x_name = simpledialog.askstring("Player Name", "Enter your name:", parent=self.root) or "Player"
        self.player_o_name = "Computer"
        self.start_game()
    
    def start_game(self):
        # Reset game state
        self.current_player = "X"
        self.board = ["-" for _ in range(9)]
        self.game_running = True
        
        # Clear menu and create game board
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Create game info frame
        info_frame = tk.Frame(self.root, bg="#2c3e50")
        info_frame.pack(pady=10)
        
        self.turn_label = tk.Label(info_frame, text=f"{self.player_x_name}'s turn (X)", 
                                  font=("Arial", 14), bg="#2c3e50", fg="white")
        self.turn_label.pack()
        
        # Create game board frame
        board_frame = tk.Frame(self.root, bg="#34495e")
        board_frame.pack(pady=10)
        
        # Create buttons for the board
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(board_frame, text="", font=("Arial", 24, "bold"), 
                                  width=5, height=2, bg="#ecf0f1",
                                  command=lambda r=i, c=j: self.make_move(r, c))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        
        # Create bottom buttons
        bottom_frame = tk.Frame(self.root, bg="#2c3e50")
        bottom_frame.pack(pady=20)
        
        restart_button = tk.Button(bottom_frame, text="Restart", font=("Arial", 12), 
                                  width=10, bg="#2ecc71", fg="white", 
                                  command=self.restart_game)
        restart_button.pack(side=tk.LEFT, padx=10)
        
        menu_button = tk.Button(bottom_frame, text="Main Menu", font=("Arial", 12), 
                               width=10, bg="#f39c12", fg="white", 
                               command=self.create_menu_screen)
        menu_button.pack(side=tk.LEFT, padx=10)
    
    def make_move(self, row, col):
        index = row * 3 + col
        
        if not self.game_running or self.board[index] != "-":
            return
        
        # Update button and board
        self.board[index] = self.current_player
        self.buttons[row][col].config(text=self.current_player, 
                                     fg="#e74c3c" if self.current_player == "X" else "#3498db")
        
        # Check for win or tie
        if self.check_win():
            winner_name = self.player_x_name if self.current_player == "X" else self.player_o_name
            messagebox.showinfo("Game Over", f"{winner_name} wins!")
            self.game_running = False
            return
        
        if self.check_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            self.game_running = False
            return
        
        # Switch player
        self.switch_player()
        
        # If playing against computer and it's computer's turn
        if self.vs_computer and self.current_player == "O" and self.game_running:
            self.root.after(500, self.computer_move)  # Delay for better UX
    
    def computer_move(self):
        if not self.game_running:
            return
            
        # Find empty spots
        empty_spots = [i for i, spot in enumerate(self.board) if spot == "-"]
        
        if empty_spots:
            position = random.choice(empty_spots)
            row, col = position // 3, position % 3
            self.make_move(row, col)
    
    def check_win(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != "-":
                return True
        
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != "-":
                return True
        
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != "-":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "-":
            return True
        
        return False
    
    def check_tie(self):
        return "-" not in self.board
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        current_name = self.player_o_name if self.current_player == "O" else self.player_x_name
        self.turn_label.config(text=f"{current_name}'s turn ({self.current_player})")
    
    def restart_game(self):
        # Reset game state
        self.current_player = "X"
        self.board = ["-" for _ in range(9)]
        self.game_running = True
        
        # Reset buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", fg="black")
        
        # Reset turn label
        self.turn_label.config(text=f"{self.player_x_name}'s turn (X)")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
