from tkinter import *
import numpy as np

KTBanCo = 600 #Kích thước bàn cờ
KTX_O = (KTBanCo / 3 - KTBanCo / 8) / 2 #kích thước X và O
do_Day = 10 #Độ dày các đường vẽ
x_color = '#7FFF00'
o_color = '#FFC0CB'
color_red = '#DC143C'


class Tic_Tac_Toe():
    def __init__(self):
        self.window = Tk() #Tạo cửa sổ
        self.window.title('Tic-Tac-Toe') #đặt tiêu đề cho cửa sổ
        self.canvas = Canvas(self.window, width=KTBanCo, height=KTBanCo) #Tạo bàn cờ có CD và CR là KTBanCo
        self.canvas.pack() #Hiện thị vùng vẽ lên cửa sổ
        
        self.window.bind('<Button-1>', self.click) #Nhấp chuột trái

        self.initialize_board() #khởi tạo trạng thái trò chơi Tic-Tac-Toe
        self.player_X_turns = True #X bắt đầu lượt chơi
        self.board_status = np.zeros(shape=(3, 3)) #Khởi tạo trạng thái bàn cờ bằng một mảng số không, với kích thước 3x3. 

        self.player_X_starts = True #Người chơi X bắt đầu lượt chơi
        self.reset_board = False #Bàn cờ chưa cần được đặt lại
        self.gameover = False #Trò chơi chưa kết thúc
        self.tie = False #Trò chơi chưa hòa.
        self.X_wins = False
        self.O_wins = False

        self.X_score = 0
        self.O_score = 0    #số lần thắng
        self.tie_score = 0  #số lần hoà

    def mainloop(self):
        self.window.mainloop() #Phương thức này sẽ bắt đầu vòng lặp chính của trò chơi

    #vẽ một lưới 3x3 trên vùng vẽ
    def initialize_board(self):
        for i in range(2): #vẽ hai đường thẳng đứng trên vùng vẽ
            self.canvas.create_line((i + 1) * KTBanCo / 3, 0, (i + 1) * KTBanCo / 3, KTBanCo) 
                    #Mỗi đường thẳng sẽ được vẽ tại vị trí (i + 1) * KTBanCo / 3, với i có giá trị từ 0 đến 1.
        for i in range(2):
            self.canvas.create_line(0, (i + 1) * KTBanCo / 3, KTBanCo, (i + 1) * KTBanCo / 3)

    def play_again(self):           #Hàm này sẽ được gọi khi người dùng muốn chơi một trò chơi mới.
        self.initialize_board()     #đặt lại trạng thái bàn cờ về trạng thái ban đầu.
        self.player_X_starts = not self.player_X_starts         #quyết định người chơi nào sẽ bắt đầu lượt chơi trong trò chơi mới
        self.player_X_turns = self.player_X_starts              #người chơi bắt đầu lượt chơi trong trò chơi mới cũng là người chơi được di chuyển trước tiên
        self.board_status = np.zeros(shape=(3, 3))  #các ô lưới đều trống

    # ------------------------------------------------------------------
    #Vẽ O
    def ve_O(self, logical_position):
        logical_position = np.array(logical_position)   #Dòng này chuyển đổi logical_positionđối số thành mảng np. 
                                                        #Điều này là cần thiết vì convert_logical_to_grid_position()hàm yêu cầu mảng NumPy làm đầu vào.
        grid_position = self.convert_logical_to_grid_position(logical_position)   #àm để chuyển đổi vị trí logic thành giá trị pixel thực tế của tâm lưới.

        # create_oval(): vẽ một hình bầu dục tại vị trí xác định, với chiều rộng và màu đường viền xác định.
        self.canvas.create_oval(grid_position[0] - KTX_O, grid_position[1] - KTX_O,
                                grid_position[0] + KTX_O, grid_position[1] + KTX_O, width=do_Day,
                                outline=o_color)

    #Vẽ X
    def ve_X(self, logical_position):
        logical_position = np.array(logical_position)
        grid_position = self.convert_logical_to_grid_position(logical_position)

        #create_line(): vẽ một đường từ góc trên bên trái của lưới đến góc dưới bên phải
        self.canvas.create_line(grid_position[0] - KTX_O, grid_position[1] - KTX_O,
                                grid_position[0] + KTX_O, grid_position[1] + KTX_O, width=do_Day,
                                fill=x_color)
        
        #create_line():vẽ một đường từ góc dưới bên trái của lưới đến góc trên cùng bên phải
        self.canvas.create_line(grid_position[0] - KTX_O, grid_position[1] + KTX_O,
                                grid_position[0] + KTX_O, grid_position[1] - KTX_O, width=do_Day,
                                fill=x_color)

    def display_gameover(self):
        if self.X_wins:
            self.X_score += 1
            text = '(X) WIN'
            color = x_color

        elif self.O_wins:
            self.O_score += 1
            text = '(O) WIN'
            color = o_color
        else:
            self.tie_score += 1
            text = 'HOÀ'
            color = '#000080'

        self.canvas.delete("all")       #xóa tất cả các đối tượng trên khung vẽ
        self.canvas.create_text(KTBanCo / 2, KTBanCo / 4, font="cmr 70 bold", fill= color, text=text) # tạo một đối tượng văn bản trên khung vẽ ở giữa khung vẽ

        score_text = 'Scores \n'
        self.canvas.create_text(KTBanCo / 2, 5 * KTBanCo / 9, font="cmr 40 bold", fill=color_red,
                                text=score_text)
        #danh sach diem
        score_text =  'P1 (X): ' + str(self.X_score) + '\n'
        score_text += 'P2 (O): ' + str(self.O_score) + '\n'
        score_text += 'Hoà    : ' + str(self.tie_score)

        self.canvas.create_text(KTBanCo / 2, 3 * KTBanCo / 4, font="cmr 30 bold", fill=color_red,
                                text=score_text)
        self.reset_board = True  #reset khi click again

        score_text = 'Click to play again \n'
        self.canvas.create_text(KTBanCo / 2, 15 * KTBanCo / 16, font="cmr 20 bold", fill="gray",
                                text=score_text)


    def convert_logical_to_grid_position(self, logical_position):
        logical_position = np.array(logical_position, dtype=int)  #chuyển đổi vị trí logic thành mảng NumPy
        return (KTBanCo / 3) * logical_position + KTBanCo / 6     # tính toán vị trí lưới

    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (KTBanCo / 3), dtype=int)

    #Hàm is_grid_occupied()lấy một vị trí logic làm đầu vào và trả về True nếu vị trí lưới bị chiếm và Falsengược lại
    def is_grid_occupied(self, logical_position):
                #Hàm kiểm tra giá trị của phần tử tương ứng trong self.board_statusmảng. 
                #Nếu giá trị là 0 thì vị trí lưới trống và hàm trả về False. 
                #Nếu giá trị khác 0 thì vị trí lưới bị chiếm và hàm trả về True.
        if self.board_status[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True

    def is_winner(self, player):
        player = -1 if player == 'X' else 1     #X biểu thị -1 và O biểu thị 1
        for i in range(3):
                    #kiểm tra xem người chơi có thắng hay không bằng cách sắp xếp ba biểu tượng của họ thành một hàng, theo chiều ngang hoặc chiều dọc
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                return True
            if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                return True

                #Hai ifcâu lệnh này kiểm tra xem người chơi có thắng hay không bằng cách sắp xếp ba biểu tượng của họ theo đường chéo
        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
            return True

        if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
            return True

        return False

    def is_tie(self):
            #r chứa chỉ mục hàng của các vị trí lưới trống
            #c chứa chỉ mục cột của các vị trí lưới trống.
        r, c = np.where(self.board_status == 0)  # np.where():tìm tất cả các vị trí lưới trống trên bảng trò chơi
        tie = False
        if len(r) == 0:
            tie = True

        return tie

    def is_gameover(self):
        self.X_wins = self.is_winner('X')
        if not self.X_wins:
            self.O_wins = self.is_winner('O')

        if not self.O_wins:
            self.tie = self.is_tie()

        gameover = self.X_wins or self.O_wins or self.tie

        if self.X_wins:
            print('X wins')
        if self.O_wins:
            print('O wins')
        if self.tie:
            print('Its a tie')

        return gameover

            #sự kiện nhấp chuột
    def click(self, event):
        grid_position = [event.x, event.y] #lấy tọa độ nhấp chuột từ eventđối tượng và lưu chúng vào grid_positionbiến.
        logical_position = self.convert_grid_to_logical_position(grid_position) #chuyển đổi tọa độ nhấp chuột thành tọa độ logic

            #kiểm tra xem trò chơi có đang được thiết lập lại hay không. 
            #Nếu không, hàm sẽ tiến hành xử lý sự kiện click chuột.
        if not self.reset_board:
            if self.player_X_turns:  #kiểm tra xem đây có phải là người chơi có biểu tượng 'X' hay không
                if not self.is_grid_occupied(logical_position): #kiểm tra xem ô lưới ở tọa độ logic có bị chiếm hay không
                    self.ve_X(logical_position)     #hàm sẽ vẽ chữ X trên khung vẽ
                    self.board_status[logical_position[0]][logical_position[1]] = -1
                    self.player_X_turns = not self.player_X_turns #đến lượt người chơi có biểu tượng 'O'
            else:
                if not self.is_grid_occupied(logical_position):
                    self.ve_O(logical_position) #hàm sẽ vẽ chữ O trên khung vẽ
                    self.board_status[logical_position[0]][logical_position[1]] = 1
                    self.player_X_turns = not self.player_X_turns


                #kiểm tra xem trò chơi đã kết thúc chưa
            if self.is_gameover():
                self.display_gameover()
        else:  # Play Again
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False


game = Tic_Tac_Toe()
game.mainloop()