def solution(n):
    answer = []
    
    def recursive(n, from_pos, to_pos, aux_pos): 
        if n == 1:
            answer.append([from_pos, to_pos])
            return 
        recursive(n-1, from_pos, aux_pos, to_pos)
        answer.append([from_pos, to_pos])
        recursive(n-1, aux_pos, to_pos, from_pos)
        
    recursive(n, 1, 3, 2)
    return answer