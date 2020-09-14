from tkinter import Frame,Label,CENTER

import Constant2048 as c
import 2048game

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.master.bind("<Key>,self.key_down")
        self.commands={c.Key_Up:2048game.move_up,c.Key_Down:2048game.move_down,c.Key_Left:2048game.move_left,c.key_Right:2048game.move_right}
        self.grid_cells=[]
        self.init_grid()
        self.update_grid_cells()
        self.mainloop()

    def init_grid(self):
        background=Frame(self,bd=c.Background_Color_Game,
                         width=c.Size,height=c.Size)
        background.grid()
        for i in range(c.Grid_len):
            grid_row=[]
            for j in range(c.Grid_len):
                cell=Frame(background,bg=c.Background_Color_Cell_Empty,
                           width=c.Size/c.Grid_len,
                           height=c.Size/c.Grid_len)
                cell.grid(row=i,column=j),padx=c.Grid_Padding,
                    pady=c.Grid_Padding)
                t=Label(master=cell,text='',
                        bg=c.Background_Color_Cell_Empty,
                        justify=CENTER,front=c.FONT,width=5,height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix=2048game.start_game()
        2048game.add_new_2(self.matrix)
        2048game.add_new_2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.Grid_len):
            for j in range(c.Grid_len):
                new_number=self.matrix[i][j]
                if new_number==0:
                    self.grid_cells[i][j].configure(
                        text='',bg=c.Background_Color_Cell_Empty)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),bg=c,
                                                    Background_Color_Dict(new_number),
                                                    fg=c.Cell_Color_Dict[new_number])
        self.update_idletasks()

    def key_down(self,event):
        key=repr(event.char)
        if key in self.commands:
            self.matrix,changed=self.commands[repr(event.char)](self.matrix)
            if changed:
                2048game.add_new_2(self.matrix)
                self.update_grid_cells()
                changed=False
                if 2048game.get_current_state(self.matrix)=="WON":
                    self.grid_cells[1][1].configure(text="You",bg=c.Background_Color_Empty)
                    self.grid_cells[1][2].configure(text="Win!",bg=c.Background_Color_Cell_Empty)
                if 2048game.get_current_state(self.matrix)=="LOST":
                    self.grid_cells[1][1]configure(text="You",bg=c.Background_Color_Cell_Empty)
                    self.grid._cells[1][2].configure(text="Lose!",bg=c.Background_Color_Cell_Empty)
                    
gamegrid=Game2048()            
            
        
        
