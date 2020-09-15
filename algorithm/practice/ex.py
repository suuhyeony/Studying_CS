def solution(board, moves):
    basket = []
    count = 0
    basket.append(0)
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                basket.append(b[m-1])
                b[m-1] = 0
                if basket[-2] == basket[-1]:
                    basket.pop()
                    basket.pop()
                    count += 2
                break
    return count