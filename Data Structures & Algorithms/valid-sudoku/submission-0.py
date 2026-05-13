class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dictBoxes = {}
        dictLignes={}
        dictColonnes = {}
        for i in range(len(board)):
            coordonnee1 = "y"+str(i//3)
            dictLignes[i] = set()
            for j in range(len(board[i])):
                if board[i][j]==".":
                    continue
                coordonnee2 = "x"+str(j//3)
                coordonnes = tuple([coordonnee1,coordonnee2])
                colonne = j   
                if board[i][j] in dictLignes[i]:
                    return False
                dictLignes[i].add(board[i][j])

                if colonne in dictColonnes:
                    if board[i][j] in dictColonnes[colonne]:
                        return False
                    else:
                        dictColonnes[colonne].add(board[i][j])
                else:
                    dictColonnes[colonne] = set()
                    dictColonnes[colonne].add(board[i][j])
                if coordonnes in dictBoxes:
                    if board[i][j] in dictBoxes[coordonnes]:
                        return False
                    else:
                        dictBoxes[coordonnes].add(board[i][j])
                else:
                    dictBoxes[coordonnes] = set()
                    dictBoxes[coordonnes].add(board[i][j])
        return True            






                
        