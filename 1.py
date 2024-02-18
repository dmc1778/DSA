def mergeAlternately(word1: str, word2: str) -> str:
        w1list = list(word1)
        w2list = list(word2)
        output = []
        if len(w1list) == len(w2list):
            for idx, item in enumerate(w1list):
                output.append(item)
                output.append(w2list[idx])
        elif len(w1list) > len(w2list):
            temp = w1list[:len(w2list)]
            sliced_elements = w1list[len(temp):]
            for idx, item in enumerate(temp):
                output.append(item)
                output.append(w2list[idx])
            output = output + sliced_elements
        else:
            temp = w2list[:len(w1list)]
            sliced_elements = w2list[len(temp):]
            for idx, item in enumerate(w1list):
                output.append(item)
                output.append(temp[idx])
            output = output + sliced_elements
        return "".join(output)

mergeAlternately("ab", "pqrs")