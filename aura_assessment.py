
class Assessment:
    """
    Assessment Class for Text and String Analysis in Python.

    This class provides utility methods for NLP-related tasks:

    - top_5_words: Finds the top K most frequent words in a given text.
    - flexible_anagram: Checks whether two strings are flexible anagrams.
    - text_similarity: Calculates a similarity score between two sentences based on word overlap.
    - clean_sentence: Cleans a sentence by removing punctuation, converting to lowercase, and returning unique words.
    """

    def __init__(self):
        #constructor 
        # print("Assessment Initialized")

        pass

    def top_5_words(self,text,top_k=5,des=True,alpha=True) ->list:
        """
        Finds top K most frequent words in a given input.
        Args:
            text (str): Input text.
            top_k (int): Number of top words to return.
            des (bool): Sort by descending frequency if True.
            alpha (bool): Sort alphabetically for tie-breaking if True.
        Returns:
        List[Tuple[str, int]]: Top K words with frequencies
        """
        # Remove punctuation and convert to lowercase
        words = self.clean_sentence(text,False)

        # Repeated Word counts
        freq = {}
        for w in words:
            if w not in freq:
                freq[w] = 1
            else:
                freq[w] += 1
        # No Repeated words count is less then top_k
        if len(freq)<top_k:
            top_k=len(freq)

        # Sort by frequency (descending) -sample output also in the descending (based on des and alpha can change the order )
        sorted_words = sorted(freq.items(), 
                              key=lambda x: (x[1] if not des else -x[1],
                                             x[0] if alpha else 0)
                            )

        return sorted_words[:top_k]
    
    def flexible_anagram(self,str1, str2) ->str:
        """
        Checks whether two strings are flexible anagrams.
        """
        # Length difference check
        if abs(len(str1) - len(str2)) > 1:
            return "NO"

        freq1, freq2 = {}, {}

        # Count characters
        for ch in str1:
            freq1[ch] = freq1.get(ch, 0) + 1
        for ch in str2:
            freq2[ch] = freq2.get(ch, 0) + 1

        # Count total mismatches
        mismatch = 0
        all_chars = set(freq1.keys()).union(freq2.keys())

        for ch in all_chars:
            mismatch += abs(freq1.get(ch, 0) - freq2.get(ch, 0))

        return "YES" if mismatch <= 2 else "NO"
    def text_similarity(self,sentence1, sentence2):
        """
        Calculates similarity score between two sentences.
        """
       #Clean punctuation and spl characters
        set1 = self.clean_sentence(sentence1)
        set2 = self.clean_sentence(sentence2)

        if not set1 and not set2:
            return 0.0
        #Calculate the unique words in the two sets for find out the similarity
        intersection = len(set1.intersection(set2))
        similarity = (2 * intersection) / (len(set1) + len(set2))

        return round(similarity, 2)
    
    def clean_sentence(self,sentence,is_set=True):
        '''
        Remove punctuation and convert to lowercase
        '''
        cleaned = ""
        for ch in sentence:
            if ch.isalnum() or ch.isspace():
                cleaned += ch.lower()
        return set(cleaned.split()) if is_set else cleaned.split()

assessment_obj=Assessment()
    
text = "The quick brown fox jumps over the lazy dog. The fox was very quick and very smart."
result =assessment_obj.top_5_words(text)
print("Question 1: Find the Top 5 Most Frequent Words")
for word, count in result:
    print(word, count)
print("Question 2: Flexible Anagram Checker")
print(assessment_obj.flexible_anagram("abcd", "abce"))    
print(assessment_obj.flexible_anagram("abc", "abcd"))     
print(assessment_obj.flexible_anagram("abc", "abxyz"))   
print(assessment_obj.flexible_anagram("aabb", "abbb"))    
print(assessment_obj.flexible_anagram("abc", "def")) 

print("Question 3: Simple Text Similarity Score (No External Libraries)")

print(assessment_obj.text_similarity(
    "Artificial intelligence is transforming the world.",
    "AI is changing the world."
))

print(assessment_obj.text_similarity(
    "Generative AI creates new content.",
    "AI models can generate text, images, or music."
))

print(assessment_obj.text_similarity(
    "Cats are lovely animals.",
    "Dogs are friendly pets but bad."
))
