import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import random
import math
from tkinter import Canvas

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("450x550")
        self.root.resizable(False, False)
        
        # Create gradient background
        self.create_gradient_background()
        
        self.current_player = "X"
        self.player_x_name = "Player X"
        self.player_o_name = "Player O"
        self.vs_computer = False
        self.computer_difficulty = "Easy"
        self.board = ["-" for _ in range(9)]
        self.game_running = False
        self.x_score = 0
        self.o_score = 0
        
        self.create_menu_screen()
    
    def create_gradient_background(self):
        self.canvas = Canvas(self.root, width=450, height=550)
        self.canvas.place(x=0, y=0)
        for i in range(550):
            r = int(44 + (i/550) * (52-44))
            g = int(62 + (i/550) * (73-62))
            b = int(94 + (i/550) * (110-94))
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_line(0, i, 450, i, fill=color)

    def create_menu_screen(self):
        for widget in self.root.winfo_children():
            if widget != self.canvas:
                widget.destroy()
        
        # Title
        title = tk.Label(self.root, text="TIC TAC TOE", font=("Arial", 30, "bold"), 
                        fg="#ecf0f1", bg="#2c3e50")
        title.place(x=225, y=50, anchor="center")
        
        # Menu frame
        menu_frame = tk.Frame(self.root, bg="#34495e", bd=5, relief="ridge")
        menu_frame.place(x=225, y=300, anchor="center")
        
        # Play with Friend button
        friend_btn = tk.Button(menu_frame, text="Play with Friend", font=("Arial", 12, "bold"), 
                             width=20, height=2, bg="#3498db", fg="white", 
                             relief="flat", command=self.setup_friend_game)
        friend_btn.pack(pady=5, padx=10)
        friend_btn.bind("<Enter>", lambda e: friend_btn.config(bg="#ecf0f1", fg="#3498db"))
        friend_btn.bind("<Leave>", lambda e: friend_btn.config(bg="#3498db", fg="white"))
        
        # Play with Computer frame with dropdown
        computer_frame = tk.Frame(menu_frame, bg="#34495e")
        computer_frame.pack(pady=5, padx=10)
        
        computer_btn = tk.Button(computer_frame, text="Play with Computer", font=("Arial", 12, "bold"),
                                width=20, height=2, bg="#e74c3c", fg="white",
                                relief="flat", command=self.show_difficulty_dropdown)
        computer_btn.pack()
        computer_btn.bind("<Enter>", lambda e: computer_btn.config(bg="#ecf0f1", fg="#e74c3c"))
        computer_btn.bind("<Leave>", lambda e: computer_btn.config(bg="#e74c3c", fg="white"))
        
        # Dropdown (initially hidden)
        self.difficulty_var = tk.StringVar(value="Easy")
        self.difficulty_dropdown = ttk.Combobox(computer_frame, textvariable=self.difficulty_var,
                                              values=["Easy", "Medium", "Hard"], 
                                              state="readonly", width=10)
        self.difficulty_dropdown.pack_forget()  # Hidden by default
        
        # Quit button
        quit_btn = tk.Button(menu_frame, text="Quit", font=("Arial", 12, "bold"), 
                           width=20, height=2, bg="#7f8c8d", fg="white", 
                           relief="flat", command=self.root.quit)
        quit_btn.pack(pady=5, padx=10)
        quit_btn.bind("<Enter>", lambda e: quit_btn.config(bg="#ecf0f1", fg="#7f8c8d"))
        quit_btn.bind("<Leave>", lambda e: quit_btn.config(bg="#7f8c8d", fg="white"))

    def show_difficulty_dropdown(self):
        """Show the difficulty dropdown when clicking Play with Computer"""
        if self.difficulty_dropdown.winfo_ismapped():
            self.difficulty_dropdown.pack_forget()
        else:
            self.difficulty_dropdown.pack(pady=5)
            self.root.after(100, lambda: self.difficulty_dropdown.bind("<<ComboboxSelected>>", 
                                                                    lambda e: self.setup_computer_game(self.difficulty_var.get())))

    def setup_friend_game(self):
        self.vs_computer = False
        self.player_x_name = simpledialog.askstring("Player Name", "Enter Player 1 (X) name:", parent=self.root) or "Player X"
        self.player_o_name = simpledialog.askstring("Player Name", "Enter Player 2 (O) name:", parent=self.root) or "Player O"
        self.start_game()
    
    def setup_computer_game(self, difficulty):
        self.vs_computer = True
        self.computer_difficulty = difficulty
        self.player_x_name = simpledialog.askstring("Player Name", "Enter your name:", parent=self.root) or "Player"
        self.player_o_name = f"Computer ({difficulty})"
        self.difficulty_dropdown.pack_forget()  # Hide dropdown after selection
        self.start_game()
    
    def start_game(self):
        self.current_player = "X"
        self.board = ["-" for _ in range(9)]
        self.game_running = True
        
        for widget in self.root.winfo_children():
            if widget != self.canvas:
                widget.destroy()
        
        # Score display
        self.score_label = tk.Label(self.root, text=f"{self.player_x_name}: {self.x_score}  |  {self.player_o_name}: {self.o_score}",
                                  font=("Arial", 12), bg="#34495e", fg="white")
        self.score_label.place(x=225, y=20, anchor="center")
        
        # Turn indicator
        self.turn_label = tk.Label(self.root, text=f"{self.player_x_name}'s turn (X)", 
                                 font=("Arial", 14, "bold"), bg="#34495e", fg="#ecf0f1")
        self.turn_label.place(x=225, y=50, anchor="center")
        
        # Game board
        board_frame = tk.Frame(self.root, bg="#34495e")
        board_frame.place(x=225, y=300, anchor="center")
        
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(board_frame, text="", font=("Arial", 30, "bold"), 
                              width=5, height=2, bg="#ecf0f1", relief="flat",
                              command=lambda r=i, c=j: self.make_move(r, c))
                btn.grid(row=i, column=j, padx=5, pady=5)
                btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#bdc3c7"))
                btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#ecf0f1"))
                row.append(btn)
            self.buttons.append(row)
        
        # Control buttons
        control_frame = tk.Frame(self.root, bg="#34495e")
        control_frame.place(x=225, y=500, anchor="center")
        
        tk.Button(control_frame, text="Restart", font=("Arial", 12, "bold"), 
                 bg="#2ecc71", fg="white", relief="flat",
                 command=self.restart_game).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Menu", font=("Arial", 12, "bold"), 
                 bg="#f39c12", fg="white", relief="flat",
                 command=self.create_menu_screen).pack(side=tk.LEFT, padx=5)

    def make_move(self, row, col):
        index = row * 3 + col
        if not self.game_running or self.board[index] != "-":
            return
        
        self.board[index] = self.current_player
        self.animate_move(row, col)
        
        if self.check_win():
            winner_name = self.player_x_name if self.current_player == "X" else self.player_o_name
            if self.current_player == "X":
                self.x_score += 1
            else:
                self.o_score += 1
            self.highlight_winning_line()
            messagebox.showinfo("Game Over", f"{winner_name} wins!")
            self.game_running = False
            self.score_label.config(text=f"{self.player_x_name}: {self.x_score}  |  {self.player_o_name}: {self.o_score}")
            return
        
        if self.check_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            self.game_running = False
            return
        
        self.switch_player()
        if self.vs_computer and self.current_player == "O" and self.game_running:
            self.root.after(500, self.computer_move)

    def animate_move(self, row, col):
        btn = self.buttons[row][col]
        color = "#e74c3c" if self.current_player == "X" else "#3498db"
        btn.config(fg=color, text=self.current_player)
        for i in range(1, 11):
            alpha = i / 10
            self.root.after(i * 30, lambda a=alpha: btn.config(fg=color))

    def highlight_winning_line(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != "-":
                for j in range(3):
                    self.buttons[i//3][j].config(bg="#2ecc71")
                return
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != "-":
                for j in range(3):
                    self.buttons[j][i].config(bg="#2ecc71")
                return
        if self.board[0] == self.board[4] == self.board[8] != "-":
            for i in (0, 4, 8):
                self.buttons[i//3][i%3].config(bg="#2ecc71")
            return
        if self.board[2] == self.board[4] == self.board[6] != "-":
            for i in (2, 4, 6):
                self.buttons[i//3][i%3].config(bg="#2ecc71")

    def computer_move(self):
        if not self.game_running:
            return
        if self.computer_difficulty == "Easy":
            self.make_easy_move()
        elif self.computer_difficulty == "Medium":
            self.make_medium_move()
        elif self.computer_difficulty == "Hard":
            self.make_hard_move()

    def make_easy_move(self):
        empty_spots = [i for i, spot in enumerate(self.board) if spot == "-"]
        if empty_spots:
            position = random.choice(empty_spots)
            row, col = position // 3, position % 3
            self.make_move(row, col)

    def make_medium_move(self):
        for i in range(9):
            if self.board[i] == "-":
                self.board[i] = "O"
                if self.check_win_without_ending():
                    self.board[i] = "-"
                    row, col = i // 3, i % 3
                    self.make_move(row, col)
                    return
                self.board[i] = "-"
        for i in range(9):
            if self.board[i] == "-":
                self.board[i] = "X"
                if self.check_win_without_ending():
                    self.board[i] = "-"
                    row, col = i // 3, i % 3
                    self.make_move(row, col)
                    return
                self.board[i] = "-"
        self.make_easy_move()

    def make_hard_move(self):
        best_score = -math.inf
        best_move = None
        for i in range(9):
            if self.board[i] == "-":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = "-"
                if score > best_score:
                    best_score = score
                    best_move = i
        if best_move is not None:
            row, col = best_move // 3, best_move % 3
            self.make_move(row, col)

    def minimax(self, board, depth, is_maximizing):
        if self.check_win_for_player("O"):
            return 10 - depth
        if self.check_win_for_player("X"):
            return depth - 10
        if "-" not in board:
            return 0
        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if board[i] == "-":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = "-"
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == "-":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = "-"
                    best_score = min(score, best_score)
            return best_score

    def check_win(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != "-":
                return True
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != "-":
                return True
        if self.board[0] == self.board[4] == self.board[8] != "-":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "-":
            return True
        return False

    def check_win_without_ending(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != "-":
                return True
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != "-":
                return True
        if self.board[0] == self.board[4] == self.board[8] != "-":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "-":
            return True
        return False

    def check_win_for_player(self, player):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == player:
                return True
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] == player:
                return True
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True
        return False

    def check_tie(self):
        return "-" not in self.board

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        current_name = self.player_o_name if self.current_player == "O" else self.player_x_name
        self.turn_label.config(text=f"{current_name}'s turn ({self.current_player})")

    def restart_game(self):
        self.current_player = "X"
        self.board = ["-" for _ in range(9)]
        self.game_running = True
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", bg="#ecf0f1", fg="black")
        self.turn_label.config(text=f"{self.player_x_name}'s turn (X)")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
