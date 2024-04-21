from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
from game import Game


app = FastAPI()
board = Game()

abc = 'abcdefgh'


def get_pos(x, y):
    return f'{abc[x - 1]}{y}'


def get_x_y(pos):
    return abc.index(pos[0]) + 1, int(pos[1])


@app.get("/show_board_console")
def show_board_console():
    board_representation = board.print_board()
    return JSONResponse(content={"board": board_representation})


@app.get("/show_board", response_class=HTMLResponse)
def show_board():
    board_html = "<table>"
    l = list(board.board.values())
    l = ['_' if not i else i for i in l]
    l = [l[i: i + 8] for i in range(0, 64, 8)]
    for i, row in enumerate(l):
        board_html += "<tr>"
        for j, square in enumerate(row):
            cell_name = get_pos(j + 1, 8 - i)
            square_repr = str(square) if square is not None else "_"
            board_html += f"<td>{cell_name}: {square_repr}</td>"
        board_html += "</tr>"
    board_html += "</table>"
    return board_html


@app.put("/move/{position_from}/{position_to}/")
def move(position_from: str, position_to: str):
    try:
        from_pos = get_x_y(position_from)
        to_pos = get_x_y(position_to)
        board.move(from_pos, to_pos)
        return {"Response": "Success"}
    except ValueError as e:
        return {"Response": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
