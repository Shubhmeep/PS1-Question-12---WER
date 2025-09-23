from jiwer import process_words

ref = "For fall break I want to go hiking by the lake and watch the sunset I also plan to attend the Inter Miami soccer game and I want to watch Messi play"
hyp = "For fall break I want to go hiking by the lake and watch the sunset I also plan to attend the ITA Magny soccer game and I want to watch messy play"

# Process alignment
result = process_words(ref, hyp)

print("WER:", result.wer*100)
print("Substitutions:", result.substitutions)
print("Insertions:", result.insertions)
print("Deletions:", result.deletions)





