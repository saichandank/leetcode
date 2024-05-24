class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        word_scores = []
        for word in words:
            word_score = sum(score[ord(char) - ord('a')] for char in word)
            word_scores.append(word_score)
        
        
        letter_count = Counter(letters)
        
        
        def can_form_word(word, available):
            word_count = Counter(word)
            for char in word_count:
                if word_count[char] > available[char]:
                    return False
            return True
        
        
        def backtrack(index, available, current_score):
            if index == len(words):
                return current_score
            
            
            max_score = backtrack(index + 1, available, current_score)
            
            
            word = words[index]
            if can_form_word(word, available):
                
                word_count = Counter(word)
                for char in word_count:
                    available[char] -= word_count[char]
                
                max_score = max(max_score, backtrack(index + 1, available, current_score + word_scores[index]))
                
                for char in word_count:
                    available[char] += word_count[char]
            
            return max_score
        
        
        return backtrack(0, letter_count, 0)
